# eMenu

Restaurant menu system made for reqruitment purposes

### Prerequisites

Virtual environment with Python 3.6+

 
### Installing

* Clone repository
* Install needed libraries
``` 
pip install -r requirements.txt 
```
* In order to access admin panel:
``` 
python manage.py createsuperuser 
```

* Initial data:
``` 
./manage.py loaddata db.json
```

* Run development server:
``` 
python manage.py runserver 
```




## Running the tests

```
./manage.py test
```

## Built With

* Django
* Django rest framework
* Bootstrap 4
* Jquery 3
* Datatables 


## Authors

* **Łukasz Durejko**