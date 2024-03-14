import requests, bs4

res = requests.get('http://nostarch.com')
try:
    res.raise_for_status()
except Exception as exc:
    print("Website failed to load due to error: %s" % (exc))
noStarchSoup = bs4.BeautifulSoup(res.text, features='html.parser')
print(type(noStarchSoup))

# here we'll make a beautiful soup object from our example html file

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, features='html.parser')
print(type(exampleSoup))