from __future__ import division
import random
import pickle

def colourTrainer():

    srm3 = pickle.load(open("srm3beer.p", "rb"))
    srm8 = pickle.load(open("srm8beer.p", "rb"))
    srm16 = pickle.load(open("srm16beer.p", "rb"))
    srm26 = pickle.load(open("srm2126beer.p", "rb"))
    srm37 = pickle.load(open("srm3740beer.p", "rb"))

    while True:
        number_set = [round(random.uniform(0.1, 3), 2) for x in range(12)]

        if analyseColour(srm3, number_set) == 4 and analyseColour(srm8, number_set) == 8 and analyseColour(srm16, number_set) == 21 and abs(analyseColour(srm26, number_set)-23) <= 6 and abs(analyseColour(srm37, number_set) - 37) < 6:
            print "!!!!!!", number_set
        else:
            print analyseColour(srm3, number_set), analyseColour(srm8, number_set), analyseColour(srm16, number_set), analyseColour(srm26, number_set), analyseColour(srm37, number_set)

#Consists of Colour Value - Colour Descriptor - Colour Score (with weightings)



def analyseColour(word_list, num_set):

    colour_value_list = [
        (1, ["pale"], num_set[0]),
        (3, ["straw"], num_set[1]),
        (4, ["yellow"], num_set[2]),
        (5, ["gold"], num_set[3]),
        (8, ["amber"], num_set[4]),
        (12, ["red"], num_set[5]),
        (16, ["copper"], num_set[6]),
        (18, ["murky"], num_set[7]),
        (21, ["brown"], num_set[8]),
        (26, ["muddy"], num_set[9]),
        (32, ["black"], num_set[10]),
        (37, ["opaque"], num_set[11])
    ]

    colour_result_dict = {
        1: 0,
        3: 0,
        4: 0,
        5: 0,
        8: 0,
        12: 0,
        16: 0,
        18: 0,
        21: 0,
        26: 0,
        32: 0,
        37: 0
    }

    for word in word_list:
        for colour_value in colour_value_list:
            for descriptor_list in colour_value[1]:
                if word in descriptor_list:
                    colour_result_dict[colour_value[0]] += colour_value[2]

    sorted_dictionary = sorted(colour_result_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dictionary[0][0]


colourTrainer()