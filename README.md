# django-rest-framework
 
### Hello everybody, let's jump in the tutorial!

#### Follow the steps:
* You need to clone the project into your desktop through the command. -> `git clone + https://github.com/FreeSoulsDotBat/django-rest-framework.git`;
* Open your terminal and prepare your virtual environment by creating one in the root of the project! -> `cd django-rest-framework` and `python -m venv venv`;<br>
![image](https://user-images.githubusercontent.com/65923588/196241991-b1426edc-19d5-4526-8c27-230276f0cf52.png)

* Now that you have a virtual environment, you need to activate it -> `./venv/Scripts/activate`<br>
![image](https://user-images.githubusercontent.com/65923588/196242123-355a62c1-df97-41bf-9932-a66281ddcf8b.png)

* Install the requirements inside your venv with pip -> `pip install -r .\requirements.txt`<br>
![image](https://user-images.githubusercontent.com/65923588/196242407-e730607c-679d-4818-9579-7201c5b172ae.png)

* And run the project by entering in the first directory -> `cd .\igsSoftwareManager` and `python manage.py runserver` (You don't need to make any migration or makemigration command because I'm sending this all done to you)
![image](https://user-images.githubusercontent.com/65923588/196242631-f5fd6d44-b8d3-43b1-877d-a48a483cd53a.png)

You will see something like this in your browser:<br>
![image](https://user-images.githubusercontent.com/65923588/196242814-d0fbb660-708b-484f-9a07-fbde0258a516.png)



#### After the successfully run of the project, you need to have in mind:

The urls of the project are:
* '/api' -> The API itself (the first page has the url of all endpoints, remembering that you only can make requests if you are authenticated)<br>
![image](https://user-images.githubusercontent.com/65923588/196243093-ae19a5b9-2f1f-4eeb-b6c4-3598cb92e7a5.png)

* '/admin' -> The Admin dashboard (you need to login with the following credentials, **username: adminigs**, **password: igstest2022**, you may not need the email, but here it is: admin@igs.com)<br>
![image](https://user-images.githubusercontent.com/65923588/196243175-22f623f7-2e09-4f25-b563-0b23a2babdb7.png)
![image](https://user-images.githubusercontent.com/65923588/196243207-936aba14-703e-4c58-8841-73b2eaba2e60.png)

* '/' -> The one view only app showing all employees registered<br>
![image](https://user-images.githubusercontent.com/65923588/196243321-51108d7c-c0a8-4714-a5c8-09347858c440.png)



#### Last concerns:

* As the project shouldn't go to production, the secret key stays there, but the good practice is to trust only in environment variables (with .env for example);
* I maded the project using sqlite as it's a small project, for big project I recommend SQL.
