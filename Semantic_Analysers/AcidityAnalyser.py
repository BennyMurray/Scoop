from __future__ import division



def analyseAcidity(word_list):


    num_set = [4.08, 0.71, 10.43, 11.05, 12.23, 12.62, 11.42, 3.1, 5.87, 2.46, 1.12, 0.82, 3.16, 1.2, 1.47, 14.7, 11.84, 6.2,
         6.72, 6.81, 4.59, 13.81, 6.69, 9.31, 7.69, 5.69, 2.5, 3.11, 2.16]

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

