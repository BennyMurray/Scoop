import os
from mainThread import compileBeerList
from geolocator import getGeoLocation


# get_or_create method checks if entry exists and, if not, creates it.

def update():


    print ('getting Geolocations...')
    print ('______________________\n')

    username = "user"
    email = "user@scoop.com"
    password = "password!!"


    location_list = []
    for i in range(Visitor.objects.count()):
        visitor_object = Visitor.objects.get(visitor_number=i + 1)
        ip_address = visitor_object.ip_address
        geolocation = getGeoLocation(ip_address)
        location_list.append(str(geolocation))
        print "done"
    print location_list
        # visitor_object.geolocation = "poo"
        # visitor_object.save()




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
    from ScoopApp.models import Visitor
    from django.contrib.auth.models import User
    from django.db import IntegrityError

    update()  # Call the populate function, which calls the
    # add_genre and add_musician functions



