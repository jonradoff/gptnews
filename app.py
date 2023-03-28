#
# Prompted into existence by Jon Radoff with the help of GPT-4.
#  Find me here:
#   https://twitter.com/jradoff
#   https://linkedin.com/in/jonradoff
#   https://linktr.ee/metavert
#   https://github.com/jonradoff
# This code is public domain. Do whatever you want with it! (Creative Commons Zero v1.0)
#

import requests
import feedparser
from bs4 import BeautifulSoup
import openai
from flask import Flask, render_template_string

from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def truncate_text(text, max_tokens):
    tokens = tokenizer.tokenize(text)
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
    return tokenizer.convert_tokens_to_string(tokens)

# Set up OpenAI API
openai.api_key = "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"

app = Flask(__name__)

# List of RSS feed URLs
feeds = [
    "https://openai.com/blog",
    "http://feeds.feedburner.com/blogspot/gJZg",
]

def extract_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    content = soup.find("div", {"class": "post-body"})
    if content is not None:
        return content.text.strip()
    else:
        return None

# Function to summarize articles
def summarize_articles():
    summaries = []

    for feed_url in feeds:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            title = entry.title
            link = entry.link

            try:
                content = extract_content(link)
                if content is None:
                    raise ValueError("Content not found")
            except Exception as e:
                print(f"Error extracting content from {link}: {e}")
                continue

            max_content_tokens = 3950  # Adjust this number based on your needs
            truncated_content = truncate_text(content, max_content_tokens)
            prompt = f"Please summarize the following article: {title}\n\n{truncated_content}"
            
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=50,
                n=1,
                stop=None,
                temperature=0.7,
            )

            summary = response.choices[0].text.strip()
            summaries.append({"title": title, "link": link, "summary": summary})

    return summaries

@app.route("/")
def index():
    summaries = summarize_articles()
    template = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>News Summary</title>
        <style>
            body { font-family: Arial, sans-serif; }
            h1 { text-align: center; }
            .article { border-bottom: 1px solid #ccc; padding-bottom: 10px; margin-bottom: 20px; }
            .article h2 { margin-top: 0; }
            .article a { color: #007bff; text-decoration: none; }
            .article a:hover { text-decoration: underline; }
        </style>
      </head>
      <body>
        <h1>Daily News Summary</h1>
        {% for summary in summaries %}
            <div class="article">
                <h2>{{ summary.title }}</h2>
                <p>{{ summary.summary }}</p>
                <p><a href="{{ summary.link }}" target="_blank">Read more</a></p>
            </div>
        {% endfor %}
      </body>
    </html>
    """
    return render_template_string(template, summaries=summaries)

if __name__ == "__main__":
    app.run(debug=True)
