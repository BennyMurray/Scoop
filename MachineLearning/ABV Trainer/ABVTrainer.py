from __future__ import division
import pickle
import random

def trainABV():

    abv_3_8 = pickle.load(open("3_8abv.p", "rb"))
    abv_5_6 = pickle.load(open("5_6abv.p", "rb"))
    abv_8_5 = pickle.load(open("8_5abv.p", "rb"))
    abv_10_5 = pickle.load(open("10_5abv.p", "rb"))
    abv_7_4 = pickle.load(open("7_4abv.p", "rb"))


    while True:
        number_set = [round(random.uniform(0.1, 3), 2) for x in range(35)]

        result_a = abs(analyseStrength(abv_3_8, 3.8, number_set) - 3.8)
        result_b = abs(analyseStrength(abv_5_6, 5.6, number_set) - 5.6)
        result_c = abs(analyseStrength(abv_8_5, 8.5, number_set) - 7)
        result_d =abs(analyseStrength(abv_10_5, 10.5, number_set) - 11.5)
        result_e = abs(analyseStrength(abv_7_4, 7.4, number_set) - 9)
        
        if result_a < 1.5 and result_b < 1.5 and result_c < 1.5 and result_d < 1.5 and result_e < 1.5:
            print 'Determined Accurate Number Set: ', number_set
            break
        else:
            print result_a, result_b, result_c , result_d, result_e


def analyseStrength(word_list, published_abv, num_set):

    alcohol_synonyms_list = ["strong", "hot", "fusel", "alcohols", "alcoholic", "fusels", "astringent", "booze",
                             "boozey", "boozy", "warm", "warming", "warmth", "port", "wine", "winey", "rum", "sharp",
                             "heavy", "champagne", "brandy", "whiskey", "esters", "rocket", "gasoline", "petrol",
                             "ethanol", "methanol"]

    alcohol_synonyms_dict = {"strong": num_set[0], "hot": num_set[1], "fusel": num_set[2], "alcohols": num_set[3], "alcoholic": num_set[4], "fusels": num_set[5],
                             "astringent": num_set[6], "booze": num_set[7], "boozey": num_set[8], "boozy": num_set[9], "warm": num_set[10], "warming": num_set[11], "warmth": num_set[12],
                             "port": num_set[13], "wine": num_set[14], "winey": num_set[15], "rum": num_set[16], "sharp": num_set[17], "heavy": num_set[18], "champagne": num_set[19],
                             "brandy": num_set[20], "whiskey": num_set[21], "esters": num_set[22], "rocket": num_set[23], "gasoline": num_set[24], "petrol": num_set[25],
                             "ethanol": num_set[26], "methanol": num_set[27]}

    alcohol_antonyms_list = ["delicate", "refreshing", "mild", "hidden", "drinkable", "balanced", "clean"]

    alcohol_antonyms_dict = {"delicate": num_set[28], "refreshing": num_set[29], "mild": num_set[30], "hidden": num_set[31], "drinkable": num_set[32], "balanced": num_set[33],
                             "clean": num_set[34]}

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





trainABV()