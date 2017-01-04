from __future__ import division

#colour = ["clear", "amber", "hazy", "orange", "hazy", "black", "brown", "golden", "copper", "straw" ]

#Consists of Colour Value - Colour Descriptor - Colour Score (with weightings)
colour_value_list = [
    (1, ["pale"], 1),
    (3, ["straw"], 1),
    (4, ["yellow"], 1),
    (5, ["gold"], 1),
    (8, ["amber"], 1),
    (12, ["red"], 1),
    (16, ["copper"], 1),
    (18, ["murky"], 3),
    (21, ["brown"], 0.4),
    (26, ["muddy"], 4),
    (32, ["black"], 0.4),
    (37, ["opaque"], 3)
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


def analyseColour(word_list):

    for word in word_list:
        for colour_value in colour_value_list:
            for descriptor_list in colour_value[1]:
                if word in descriptor_list:
                    colour_result_dict[colour_value[0]] += colour_value[2]

    sorted_dictionary = sorted(colour_result_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dictionary[0][0]


