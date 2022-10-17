# django-rest-framework
 
### Hello everybody, let's jump in the tutorial!

#### Follow the steps:
* You need to clone the project into your desktop through the command. -> `git clone + https://github.com/FreeSoulsDotBat/django-rest-framework.git`;
* Open your terminal and prepare your virtual environment by creating one in the root of the project! -> `python -m venv venv`;
* Now that you have a virtual environment, you need to activate it -> `./venv/Scripts/activate`
* Install the requirements inside your venv with pip -> `pip install -r requirements.txt`
* And run the project by entering in the first directory -> `python manage.py runserver` (You don't need to make any migration or makemigration command because I'm sending this all done to you)


#### After the successfully run of the project, you need to have in mind:

The urls of the project are:
* '/api' -> The API itself (the first page has the url of all endpoints, remembering that you only can make requests if you are authenticated) 
* '/admin' -> The Admin dashboard (you need to login with the following credentials, **username: adminigs**, **password: igstest2022**, you may not need the email, but here it is: admin@igs.com)
* '/' -> The one view only app showing all employees registered


#### Last concerns:

* As the project shouldn't go to production, the secret key stays there, but the good practice is to trust only in environment variables (with .env for example)
