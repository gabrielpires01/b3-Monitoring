# Project to Keep Track of your Actives
Create Pipelines ot receive email When active reach the top or bottom values

## How to inicialize

### BackEnd
Setting your gmail to receive notifications of your actives

first:
  set EMAIL_HOST_USER in b3_monitoring/settings.py to be the email you would like to receive
  and EMAIL_HOST_PASSWORD in the same file to be the passaword or key of the app
  [Simple tutorial to settup the host user and password](https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab)

first create an enviroment, <br/>
then:
```
  $ pip install -r requirements.txt
```
then
```
  $ python manage.py makemigrations
  $ python manage.py migrate
  $ python manage.py runserver
```

### FrontEnd

```
  $ cd frontend
  $ npm i
  $ npm start
```
