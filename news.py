from pprint import pprint

from finnews.client import News

# Start
news_client = News()

#Wall Street Journal client start
wsj_client = news_client.wsj

#WSJ Feeds
wsj_bus = wsj_client.us_business_news()
wsj_mkt = wsj_client.market_news()


# #SPGlobal client start
# sp_global_client = news_client.sp_global

# #SPGlobal Feeds
# sp_indicies = sp_global_client.all_indicies()


print(type(wsj_bus))
for articles in wsj_bus:
    print(articles['title'])
    print(articles['link'])
    print()