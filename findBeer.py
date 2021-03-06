
import operator

#Compares two beers
def compare(list1, list2):
    difference_one = abs(float(list1[0])-float(list2[0])) #strength
    difference_two = abs(float(list1[1])-float(list2[2])) #bitterness
    difference_three = abs(float(list1[2])-float(list2[1])) #color
    difference_four = abs(float(list1[3])-float(list2[3])) #acidity/funk

    #Eliminates inactive sliders

    if float(list1[0]) == 0:
        difference_one = 0

    if float(list1[1]) == 0:
        difference_two = 0

    if float(list1[2]) == 0:
        difference_three = 0

    if float(list1[3]) == 0:
        difference_four = 0

    #Applies weightings and calculates total difference
    total_difference = (difference_one * 6) + (difference_three * 2.5) + (difference_four * 10) + (difference_two * 1.8)
    return total_difference


#Compares user-input (choice) to all beers in dictionary using compare function. Outputs result as dictionary.
def find_beer(choice, dict):


    #compares and assigns difference as an float to each beer
    new_dict = {}
    counter = 0
    for i in dict:
        new_dict[i] = compare(choice, (dict[i])) + (counter * 0.05) #offsets values by a fraction to avoid duplicate key values
        counter += 1


    #Sorts by least different
    sorted_beers = sorted(new_dict.items(), key=operator.itemgetter(1))


    #creates dict for json export
    result_dict = {}
    dict_names = ["first","second","third","fourth","fifth","sixth", "seventh","eighth","ninth","tenth","eleventh","twelfth"]

    for i in range(12):
        beer_value_list = dict[sorted_beers[i][0]]
        result_dict[dict_names[i]] = {"name": sorted_beers[i][0], "ABV" : beer_value_list[0], "IBU": beer_value_list[1], "SRM" : beer_value_list[2], "acidity" : beer_value_list[3], "image_link": beer_value_list[4]}

    return result_dict




