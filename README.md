# Georgia Tech Hockey Website

This repository holds the code for the Georgia Tech club hockey website that can be found [here.](http://www.gthockey.com)

Currently, it is in beta and not running in production.

## Installation

Here are the instructions for installing on ubuntu.

Install python 3 and the corresponding pip.

```
sudo apt-get install python3 python3-pip python3-dev
```

Then install virtualenv and create a virtual environment in the project directory:

```
sudo apt-get install virtualenv
cd gthockey/
virtualenv -p python3 virtenv
source virtenv/bin/activate
```

Install the requirements with pip

```
pip install -r requirements.txt
```

Install the postgres dev library:
```
sudo apt-get install libpq-dev
```

and configure local_settings.py like so:

```
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '********',
            'USER': '********',
            'PASSWORD': '*********',
            'HOST': '******',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }

```

At this point we should be able to migrate and run the server:

```
./manage.py migrate
./manage.py runserver
```
