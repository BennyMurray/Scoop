# -*- coding: utf-8 -*-
from mechanize import Browser
from bs4 import BeautifulSoup
from IDFetcher import IDFetcher
import re



#SET UP HEADLESS BROWSER
#-----------------------#

#Creates browser object
br = Browser()

#Set robots and user-agent (prevents HTTP 500 from some websites)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'), ('Accept', '*/*')]



#SCRAPE BEER NAMES, ALCOHOL CONTENT AND RATEBEER IMAGE IDS FROM THE INTERNET
#--------------------------------------------------------------------------#


def scrapeBeers():

    page_number = 1

    beer_dict = {}
    #Scrapes 17 Pages (approx - 300 beers)
    for i in range(17):

        counter = 0

        #Opens webpage at 'pagenumber'
        page = br.open("http://www.drinkstore.ie/WORLD-%26-CRAFT-BEER/?page=" + str(page_number))

        #Parses html to find values for name and alcohol content
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

        print "Scraped webpage number",page_number," without issue..."
        page_number += 1


    # Scrape Beer IDs from RateBeer
    for beername in beer_dict:
        beerID = IDFetcher(beername)
        if beer_dict[beername][1] is None:
            beer_dict[beername][1] = "ID NOT FOUND for " + beername

        else:
            beer_dict[beername][1] = beerID
        print "Fetched BeerID value for ", beername



    return beer_dict


