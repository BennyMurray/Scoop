import os
from CompileBeerList import compileBeerList


#POPULATE DATABASE WITH BEER OBJECTS
#-----------------------------------#


def populate():

    #Scrape beers form the internet and analyses reviews to generate values for strength, bitterness, colour and acidity .
    beer_List = compileBeerList()

    print ('populating Database...')
    print ('______________________\n')

    #Creates a superuser to access the MVC admin
    username = "user"
    email = "user@scoop.com"
    password = "password!!"

    #Creates a data base object if it does not exist
    counter = 1
    for list in beer_List:
        if list[1] == None:
            list[1] = list[0] + "Not Found: " + str(counter)
        add_Beer(list[1], list[0],list[2],list[3], list[4],list[5], list[6], counter)
        counter += 1



#ADD BEER FUNCTION
#----------------#

def add_Beer(beerID, beer_name, ABV, SRM, IBU, acidity, image_link, sequence_added):
    b, created = CraftBeer.objects.get_or_create(beerID=beerID, beer_name=beer_name, ABV=ABV, SRM=SRM, IBU=IBU, acidity=acidity, image_link=image_link, sequence_added=sequence_added)
    print ("- CraftBeer: {0}, Created: {1}".format(str(b), str(created)))
    return b

	

#CREATE SUPER USER FUNCTION
#-------------------------#

def create_super_user(username, email, password):
    '''
    for some reason get_or_create didn't work with creating the
    SuperUser so here is a try/except, with an IntegrityError
    raised if the SuperUser already exists
    '''
    try:
        u = User.objects.create_superuser(username, email, password)
        return u
    except IntegrityError:
        pass


#ALLOWS USE OF MVC MODELS EXTERNALLY
#-----------------------------------#

if __name__ == '__main__':
    print '\n' + ('=' * 80) + '\n'
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'ScoopProject.settings')
    django.setup()
    from ScoopApp.models import CraftBeer
    from django.contrib.auth.models import User
    from django.db import IntegrityError
    populate()  # Call the populate function, which calls the
                # add_genre and add_musician functions



