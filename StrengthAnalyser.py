from __future__ import division

alcohol_synonyms_list = ["strong", "hot", "fusel", "alcohols", "alcoholic", "fusels", "astringent", "booze", "boozey", "boozy", "warm", "warming", "warmth","port", "wine", "winey", "rum", "sharp", "heavy", "champagne", "brandy", "whiskey", "esters", "rocket", "gasoline", "petrol", "ethanol", "methanol"]
alcohol_synonyms_dict = {"strong":0.5, "hot":2, "fusel":4, "alcohols":4, "alcoholic":1, "fusels":4, "astringent":4, "booze":2, "boozey":4, "boozy":4, "warm":2, "warming":2, "warmth":2,"port":2, "wine":2, "winey":3, "rum":3, "sharp":2, "heavy":1, "champagne":2, "brandy":2, "whiskey":2, "esters":2, "rocket":2, "gasoline":5, "petrol":5, "ethanol":4, "methanol":6}

alcohol_antonyms_list = ["delicate", "refreshing", "mild", "hidden", "drinkable", "balanced", "clean"]
alcohol_antonyms_dict = {"delicate":5, "refreshing":10, "mild":4, "hidden":4, "drinkable":15, "balanced":6, "clean":6}

def analyseStrength(word_list, published_abv):

    #18 being the point that is not sweet nor bitter

    alcohol_score = 0


    for word in word_list:
        if word in alcohol_synonyms_list:
            alcohol_score += alcohol_synonyms_dict[word]
        elif word in alcohol_antonyms_list:
            alcohol_score -= alcohol_antonyms_dict[word]
    try:
        return round(float(published_abv) + (alcohol_score/100),1)
    except TypeError:
        print "Type Error"
        return 0





