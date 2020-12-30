# todo-list-rest-api
A rest api for todo list developed in django rest frameework.

api-endpoints:-
1. auth
  > post: api/auth/user/register/  ( register new user )
    data = {"username":"","password":""}
  > post: api/auth/user/login/     ( login user )
    data = {"username":"","password":""}
    response = {"token":"a token"}

headers = {"Authorization":"Token token-obtained-after-login}
add headers while making api calls:-
2. user
  > get api/user/                  ( get user detail )
  > put api/user/<id>/             ( update user )
  > delete api/user/<id>/          ( delete user )

2. todo-list
  > get:    api/todo/               ( returns all todo tasks )
  > post:   api/todo/               ( create a todo task )
  > put:    api/todo/<id>/          ( update a todo task )
  > delete: api/vi/<id>/            ( delete a todo task )
  
  
  

