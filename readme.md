# Form Builder Service

## Clone From The Git Hub

First we get the code files from the Git Hub.

```bash
$ git clone https://github.com/syml30/form_builder.git
## Create And Activate Virtualenv

Create a virtual environment based on Python > 3.9\* and activate it.


$ virtualenv venv
$ source venv/bin/activate
```

## Install Requirements

```bash
$ mkdir -p form_builder_files
$ mkdir -p form_builder_uploads
$ pip install -r requirements.txt
$ cp env_example .env
```

## Migrate

```bash
$ python manage.py migrate
```

## Collect Static

```bash
$ python manage.py collectstatic
```

## Create Super User

```bash
$ python manage.py createsuperuser
```

## Run Server

```bash
$ python manage.py runserver 8000
```

## License

