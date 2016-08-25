# -*- coding: utf-8 -*-
from random import randint

drzave_mesta = {"Slovenija": "Ljubljana",
                "Hrvaška": "Zagreb",
                "Avstrija": "Dunaj"}

drzave_slike = {"Slovenija": "http://www.hotelcubo.com/wp-content/uploads/2014/09/Ljubljana_Jeseni%C4%8Dnik.jpg",
                "Hrvaška": "http://www.travelandleisure.com/sites/default/files/styles/tnl_redesign_article_landing_page/public/1448052729/zagreb-croatia-WTG0116.jpg?itok=IIpWCtBo",
                "Avstrija": "http://www.austria.info/media/17083/thumbnails/stadtansicht-wien--oesterreich-werbung-julius-silver--d.jpg.3146497.jpg"}

nakljucno = randint(0, 2)
drzava = drzave_mesta.keys()[nakljucno]
slika = drzave_slike.keys()[nakljucno]
#ugibanje = raw_input("Katero je glavno mesto države " + drzava + ": ")

'''
preverba_ugibanja(ugibanje, drzave_mesta, drzava)
def preverba_ugibanja(guess, slovar, country):
    if guess.lower() == slovar[country].lower():
        print("Pravilno!")
        return True
    else:
        print("Narobe")
        return False
'''
print drzava
print slika
print drzave_mesta[drzava]
print drzave_slike[drzava]