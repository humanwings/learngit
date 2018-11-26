from pyquery import PyQuery as pq

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''

doc = pq(text)
#print(doc.html())
#print(doc)
#print(type(doc))

li = doc('li')
#print(li.text())
#print(type(li))

p = pq('<p id="hello" class="hello"></p>')
print(p.attr("id"))
print(p.attr("id", "plop"))
print(p.attr("id", "hello"))

print(p.addClass('beauty'))
print(p.removeClass('hello'))
print(p.css('font-size', '16px'))
print(p.css({'background-color': 'yellow'}))

print(p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>'))
print(p.prepend('Oh yes!'))
d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
p.prependTo(d('#test'))
print(p)
print(d)
d.empty()
print(d)


