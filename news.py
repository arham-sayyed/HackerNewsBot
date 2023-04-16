import feedparser


last_update_time = None

def get_latest_news():
    global last_update_time
    try:
        feed = feedparser.parse("https://feeds.feedburner.com/TheHackersNews")
        news_item = feed['entries'][0]

        # check if the RSS feed has been updated since the last time
        if last_update_time is None or news_item['published'] != last_update_time:
            last_update_time = news_item['published']

            title = news_item['title']
            publish_date = news_item['published']
            summary = news_item['summary']
            full_article = news_item['link']
            try:
                image = news_item['links'][1]['href']
            except:
                image = None
            return {'title': title , 'publish_date': publish_date, 'summary': summary, 'full_article': full_article, 'image': image}
        else:
            print("no latest news")
            return None
        
    except Exception as e:
        print(f"ERROR while 'get_latest_news': {e}")
        return None
