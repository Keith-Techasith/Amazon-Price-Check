import requests
import os
from bs4 import BeautifulSoup
from smtplib import SMTP
from dotenv import load_dotenv

load_dotenv()


URL= "https://www.amazon.com/Organic-Ashwagandha-1300mg-Capsules-Enhancer/dp/B06ZYHJYD5/ref=sr_1_5?crid=2STMUALZ9XA9B&dib=eyJ2IjoiMSJ9.Y8mIX4FyMZ8bPGkzaNgY4Pf8YMKEYIQt8UPCZlDzZ0sqdSWooIHN829h5acxR0lGlyAVtqJ4rtAFSLW5HBWQrIpspNBwFfRjzacTbBO2oJFl4oXuJJqmKe0arsHvNBUXWAlG1TRUhBGOm0Nh6XDrqRC7vm7bBf7s2SJkmmLgt6r3lr-gAiLqeqzbVOIceoKdnRYgkV5E-CUfzqDPrTWx7MT763KK1AAbZJ-DFx0Bkw-Anvf7l_-pc1Mt_1I9Ch5GsXdTkYWgl4SsM571BUEpx3ANpiU_iVOQQAqfFBO9GBk.d6FYXZrpJhN7-pSMAXsIBFoo2Fq4ABuhovbok-JS-20&dib_tag=se&keywords=ashwagandha&qid=1733795320&rdc=1&sprefix=ash%2Caps%2C128&sr=8-5"
USER= os.environ["user"]
PASSWORD= os.environ["password"]
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7"
}

response = requests.get(url=URL,headers=header)
soup = BeautifulSoup(response.text, "html.parser")

# print(soup)
# print(f"email: {USER}, password: {PASSWORD}")

price_with_currency = soup.find(class_="a-offscreen").getText()
price_as_float = float(price_with_currency.split("$")[1])
print(price_as_float)
# if price_as_float < 100:
#     with SMTP("smtp.gmail.com") as connection: 
#         connection.starttls()
#         connection.login(user=USER,password=PASSWORD)
#         connection.sendmail(from_addr=USER, to_addrs=USER, msg=f"Subject:Price drop\nThe price reduced to {price_as_float}")