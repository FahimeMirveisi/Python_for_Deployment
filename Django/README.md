
# 📊 Polls app with django

with help of django documentation, we`ll walk through the creation of a basic poll application.

It consist of two parts:
* A public site that lets people view polls and vote in them.
* An admin site that lets you add, change and delete polls. 


## ✈️ Getting Started

these instructions will help you set up and run the project on your local machine.
## Prerequisites
<code>python== 3.5 or up and django==2.0 or up</code>

## Installation

```
pip install django
```
## Creating a project

```
mkdir djangotutorial
django-admin startproject mysite djangotutorial
```

## The development server
```
python manage.py runserver
```

Now that the server’s running, visit http://127.0.0.1:8000/ with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!