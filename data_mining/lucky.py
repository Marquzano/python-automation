#! /home/marquzano/workspace/data_mining/bin/python3
# lucky.py opens the first 5 pages for a single google search

import requests, webbrowser, sys, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://www.google.com/search?q=' + ' '.join(sys.argv[1:]))

res.raise_for_status()

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# open a browser tab for each result
# need to determine how to find the search results and not the first hrefs for the first a tags
# have attempted searching using class .g Ww4FFB vt6azd tF2Cxc asEBEc found
# for the first results that didn't match with the first a tags class.
# have also attempted using jsname='UWckNb' attribute which only show for dedicated
# search results.
linkElems = soup.select('.r a')# <-- issue is here
print(linkElems[0].get('href')) # logging here to debug and see the first href given
numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     webbrowser.open('http://google.com' + linkElems[i].get('href'))

# example search is 'Linux basics for intermediate users'
# expecting first href to be 'https://www.w3resources.com/slides/linux-commands-for-intermediate-users.php'