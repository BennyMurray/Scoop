from __future__ import division





def analyseColour(word_list):


    num_set = [0.33, 1.68, 2.2, 2.36, 2.87, 0.29, 0.27, 2.94, 0.81, 0.22, 2.59, 1.06]


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
