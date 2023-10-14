Katrina McKenna
Coursera Meta Backend Capstone
-------
MySQL Database
'ENGINE': 'django.db.backends.mysql',
'NAME': 'reservations',
'USER' : 'root',
'PASSWORD' : 'root@123'

Load Data
python manage.py loaddata Category.json
python manage.py loaddata MenuItem.json

Create 3 groups
Groups
Groups
    Customer
        Can add booking

    Employee
        Can add/change/view menu items
        Can add/change/view categories
        Can view bookings

    Manager
        Can add/change/view/delete menu items
        Can add/change/view/delete categories
        Can add/change/view/delete bookings

Unauthenticated
    Can view menu items
    Can view categories

http://127.0.0.1:8000
    /api/menuitems/
    /api/bookings/

    /api/users/
    /api/groups/