import requests
import time

while True:

    response = requests.get("https://api.thecatapi.com/v1/images/search")

    data = response.json()

    url = data[0]['url']

    photo = requests.get(url)

    img = open("file.jpg", "wb")

    img.write(photo.content)

    img.close()

    time.sleep(2)