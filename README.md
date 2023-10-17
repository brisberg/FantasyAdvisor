# FantasyAdvisor
Web Application to make recommendations and manage your Yahoo Sports Fantasy Team

*Archived Oct 2023*: Unlikely to keep workin on this project in its current form.

## Virtualenv Management

Need to create a local virtualenv called `faenv`

Navigate to `server` directory
`add2virtualenv fantasyadvisor`
This will add the project directory to the PYTHONPATH, so we can import django
apps that are inside the project directory.

## Install Dependencies

`pip install -r requirements.text`

## Run Django server

`python server/manage.py runserver`

or

```cd server
gunicorn --bind 0.0.0.0:8000 fantasyadvisor.wsgi```
