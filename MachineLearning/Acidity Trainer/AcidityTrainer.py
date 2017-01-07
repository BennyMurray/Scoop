from __future__ import division
import random
import pickle


def trainAcidity():
    acid0 = pickle.load(open("0acidbeer.p", "rb"))
    acid3 = pickle.load(open("3acidbeer.p", "rb"))
    acid6 = pickle.load(open("6acidbeer.p", "rb"))
    acid7 = pickle.load(open("7acidbeer.p", "rb"))
    acid10 = pickle.load(open("10acidbeer.p", "rb"))

    while True:
        number_set = [round(random.uniform(0.1, 15), 2) for x in range(29)]

        if analyseAcidity(acid0, number_set) == 0 and abs(analyseAcidity(acid3, number_set) - 30) < 11 and abs(analyseAcidity(acid6, number_set) - 60) < 10 and abs(analyseAcidity(acid7, number_set) - 45) < 11 and analyseAcidity(acid10, number_set) > 70:
            print "!!!!!!!!!", number_set
            break
        else:
            print analyseAcidity(acid0, number_set), analyseAcidity(acid3, number_set), analyseAcidity(acid6, number_set),analyseAcidity(acid7, number_set), analyseAcidity(acid10, number_set)



def analyseAcidity(word_list, num_set):

    acidity_synonyms_list = ["funk", "funky", "cheese", "cheesy", "sourness", "sour", "harsh", "astringent", "vinegar",
                             "diaper", "gueuze", "lambic", "horse", "brett", "wild", "hay", "stable", "lactic",
                             "barnyard", "leather", "tart", "phenolic"]

    acidity_antonyms_list = ["moderate", "balanced", "mellow", "drinkable", "sweet", "sweetness", "caramel"]

    acidity_synonyms_dict = {"funk": num_set[0], "funky": num_set[1], "cheese": num_set[2], "cheesy": num_set[3], "sourness": num_set[4], "sour": num_set[5], "harsh": num_set[6],
                             "astringent": num_set[7], "vinegar": num_set[8], "diaper": num_set[9], "gueuze": num_set[10], "lambic": num_set[11], "horse": num_set[12],
                             "brett": num_set[13], "wild": num_set[14], "hay": num_set[15], "stable": num_set[16], "lactic": num_set[17], "barnyard": num_set[18], "leather": num_set[19],
                             "tart": num_set[20], "phenolic": num_set[21]}

    acidity_antonyms_dict = {"moderate": num_set[22], "balanced": num_set[23], "mellow": num_set[24], "drinkable": num_set[25], "sweet":num_set[26], "sweetness":num_set[27], "caramel":num_set[28] }

    #18 being the point that is not sweet nor bitter
    wordcount = len(word_list)
    acidity_score = 0
    weighting = 13


    for word in word_list:
        if word in acidity_synonyms_list:
            acidity_score += acidity_synonyms_dict[word]
        elif word in acidity_antonyms_list:
            acidity_score -= acidity_antonyms_dict[word]

    #if these words occupy less than 10% of word list, beer is not acidic

    try:

        if (acidity_score*weighting/wordcount) * 100 < 5:
            return 0
        else:
            try:
                return round((acidity_score*weighting/wordcount) * 10,0)
            except ZeroDivisionError:
                return 0

    except ZeroDivisionError:
        return 0




trainAcidity()