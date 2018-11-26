metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)), 
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas: 
    if longitude <= 0: 
        print(fmt.format(name, latitude, longitude))

metro_areas = reversed(metro_areas)

# 元组中放置可变对象时
# 改变可变对象的值，但是error也发生
t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except Exception as e:
    print(e)
finally :
    print(t)

# 改变可变对象的值，而且error不发生
s = [30, 40]
t = (1, 2, s)
try:
    s += [50, 60]
except Exception as e:
    print(e)
finally :
    print(t)