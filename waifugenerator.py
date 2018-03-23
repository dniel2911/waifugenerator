# SCRIPT BY MOE POI~
from bs4 import BeautifulSoup as bs
from random import randint
from random import choice
import requests as rq
import json
import lxml

class Waifu():

	def __init__(self):
		print ("====== THIS SCRIPT BY MOE POI ~ ======" + "\n")

	def Generator(self):
		hasil = []
		pagez = randint(1, 9)
		req1 = "http://jurnalotaku.com/page/{}/?s=%5Bwaifu+wednesday%5D".format(str(pagez))
		req2 = "http://jurnalotaku.com/?s=%5Bwaifu+wednesday%5D"
		reqs = [req1,req2]
		reqz = choice(reqs)
		req = rq.get(reqz)
		soup = bs(req.text, "lxml")
		for xx in soup.find_all('div', {'class':'article-inner-wrapper'}):
			for zz in xx.find_all('div', {'class':'cover size-a has-depth'}):
				for ff in zz.find_all('img'):
					images = ff.get('src')
					namez = ff.get('alt')
					names = namez.replace("[Waifu Wednesday] ","")
					mergez = names + " xxx " + images
					hasil.append(mergez)
		generatedwaifu = choice(hasil)
		return generatedwaifu

waifu = Waifu()
gen = waifu.Generator()
genx = gen.split(" xxx ")
titlexz = genx[0]
linkxz = genx[1]
print ("Title : " + linkxz + "\nImage Link : " + titlexz)
