import bs4

exampleFile = open('example.html')

# below will contain samples of some of functions that are useful from bs4
# for parsing html pages

exampleSoup = bs4.BeautifulSoup(exampleFile.read())
# this returns a list of the elements which contain author
elems = exampleSoup.select('#author')
# this shows that the type for elems is list
print(type(elems))
# shows us the length of the list
print(len(elems))
# gives us the type for the first element in elems
print(type(elems[0]))
# gets the value of the first element as text
author = elems[0].getText()
print(author)
# shows us what the first element truly is as a string
# and not just the text within
print(str(elems[0]))
# gives us the dictionary of the attributes and their values
# for the first element in elems
print(elems[0].attrs)

# lets pull all the <p> tags from the example file
pElems = exampleSoup.select('p')
print(str(pElems[0]))
firstParagraph = pElems[0].getText()
print(firstParagraph)
print(str(pElems[1]))
secondParagraph = pElems[1].getText()
print(secondParagraph)
print(str(pElems[2]))
thirdParagraph = pElems[2].getText()
print(thirdParagraph)