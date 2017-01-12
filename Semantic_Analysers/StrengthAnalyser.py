from __future__ import division

def analyseStrength(word_list, published_abv):

   num_set = [0.19, 1.34, 1.83, 1.55, 1.38, 2.67, 1.33, 0.39, 2.55, 0.69, 1.64, 1.13, 1.29, 1.93, 2.8, 0.36, 1.54,
              2.11, 0.12, 2.67, 0.39, 2.37, 0.39, 2.36, 2.59, 1.17, 0.47, 0.6, 0.33, 0.67, 0.46, 1.67, 2.92, 0.63,
              0.75]

   alcohol_synonyms_list = ["strong", "hot", "fusel", "alcohols", "alcoholic", "fusels", "astringent", "booze",
                            "boozey", "boozy", "warm", "warming", "warmth", "port", "wine", "winey", "rum", "sharp",
                            "heavy", "champagne", "brandy", "whiskey", "esters", "rocket", "gasoline", "petrol",
                            "ethanol", "methanol"]

   alcohol_synonyms_dict = {"strong": num_set[0], "hot": num_set[1], "fusel": num_set[2], "alcohols": num_set[3],
                            "alcoholic": num_set[4], "fusels": num_set[5],
                            "astringent": num_set[6], "booze": num_set[7], "boozey": num_set[8],
                            "boozy": num_set[9], "warm": num_set[10], "warming": num_set[11], "warmth": num_set[12],
                            "port": num_set[13], "wine": num_set[14], "winey": num_set[15], "rum": num_set[16],
                            "sharp": num_set[17], "heavy": num_set[18], "champagne": num_set[19],
                            "brandy": num_set[20], "whiskey": num_set[21], "esters": num_set[22],
                            "rocket": num_set[23], "gasoline": num_set[24], "petrol": num_set[25],
                            "ethanol": num_set[26], "methanol": num_set[27]}

   alcohol_antonyms_list = ["delicate", "refreshing", "mild", "hidden", "drinkable", "balanced", "clean"]

   alcohol_antonyms_dict = {"delicate": num_set[28], "refreshing": num_set[29], "mild": num_set[30],
                            "hidden": num_set[31], "drinkable": num_set[32], "balanced": num_set[33],
                            "clean": num_set[34]}

   # 18 being the point that is not sweet nor bitter

   alcohol_score = 0

   for word in word_list:
       if word in alcohol_synonyms_list:
           alcohol_score += alcohol_synonyms_dict[word]
       elif word in alcohol_antonyms_list:
           alcohol_score -= alcohol_antonyms_dict[word]
   try:
       return round(float(published_abv) + (alcohol_score / 100), 1)
   except TypeError:
       print "Type Error"
       return 0






