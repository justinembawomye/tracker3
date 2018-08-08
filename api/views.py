from flask import request,jsonify,make_response
from flask_restful import Resource
# from webargs.flaskparser import use_args
# from .args import songs_args, songs_id_arg
from .models import User, Requests, users
from flask import Blueprints

class UserListView(Resource):
    def post(self):
        new_user = User(
            name = ['name']
            email = ['email'] 
            username = ['username']
            password = ['password']
        ) 
        users.append(new_user)
        response={
            'messages': f'User {name} successfully created',
            }
        return make_response(jsonify(response), 201)

