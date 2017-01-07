

#FIX BEER SCRAPER ITS USING ID!

def analyseBitterness(word_list, number_set):

    bitterness_synonyms_list = ["hoppy", "hop", "hops", "well-hopped", "hopped", "bitter", "bitterness", "piney",
                                "tropical", "earthy", "cascade", "citra", "grassy", "lemon", "resin", "grassy",
                                "citrus", "crisp", "tangerine", "slick", "floral", "florals", "oily", "pine", "aroma",
                                "well-hopped", "zesty", "refreshing", "passionfruit"]

    bitterness_antonyms_list = ["drinkable", "balanced", "malt", "malty", "maltiness", "sweet", "sweetness", "caramel",
                                "yeast", "yeasty", "bready", "honey", "toasted", "rich", "crystal", "burnt", "full",
                                "bodied", "hearthy", "sugar", "toffee", "wood", "biscuit", "biscuity", "malts",
                                "butterscotch", "creamy", "vanilla", "fig", "figs", "banana", "esters", "grains",
                                "toast", "toasty", "full-bodied", "syrup", "tea", "oats", "coffee", "chocolate",
                                "cacao", "molasses", "sticky"]

    bitterness_synonyms_dict = {"hoppy": number_set[0], "hop": number_set[1], "hops": number_set[3],
                                "well-hopped": number_set[4], "hopped": number_set[5], "bitter": number_set[6],
                                "bitterness": number_set[7], "piney": number_set[8], "tropical": number_set[9],
                                "earthy": number_set[10], "cascade": number_set[11], "citra": number_set[12],
                                "grassy": number_set[13], "lemon": number_set[14], "resin": number_set[15],
                                "grassy": number_set[16], "citrus": number_set[17], "crisp": number_set[18],
                                "tangerine": number_set[19], "slick": number_set[20], "floral": number_set[21],
                                "florals": number_set[22], "oily": number_set[23], "pine": number_set[24],
                                "aroma": number_set[25],
                                "well-hopped": number_set[26], "zesty": number_set[27], "refreshing": number_set[28],
                                "passionfruit": number_set[29]}

    bitterness_antonyms_dict = {"drinkable": number_set[30], "balanced": number_set[31], "malt": number_set[32],
                                "malty": number_set[33], "maltiness": number_set[34],
                                "maltyness": number_set[35], "cloying": number_set[36], "sweet": number_set[37],
                                "sweetness": number_set[38], "caramel": number_set[39], "yeast": number_set[40],
                                "yeasty": number_set[46], "bready": number_set[47], "bread": number_set[48],
                                "honey": number_set[49], "toasted": number_set[50], "rich": number_set[51],
                                "crystal": number_set[52],
                                "burnt": number_set[0], "full": number_set[53], "bodied": number_set[54],
                                "hearthy": number_set[55], "sugar": number_set[56], "toffee": number_set[57],
                                "wood": number_set[58],
                                "biscuit": number_set[0], "biscuity": number_set[59], "malts": number_set[60],
                                "butterscotch": number_set[61], "creamy": number_set[62], "vanilla": number_set[63],
                                "fig": number_set[0], "figs": number_set[64], "banana": number_set[65],
                                "esters": number_set[66], "grains": number_set[67], "sticky": number_set[68],
                                "toast": number_set[69],
                                "toasty": number_set[0], "molasses": number_set[70], "full-bodied": number_set[71],
                                "syrup": number_set[72], "tea": number_set[73], "oats": number_set[74],
                                "coffee": number_set[0], "chocolate": number_set[75], "cacao": number_set[76], }

    #18 being the point that is not sweet nor bitter
    final_score = 18
    hop_score = 0.0
    sweet_score = 0.0

    for word in word_list:
        if word in bitterness_synonyms_list:
            hop_score += bitterness_synonyms_dict[word]
        elif word in bitterness_antonyms_list:
            sweet_score += bitterness_antonyms_dict[word]

    #weighting
    sweet_score = sweet_score * 0.64

    if sweet_score > hop_score:

        try:

            bitterness = final_score - round(((sweet_score/hop_score) * 10), 0)
            if bitterness < 0:
                return 7
            else:
                return bitterness
        except ZeroDivisionError:
            return 0

    else:
        try:
            bitterness = final_score + round(((hop_score/sweet_score) * 10), 0)
            if bitterness > 100:
                return 100
            else:
                return bitterness
        except ZeroDivisionError:
            return 100


import pickle


wordlist = pickle.load(open("10ibubeer.p", "rb"))
#number_set = [0.63, 0.71, 9.3, 0.89, 4.54, 7.09, 4.67, 5.77, 7.97, 0.58, 2.51, 5.81, 9.49, 6.43, 5.02, 5.07, 1.04, 3.24, 9.83, 2.92, 0.73, 8.83, 3.01, 1.42, 2.16, 5.62, 9.07, 4.67, 4.94, 2.96, 3.39, 9.45, 2.52, 3.32, 2.07, 8.09, 4.15, 2.48, 2.78, 7.49, 6.61, 5.66, 5.34, 1.99, 9.59, 1.24, 3.07, 4.6, 3.29, 1.41, 4.26, 7.28, 2.82, 8.56, 8.99, 9.06, 3.61, 3.64, 6.03, 7.13, 0.81, 9.67, 0.35, 6.24, 4.47, 8.56, 5.76, 8.31, 0.23, 5.2, 9.73, 2.53, 4.4, 6.53, 0.2, 0.2, 8.69]
number_set = [3.1, 9.14, 3.73, 0.63, 1.84, 5.36, 7.85, 8.75, 9.3, 2.25, 5.05, 4.15, 6.71, 8.37, 0.11, 1.31, 6.24, 1.63, 1.36, 0.27, 1.24, 0.4, 6.64, 0.17, 2.69, 7.98, 0.71, 0.65, 9.49, 3.58, 0.88, 0.37, 7.34, 9.96, 2.69, 6.65, 9.18, 4.96, 8.44, 8.14, 4.46, 2.62, 2.57, 7.34, 1.34, 8.4, 9.91, 2.99, 8.46, 6.98, 6.32, 1.53, 6.5, 7.5, 5.18, 4.25, 5.9, 6.01, 6.06, 6.74, 6.61, 9.15, 0.56, 4.29, 7.63, 4.72, 5.98, 0.69, 7.92, 4.48, 6.47, 3.22, 0.7, 2.7, 2.06, 2.83, 4.21]
print analyseBitterness(wordlist, number_set)
