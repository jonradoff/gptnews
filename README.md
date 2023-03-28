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

--- background ---

If you want to try the same prompts I did:

1) Choose GPT-4 in ChatGPT

<img width="787" alt="Screenshot 2023-03-28 at 9 18 02 AM" src="https://user-images.githubusercontent.com/24194539/228249785-b15842c1-eb84-4b56-a5de-50b05b31550a.png">

2) Initial prompt:

How can I create a webpage that automatically observes several blogs and news feeds I care about, and summarizes the articles using GPT?  I need something that gives me a daily summary of news I should care about most.

[...]

can you give me a version of the above code that is implemented with Flask?

3) I had to address a couple errors; here's what I also prompted along the way:

I tried this but I'm getting some errors that look like this (ai.googleblog.com is an RSS feed I pointed at)

Error extracting content from http://ai.googleblog.com/2023/03/presto-multilingual-dataset-for-parsing.html: 'NoneType' object has no attribute 'text'

What should I fix?

4) The Google blog was failing with an error, so I got some extra help to handle this case:

How can I deal with this error?

openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens, however you requested 4151 tokens (4101 in your prompt; 50 for the completion). Please reduce your prompt; or completion length.

...everything basically worked after the suggested changes from ChatGPT.

