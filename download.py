from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys


# APIの情報

key = "2c0fcba614339e234d9cb7285a1161f2"
secret = "8443be2a6d1ea74d"
wait_time = 1


# 保存フォルダの指定

animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
pprint(photos)