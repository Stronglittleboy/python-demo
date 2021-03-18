import requests
from bs4 import BeautifulSoup


class Dog():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello,World!")


# dog = Dog("李白", 51);
# dog.sayHello()
# print(dog.name)
# print(dog.age)
# dog.age = 20
# print(dog.age)
# link = "http://www.santostang.com/"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# r = requests.get(link, headers=headers)
# print(r.text)
# soup= BeautifulSoup(r.text, "html.parser")
# title = soup.find("h1", class_="post-title").a.text.title()
# print(title)
# we
