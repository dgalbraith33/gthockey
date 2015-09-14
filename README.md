# Georgia Tech Hockey Website

This repository holds the code for the Georgia Tech club hockey website that can be found at gthockey.com

Currently, it is in beta and not running in production.

## Installation

Here are the instructions for installing on ubuntu.

Install python 3 and the corresponding pip.

```sudo apt-get install python3 python3-pip```

Then install virtualenv and create a virtual environment in the project directory:

```sudo apt-get install virtualenv
cd gthockey/
virtualenv -p python3 virtenv
source virtenv/bin/activate```

Install the requirements with pip

```pip install -r requirements.txt```


At this point we should be able to migrate and run the server:

```./manage.py migrate
./manage.py runserver```
