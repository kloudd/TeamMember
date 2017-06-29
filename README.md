"#TeamMember" 

1: Install restframework. "pip install djangorestframework"
2: install mysql client for python. "pip install mysqlclient"

Create a database named team in mysql server 
"create database team;"

provide information regarding database in settings.py file. 
run command "python manage.py makemigrations"
run command "python manage.py migrate

to run the application go to ./ folder in cmd and type "python manage.py"

Go to the webbrowser and go to link "http://127.0.0.1:8000/myTeamApp/teamMember/" - to see the details of the team member or to add team member

Go to the webbrowser and go to link "http://127.0.0.1:8000/MyTeamApp/teamMember/?format=json" - to see the JSON details of the team member

to edit destroy/delete go to link "http://127.0.0.1:8000/myTeamApp/teamMember/1" - whatever id you want to delete of edit