# Django Driver Tracking Map App
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#install">Install</a></li>
        <li><a href="#configuration">Configuration</a></li>
        <li><a href="#how-to-run">How To Run</a></li>
      </ul>
    </li>
  </ol>
</details>

## About The Project
This is a fullstack application for showing geographical information of entities on the map. First, a dummy data of 10 drivers are generated using factory boy. These data are then added to the database. A scheduled task updates the positions of each driver in a given range every 5 seconds and updates the database. Frontend fetches the data from django backend and shows the positions of each driver with different colored markers on the map. When the page is refreshed change of the positions can be observed. If you hover over to a driver on the map you can see additional information about the driver such as name, nationality, language, phone, licence plate, etc. as a tooltip.

### Built With
* [React](https://reactjs.org/) - A JavaScript library for creating single page apps.
* [Leaflet](https://leafletjs.com/) - An open-source JavaScript library for interactive maps.
* [Django](https://www.djangoproject.com/) - A web framework for python.
* [Redis](https://redis.io/) - Backend for running scheduled jobs
* [Postgresql](https://www.postgresql.org/) - Database.
* [Celery](https://docs.celeryproject.org/en/stable/index.html) - Distributed Task Queue.
* [PostGIS](https://postgis.net/) - Spatial and Geographic objects for PostgreSQL
* [FactoryBoy](https://factoryboy.readthedocs.io/en/stable/) - Test fixture creator/ dummy data generator.
### Project Structure Explained
  - manage.py is coming from django framework, resides in the main folder and used to setup the server.
  - All project settings are inside the "./django-driver-tracker/mapApp" folder.
  - mapApp is our django application which serves the backend. It has models, views, serializers for the database operations.
  - We populate dummy data and insert into the database. In "driverTracker/tests" folder we have    factories.py file which generates and saves the initial drivers data for us. In "How To Run" section we will explain how to generate fake initial data.
  - We have 2 frontends at the moment, one of them is in .django-driver-tracker/static folder and can be ignored. However, it also shows a map with markers and reachable at http://127.0.0.1:8000/driverTracker/map. I also implemented a more complex UI with React and React Hooks inside the .django-driver-tracker/frontend folder. And I would prefer using the latter one as a frontend application.
  - In mapApp/fixtures folder I stored an example information about drivers as a json file.
  - Scheduled tasks are implemented at "./driverTracker/mapApp/tasks.py". It gets drivers from the database and updates each driver's locations in every 5 seconds.
  - Frontend calls the backend with 'api/markers' and gets all drivers as a geojson object. Then shows them on the map. Each driver has a unique color and can be tracked easily. 
  - Drivers positions are randomly updated in a range of 100kms.
## Getting Started
In order to run this project some libraries should be installed and configured. I will explain to install the libraries and frameworks for Linux. But Mac users can use 'brew' instead of 'sudo apt-get'.

### Install
1) We need to install the GDAL (Geospatial Data Abstraction Library), PostGIS, Redis and Postgres
 ```sh
 sudo apt-get install gdal-bin
 sudo apt-get install libpq5
 sudo apt-get install postgresql
 sudo apt-get install postgresql-contrib
 sudo apt install redis-server
 ```

2) We need to install the python libraries.
 ```sh
python3 -m venv virtual-env
source virtual-env/bin/activate
pip3 install -r requirements.txt
 ```
 If you get errors when installing requirements (with pip3 install -r requirements.txt), 
 ```sh
  sudo apt-get install python-psycopg2
  sudo apt-get install libpq-dev
  pip3 install -r requirements.txt
```
3) We should create and activate a postgres database. It is created without password in this example. We can create the database using PgAdmin4 with GUI.
 ```sh
  sudo service postgresql start
   ```
We should add postGIS as an extension to our new database. (Check extensions in the database directory tree to add new extensions from dropdown list in PgAdmin4)
### Configuration
In projects driverTracker/settings.py file we configure the database locally.
```sh
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": <replaceWithDbName>,
        "PORT": 5432,
        "USER": <replaceWithUsername>,
        (if Password exits)
        "PASSWORD": <replaceWithPassword>,
    }
}
```
Now we should migrate the database,
```sh
cd ~/django-driver-tracker
python3 manage.py makemigrations
python3 manage.py migrate
```
Then we create super user for our django app. With this user credentials we can switch to admin panel in  http://localhost:8000/admin after running the server.
```sh
python3 manage.py createsuperuser
```
We should also run the redis-server in another terminal in the background.
```sh
redis-server
```
Finally, we switch to frontend and install packages.

   ```sh
   cd ~/django-driver-tracker/frontend
   npm install
   ```
### How To Run
1) Redis-server and Postgres should be up and running in the background.
2) In "/driverTracker/mapApp/management/commands", I created a custom django command as seed.py. It is used to populate the driver data using factories.py file from the command line. (default: 10 drivers). We can run this script;
   ```sh
    python3 manage.py seed
   ```
3) We should be in the driverTracker folder and run the celery command to start scheduled worker and tasks in different terminals (both runs in the background)
```sh
  celery -A django-driver-tracker worker 
  celery -A django-driver-tracker beat -S django 
 ```

4) Then, we run our django backend inside the django-driver-tracker;
```sh
  python3 manage.py runserver
 ```
 Now server should be running in http://127.0.0.1:8000/

 5) In another terminal we go to "django-driver-tracker/frontend" folder and start the front-end.
 ```sh 
  npm run start
 ```

 Front-end runs in http://127.0.0.1:3000/map-drivers
 Now, we should be able to see a map with 10 markers. The data is updated in the backend periodically. We can refresh the page and observe markers moving.

 ### If I Had More Time...
  - I would like to update my django model for Markers to get a history object to store all coordinates for each driver. Then I could draw a line on the map to show the distance they achieved from the start. (as driver locations are updated in every 5 seconds)
  - Functionality to register/delete drivers (rather than using the admin panel or sending http request to admin to add new data) and save them through the react frontend with another api endpoint.
  - I would like to use webpack and replace static files with webpack bundled static files to render the frontend inside the django application.
  - I would like to deploy the project on Heroku.
 