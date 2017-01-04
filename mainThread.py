from __future__ import division

from Beerscraper import scrapeBeers
from reviewScraper import scrapeReviews
from SemanticAnalyser import getValues
import pickle
import time


def compileBeerList():


    start = time.time()

    counter = 0

    beer_data_list = []


    # #beer_dict = scrapeBeers()
    beer_dict = scrapeBeers()



    #For each beer in the beer_dictionary
    for beerName in beer_dict:

        #Scrape and clean 3 pages of reviews
        word_list = scrapeReviews(beerName, beer_dict[beerName][1])

        #Analyse the reviews and return values for colour, bitterness, strenght and acidity

        try:
            image_link = 'http://res.cloudinary.com/ratebeer/image/upload/w_250,c_limit/beer_' + beer_dict[beerName][1] + '.jpg'
        except TypeError:
            image_link = "image not found"

        value_list = getValues(word_list, beer_dict[beerName][0], beerName)
        beer_data_list.append([beerName, beer_dict[beerName][1], value_list[0], value_list[1], value_list[2], value_list[3], image_link])
        counter += 1

        print (counter/len(beer_dict) * 100),"% complete"

    end = time.time()
    print end - start
    pickle.dump(beer_data_list, open("beerData.p", "wb"))
    return beer_data_list



