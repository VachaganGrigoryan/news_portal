# Simple News Portal
This is a Simple News Portal created by using [Django 3](https://docs.djangoproject.com/en/3.1/releases/3.0/).
The project was created per the [Task for Python Developer](task.txt) mail message.

## Requirements
##### Install [Python 3](https://www.python.org/downloads/) on your computer.
    Python >= 3.7
For more information from python packages look in the [requirements.txt](requirements.txt) file. 


## The installation steps
##### 1. Create [virtual environment](https://docs.python.org/3/tutorial/venv.html)
    virtualenv -p python3 venv
##### 2. Activate the python environment
    source venv/bin/activate
##### 3. Install python packages [requirements.txt](requirements.txt)
    pip install -r requirements.txt


## The Database setup and Django model migration
The default database config. (You can change the `sqlite3` to another DB. Look [here](https://docs.djangoproject.com/en/3.1/ref/databases/)) 
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Need to make run `makemigrations` and `migrate` commands before the running the Django server.
``` shell script
python manage.py makemigrations
python manage.py migrate
```
Create Super User using `python manage.py createsuperuser` command. 
```shell script
(venv) ~/Projects/news_portal >>> python manage.py createsuperuser                                                                                                                                             
Username (leave blank to use 'vachagan'): 
Email address: 
Password: 
Password (again): 
Superuser created successfully.
```

## Run the project 
Use the `python manage.py runserver` command and run the project on the local.
```shell script
(venv) ~/Projects/news_portal >>> python manage.py runserver                                                                                                                                                   
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 16, 2021 - 18:33:31
Django version 3.1.6, using settings 'news_portal.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```



      
