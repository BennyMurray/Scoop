
import operator

dict = {

        'Imperial_IPA': [9, 5, 60, 0],
        'Oude Geuze': [6, 5, 3, 8 ],
        'Belgian Blonde': [6, 5, 3, 0],
        'Russian Imperial Stout': [12, 40, 22, 0],
        'Oatmeal Stout': [4, 35, 20, 0],
        'Session IPA': [3, 3, 50, 0],
        'Belgian Dark Ale': [12, 21, 21, 0],
        'Irish Stout': [4, 40, 21, 0],
        'Belgian Triple': [9, 4, 14, 0],
        'Oude Bruin': [6, 16, 4, 7],
        'Flanders Red Ale': [7, 14, 3, 6],
        'Belgian Wit': [6, 8, 12, 0],
        'American Pale Ale': [5, 5, 42, 0],
        'Chocolate Milk Stout': [4, 28, 12, 0],
        'Saison': [40, 5, 34, 1],
        'Biere de Guarde': [7, 7, 22, 0],
        'English Brown Ale': [4, 14, 24, 0],
        'Scotch Ale': [3, 14, 8, 0],
        'English Barley Wine': [12, 18, 14, 0],
        'American Lager': [4, 2, 11, 0],
        'Berliner Weiss': [1, 4, 5, 2],
        'DunkelWeizen': [8, 18, 11, 0],
        'German Doppelboch': [8, 16, 13, 0],
        'Hefeweizen': [5, 4, 11, 0],
        'Czech Pilsner': [4, 2 , 22, 0],
        'English Bitter': [3, 7, 42, 0],
        'Robust Stout': [6, 34 , 36, 0],
        'Extra Special Bitter': [5, 8, 46, 0],

    }


#Compares two beers
def compare(list1, list2):
    difference_one = abs(float(list1[0])-float(list2[0])) #strength
    difference_two = abs(float(list1[1])-float(list2[2])) #bitterness
    difference_three = (abs(float(list1[2])-float(list2[1])))#color
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
    total_difference = (difference_one*6) + (difference_three * 2.5) + (difference_four*10) + (difference_two * 1.5)
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





