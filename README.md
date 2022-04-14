# MFI Test - Mountain Peaks

PREREQUISITES: To have docker installed on your computer

This project is about a map displaying some mountain peaks on given coordinates.

## Features
- You can add new mountain peak by clicking on the __add data__ button
- You can update a mountain peak by clicking on the __point__ in the map

## To easily run your project

First you have to clone this repository on your computer by typing

```
git clone https://github.com/Fantemis/mfi_test.git
```

Then move on this folder:
```
cd mfi_test
```

Next step is to move on the folder named: __back__ .

```
cd back/restApiMountainPeaks
```

You'll now find a file named: __docker-compose.yml

This file allows you to get the entire project environment, including:
- postgresql database
- django rest api
- react web app (with 3D globe)

Then you'll have to type this commands:

```
docker-compose run web python manage.py makemigrations
```

Then

```
docker-compose run web python manage.py migrate
```

And then you can finish by:

```
docker-compose up --build
```

This flag is to build your environment, to download all dependencies etc.

I am personally using docker desktop on windows10.
So when your containers are built, you can find them on the docker desktop interface or by typing

```
docker container ls
```

You'll find 3 containers:
- react_web_app
- psql_db
- django_rest_api

You can now navigate on your applications
- __localhost:3000__ for the react web app
- __localhost:8000/mountain_peak__ for the django api (with default user web interface)

Note that you have differents api routes availables
- CREATE: __localhost:8000/mountain_peak/create/__  : Allows you to create your own mountain peak
- READ: __localhost:8000/mountain_peak__ : Its the default route, it will give you all mountain peaks
- UPDATE: __localhost:8000/mountain_peak/update/particular-id__: To update particular mountain peak
- DELETE: __localhost:8000/mountain_peak/delete/particular-id__: To delete particular mountain peak
