# gptnews
Summarizes newsfeeds using GPT. Written with GPT-4.

This was created with the assistance of GPT-4 to help me summarize newsfeeds I'm interested in.

It could probably use some improvements, but I thought this was a good starting point.
The big thing it could use is something to remember what it has previously summarized, so that it doesn't
keep going back to the GPT API and running up fees...

To get this working:

1) Install dependencies:

pip install Flask feedparser beautifulsoup4 requests openai transformers

2) Find this line in app.py:

openai.api_key = "PUT YOUR KEY HERE" 

...replace the key with your own OpenAI API secret key.

3) run the script:

python3 app.py

4) connect to your local machine via your webbrowser -- by default this will be http://127.0.0.1:5000/

Have fun! Find me here:

https://twitter.com/jradoff
https://linkedin.com/in/jonradoff
https://linktr.ee/metavert
