from __future__ import division

bitterness_synonyms_list = ["hoppy", "hop", "hops", "well-hopped", "hopped", "bitter", "bitterness", "piney", "tropical", "earthy", "cascade", "citra", "grassy", "lemon", "resin","grassy", "citrus", "crisp", "tangerine", "slick", "floral", "florals","oily", "pine","aroma", "well-hopped", "zesty", "refreshing", "passionfruit"]
bitterness_antonyms_list = ["drinkable", "balanced","malt", "malty", "maltiness", "sweet", "sweetness", "caramel", "yeast", "yeasty", "bready", "honey", "toasted", "rich", "crystal", "burnt", "full", "bodied", "hearthy", "sugar", "toffee", "wood", "biscuit", "biscuity", "malts", "butterscotch", "creamy","vanilla", "fig", "figs", "banana", "esters","grains", "toast", "toasty", "full-bodied", "syrup", "tea", "oats", "coffee", "chocolate", "cacao", "molasses", "sticky"]
bitterness_synonyms_dict = {"hoppy" : 5, "hop" : 4, "hops" : 4, "well-hopped" : 4, "hopped":4, "bitter":4, "bitterness":3, "piney":1, "tropical":2, "earthy":1, "cascade":3, "citra":3, "grassy":1, "lemon":1, "resin":1,"grassy":1, "citrus":1, "crisp":1, "tangerine":1, "slick":1, "floral":1, "florals":1,"oily":2, "pine":2,"aroma":1, "well-hopped":4, "zesty":2, "refreshing":1, "passionfruit":1}
bitterness_antonyms_dict = {"drinkable": 1, "balanced":1, "malt" : 0.5, "malty" : 1.5, "maltiness" : 1.5, "maltyness":1.5, "cloying":5, "sweet":5, "sweetness":5, "caramel":4,"yeast":2, "yeasty":2, "bready":3, "bread":3, "honey":2, "toasted":2, "rich":3, "crystal":2, "burnt": 5, "full":3, "bodied":5, "hearthy":3, "sugar":10, "toffee": 5, "wood":3, "biscuit":5, "biscuity":5, "malts":3, "butterscotch": 5, "creamy":5,"vanilla":3, "fig":5, "figs":5, "banana":5, "esters":3,"grains": 4, "sticky":2, "toast": 4, "toasty":4, "molasses":2, "full-bodied":5, "syrup":4, "tea":3, "oats":4, "coffee":5, "chocolate":4, "cacao":4, }


def analyseBitterness(word_list):

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


