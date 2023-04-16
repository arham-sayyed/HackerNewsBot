import requests
from api_secrets import telegram_secrets


def telegram(title, summary, imagepath, recipient="ALL"):

    recipients = telegram_secrets['recipients']
    API_KEY = telegram_secrets['API_KEY']

    
    if (not recipient in list(recipients.keys())) and (not recipient == "ALL"):
        print(list(recipients.keys()))
        print("Invalid Recipient")
        return

    if recipient == "ALL":
        for key, value in recipients.items():
            id = value
            url = f"https://api.telegram.org/bot{str(API_KEY)}/sendPhoto"
            files = {"photo": open(imagepath, "rb")}
            data = {"chat_id": id, "caption": f"<b>{title} \n</b>\n{summary}", 'parse_mode': 'HTML'}
            # headers = {"Content-Type": "image/jpeg"} # or "Content-Type": "image/png" if the file is in PNG format
            response = requests.post(url, data=data, files=files)
    
    else:
        id = recipients[recipient]
        url = f"https://api.telegram.org/bot{str(API_KEY)}/sendPhoto"
        files = {"photo": open(imagepath, "rb")}
        data = {"chat_id": id, "caption": f"<b>{title} \n</b>\n{summary}", 'parse_mode': 'HTML'}
        # headers = {"Content-Type": "image/jpeg"} # or "Content-Type": "image/png" if the file is in PNG format
        response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        print("Success!")
    else:
        print("Failed!")
        print(response.text)
