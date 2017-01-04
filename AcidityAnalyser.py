from __future__ import division

acidity_synonyms_list = ["funk", "funky", "cheese", "cheesy", "sourness","sour", "harsh", "astringent", "vinegar", "diaper", "gueuze", "lambic", "horse", "brett", "wild","hay", "stable", "lactic", "barnyard", "leather", "tart", "phenolic" ]
acidity_antonyms_list = ["moderate", "balanced", "mellow", "drinkable"]

acidity_synonyms_dict = {"funk":2, "funky":2, "cheese":1, "cheesy":2, "sourness":2,"sour":2, "harsh":1, "astringent":3, "vinegar":6, "diaper":4, "gueuze":2, "lambic":2, "horse":2, "brett":3, "wild":3,"hay":3, "stable":3, "lactic":2, "barnyard":3, "leather":3, "tart":1, "phenolic":1}
acidity_antonyms_dict = {"moderate":2, "balanced":2, "mellow":2, "drinkable":2}


def analyseAcidity(word_list):

    #18 being the point that is not sweet nor bitter
    wordcount = len(word_list)
    acidity_score = 0
    weighting = 4


    for word in word_list:
        if word in acidity_synonyms_list:
            acidity_score += acidity_synonyms_dict[word]
        elif word in acidity_antonyms_list:
            acidity_score -= acidity_antonyms_dict[word]

    #if these words occupy less than 10% of word list, beer is not acidic

    try:

        if (acidity_score*weighting/wordcount) * 100 < 10:
            return 0
        else:
            try:
                return round((acidity_score*weighting/wordcount) * 10,0)
            except ZeroDivisionError:
                return 0

    except ZeroDivisionError:
        return 0




