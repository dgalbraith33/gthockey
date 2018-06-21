# Georgia Tech Hockey Website

[![Build Status](https://travis-ci.org/dgalbraith33/gthockey.svg?branch=master)](https://travis-ci.org/dgalbraith33/gthockey)

This repository holds the code for the Georgia Tech club hockey website that can be found [here](https://www.gthockey.com).

## Client-Server Architecture

The client side implementation for the browser and the server side implementation for the API are
completely independent. They could be decoupled into seperate repositories and even run/served by
seperate machines if necessary.

### Client

The client code is contained in the `client/` directory and is written using Angular and Typescript.
Once loaded, the entire website is available without page reloads and simply loads data by making
API calls to the server.

### Server

The server is written in Django/Python. Configuration is in `gtsite/` and business logic is in
`gthockey/`. The server leverages DjangoRestFramework to send serialize model objects into JSON
for API call responses.

## Setting up a Development Environment

### Setting up the client

The first step is to install `node` from LINK.

Once node is installed the next step is to install dependencies and build the client.
```
$ cd client/
$ npm install
$ ng build
```

If the above steps complete without error, you can have angular (ng) serve the client at
`localhost:4200` with the following command:
```
$ ng serve
```

### Setting up the server

Make sure you have python 3 downloaded and installed. Then create a virtual environment and
install all of the necessary dependencies.

```
virtualenv --python=python3 virtenv
source virtenv/bin/activate
pip install -r requirements.txt
```

If this step completes successfully you should be able to run the test server

```
./manage.py runserver --settings=gtsite.env.dev
```