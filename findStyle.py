import pickle
import operator

#Import web-scraped beer dictionary
#beer_dict has following format: {STRENGTH - IMAGE_LINK - BITTERNESS - COLOUR - ACIDITY - RATEBEER_LINK_CODE}
#dict = pickle.load(open( "beerDictionary.p", "rb" ))


dict = {

        'Imperial_IPA': [9, 5, 60, 0],
        'Oude Geuze': [6, 5, 3, 8 ],
        'Belgian Blonde': [6, 5, 3, 0],
        'Imperial Stout': [12, 40, 22, 0],
        'Oatmeal Stout': [4, 35, 20, 0],
        'Session IPA': [3, 3, 50, 0],
        'Belgian Dark Ale': [13, 41, 21, 0]

    }


#Compares two beers
def compare(list1, list2):
    difference_one = abs(float(list1[0])-float(list2[0])) #strength
    difference_two = abs(float(list1[2])-float(list2[1])) #bitterness
    difference_three = (abs(float(list1[1])-float(list2[2])))#color
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
    total_difference = (difference_one * 6) + (difference_three * 4) + (difference_four) + (difference_two * 1.8)
    return total_difference


#Compares user-input (choice) to all beers in dictionary using compare function. Outputs result as dictionary.
def findStyle(choice):


    #compares and assigns difference as an float to each beer
    new_dict = {}
    counter = 0
    for i in dict:
        new_dict[i] = compare(choice, (dict[i])) + (counter * 0.05) #offsets values by a fraction to avoid duplicate key values
        counter += 1


    sorted_beers = sorted(new_dict.items(), key=operator.itemgetter(1))
    return sorted_beers[0][0]





