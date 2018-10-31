import requests as rq

r = rq.get('https://dummyimage.com/600X400/000/fff')

open('fff.jpg', 'wb').write(r.content)
