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
    try:
        price = float(game['price'][1:])
    except TypeError:
        continue
    try:
        group = math.floor( float(rating) / 10 )
    except ValueError:
        continue
    tuplist.append((f'{title} - {price} ({rating})', price, group))

tuplist.sort(key=lambda x : x[1])
tuplist.sort(key=lambda x : x[2], reverse=True)

for item, rating, group in tuplist:
    if rating in ['tbd', 'unknown']:
        continue
    print(item) 
