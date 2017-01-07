from __future__ import division






def analyseBitterness(word_list):




    number_set = [2.22, 5.17, 4.13, 6.41, 2.46, 5.51, 7.81, 8.11, 0.94, 4.44, 6.83, 9.58, 6.5, 6.51, 8.52, 3.11, 4.8,
                  4.0, 0.53, 5.73, 7.26, 0.69, 2.85, 0.3, 5.72, 3.0, 6.87, 4.17, 8.43, 4.62, 1.18, 4.01, 9.08, 9.29,
                  3.93, 6.88, 1.94, 4.59, 9.71, 1.2, 7.01, 3.36, 5.06, 3.22, 6.25, 6.53, 0.53, 2.35, 5.46, 3.13, 9.88,
                  0.72, 1.73, 8.59, 6.31, 1.95, 2.69, 2.63, 1.53, 7.14, 7.48, 5.59, 4.23, 1.63, 1.8, 8.48, 5.35, 8.98,
                  4.91, 5.57, 7.0, 8.34, 8.19, 1.49, 6.77, 7.0, 9.9]

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
    sweet_score = sweet_score * 0.68

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