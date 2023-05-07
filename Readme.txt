Registration URL using Djoser:
http://localhost:8000/auth/users

Get a JWT access token:
http://localhost:8000/api/token

Note: access token valid for only 60 minutes

Copy the access token and open Postman or Insomnia:
1- select GET method
2- write in URL field: http://localhost:8000/api/menu
3- click on Authorization tab, and select `Bearer Token`
4- copy your access token inside, and press send

Now you are authorized to browse all of the URLs