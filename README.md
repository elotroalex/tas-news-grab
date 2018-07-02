README

## From Rachel

API NEWS APPROACH

Towards the end of the evening I realised everyone had given up on using APIs for news searching and were using RSS instead. There seemed to be some issues with RSS so I had a quick play with Bing News API instead.

In the attached notebook there's just a proof of concept where I grab 100 news articles that mention one of the detention centres. Obviously it can easily be scaled up to loop through multiple centres. And I haven't tested how many articles we can grab at a time. The most I tried was 100.

I'm not sure (yet) how to make it do a precise match, but I'm sure it's possible.

The code as written outputs the descriptions only, but it's returning a search_results object that can be queried for e.g. url, date, headline and other elements.

It's using a trial API key that should work for 7 days. After that someone else can get a new trial key I guess.

ALTERNATIVE APPROACH:
I'm also attaching a fuzzy matching python script that Patrick wrote. The idea is to run that on the results of the RSS grabbing code that the others wrote. Their RSS code gets all news articles, not just the ones with our keywords in them. So then you run Patrick's script on the results to find the relevant articles. I think this approach may not work so great (yet) because it is only returning headlines, not any further text.



