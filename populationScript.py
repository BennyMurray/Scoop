import os
from mainThread import compileBeerList


#get_or_create method checks if entry exists and, if not, creates it. 

def populate():

    beerList = compileBeerList()

    print ('populating Database...')
    print ('______________________\n')

    username = "user"
    email = "user@scoop.com"
    password = "password!!"



    for list in beerList:
        add_Beer("5", list[0],list[2],list[3], list[4],list[5], list[6])




    

    #create_super_user(username, email, password)



def add_Beer(beerID, beer_name, ABV, SRM, IBU, acidity, image_link):
    b, created = CraftBeer.objects.get_or_create(beerID=beerID, beer_name=beer_name, ABV=ABV, SRM=SRM, IBU=IBU, acidity=acidity, image_link=image_link)
    print ("- CraftBeer: {0}, Created: {1}".format(str(b), str(created)))
    return b

	


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



