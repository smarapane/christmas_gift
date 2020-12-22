from settings import ACCOUNT_SID, AUTH_TOKEN, FROM, TO
import requests
import json
from twilio.rest import Client
from random import randint


def get_pic():
    num = randint(0, 1)
    if num == 0:
        return get_doggo()
    elif num == 1:
        return get_kitten()


def get_doggo():
    url = "https://dog.ceo/api/breed/goldenretriever/images/random"
    return json.loads(requests.get(url).content)["message"]


def get_kitten():
    url = "https://api.thecatapi.com/v1/images/search"
    return json.loads(requests.get(url).content)[0]["url"]


def send_message():
    message = client.messages.create(
        body="test",
        from_=FROM,
        media_url=get_pic(),
        to=TO
    )


if __name__ == "__main__":
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    send_message()
