#!/bin/python3
from requests import get
from os.path import isfile
from os import remove
from bs4 import BeautifulSoup as bs
from zipfile import ZipFile

if not isfile("cookie.txt"):
    c = input("cookie: ")
    with open("cookie.txt", "w") as f:
        f.write("sessionid=" + c)
else:
    with open("cookie.txt", "r") as f:
        c = f.read()

url ="https://dreamhack.io/wargame/challenges/"

n = input("문제 번호: ")

r = get(url + n, headers={"Cookie": c})

soup = bs(r.text, "html.parser")

link = soup.find("div", {"id": "challenge-info"}).find("div", {"class": "row"}).find("div").find("a").attrs["href"]

with open(n + ".zip", "wb") as f:
    f.write(get(link).content)

with ZipFile(n + ".zip", "r") as f:
    f.extractall(path="./" + n)

remove(n + ".zip")
