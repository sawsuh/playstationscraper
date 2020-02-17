import json
import math

with open('out.json') as f:
    data = []
    for line in f:
        data.append(json.loads(line))

tuplist = []
for game in data:
    title = game['title']
    rating = game['rating']
    price = game['price']
    group = math.floor( float(price[1:]) / 20 )
    tuplist.append((f'{title} - {price} ({rating})', rating, group))

tuplist.sort(key=lambda x : x[1], reverse=True)
tuplist.sort(key=lambda x : x[2])

for item, rating, group in tuplist:
    if rating in ['tbd', 'unknown']:
        continue
    print(item) 
