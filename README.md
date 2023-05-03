# Installation :
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

# Description :
As a listing owner, I want a system for making and tracking reservations that can be handled by third-party services.

* The system can be used by multiple listings.
* The system provides REST API endpoints:
-> To make reservations
-> To check if a number of rooms are available at a certain time
* A reservation is for a name (any string) and for a certain amount of time
* The listing owner can get an overview over the booked rooms as an HTML or TEXT report (http://127.0.0.1:8000/rooms/booked_list)

# Swagger Url :
http://127.0.0.1:8000/swagger

# Admin Url :
http://127.0.0.1:8000/admin

# Note :
i deliberatly add sqlite3.db to have some mock data.