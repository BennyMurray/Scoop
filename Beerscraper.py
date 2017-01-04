# -*- coding: utf-8 -*-
import pickle
from mechanize import Browser
from bs4 import BeautifulSoup
from BrowserSearch import browsersearch
import re

br = Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'), ('Accept', '*/*')]

def scrapeBeers():
    page_number = 1

    beer_dict = {}
    for i in range(1):

        counter = 0
        page = br.open("http://www.drinkstore.ie/WORLD-%26-CRAFT-BEER/?page=" + str(page_number))

        soup = BeautifulSoup(page, "html.parser")
        soup_names = soup.find_all('a', class_='product-link')
        titles = re.findall(r"[jpg\"bmp]+\stitle=\"[A-Za-z0-9'úúáéíóúüÁÉÍÓÚÜÖöèêëâàùûÿœôîïÈÊËÂÀÙÛŸŒÔÎÏ\.\s]+", str(soup_names))

        soup_strength = soup.find_all('span', class_='product-summary')
        strength = re.findall(r"<br\/>ABV\s[0-9]+[\.0-9%]+", str(soup_strength))

        if len(titles) != len(strength):
            page_number += 1
            continue

        titles2 = []

        for i in titles:
             titles2.append(re.sub(r"[0-9]+ML","", i))

        for i in titles2:
            beer_dict[i[12:]] = [strength[counter][9:-1], ""]
            counter += 1

        print "compiled page ",page_number," without issue"
        page_number += 1


    # Scrape Beer IDs from RateBeer
    for beername in beer_dict:
        beerID = browsersearch(beername)
        if beer_dict[beername][1] is None:
            beer_dict[beername][1] = "ID NOT FOUND"

        else:
            beer_dict[beername][1] = beerID
        print "fetched ID for ", beername



    #pickle.dump(beer_dict, open("save.p", "wb"))

    print beer_dict
    return beer_dict


