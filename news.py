from pprint import pprint

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the Wall Street Journal News Client.
wsj_client = news_client.wsj

# Grab the Market News Feed.
content = wsj_client.us_business_news()
# pprint(content)

for elements in content:
    pprint(elements['title'])