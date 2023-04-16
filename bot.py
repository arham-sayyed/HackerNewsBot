from news import get_latest_news
from image_processor import create_image_with_title
from twitter import tweet_img_with_text
from pytelegram import telegram
import time

def main():
    news = get_latest_news()
    if news is not None:
        title = news['title']
        image_url = news['image']
        summary = news['summary']
        full_article = news['full_article']
        
        # text = str(title) + "\n" + str(summary) + "\n" + str(f"Read the full Article at: {full_article}")
        text = title + "\n" + str(f"Read the full Article at: {full_article}")

        image_path , filename = create_image_with_title(title=title , image_url=image_url)

        if image_path is not None:
            is_tweeted = tweet_img_with_text(tweet_text= text, image_path= image_path, filename= filename) 
            is_telegramed = telegram(title= title , summary= (summary + "\n" + "\n" + str(f"<b>Read the full Article at: {full_article}</b>")), imagepath= image_path)

        else:
            print("image not found")
            return
        
        if is_tweeted is not None:
            print("Successfully Tweeted!")


while True:
    main()
    time.sleep(60*60)

         
