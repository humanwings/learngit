from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
<b><!--Hey, buddy. Want to buy a used parser?--></b>
"""

soup = BeautifulSoup(html_doc, 'html.parser')


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id)

tag = soup.b
print(tag.string)
for i,element in enumerate(tag.next_elements):
    print(i)
    print(element.string)

print(soup.prettify())

print(soup.name)

tag = soup.a
print(tag.name)
print(tag.attrs)
print(tag['class'])
print(tag['href'])
print(tag['id'])

del tag['class']
print(soup)

print(tag.string)
tag.string.replace_with("wujian")

tags = soup.find_all("a")
print(len(tags))
print(tags[0].string)

print(len(soup.body.contents))
for item in soup.body.contents :
   print(item)

for child  in soup.body.children :
   print(child )

for child in soup.body.descendants:
   print(child)

for string in soup.stripped_strings :
   print("-------------------------------")
   print(string)

for string in soup.strings :
   print("-------------------------------")
   print(string)

tag =  soup.find_all("a")[1]
print(tag.string)
print(tag.next_sibling.next_sibling.string)
print(tag.previous_sibling.previous_sibling.string)
print()
print(tag.string)
print(tag.next_element.next_element.string)
print(tag.previous_element.previous_element.string)

