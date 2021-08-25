from flask_restful import Resource, Api, abort, reqparse
# from guhitApp import db, api
from guhitApp import  api
from flask import jsonify, Flask, request
import json
from flask_cors import CORS, cross_origin
##

with open("./guhitApp/users.json") as file:
    data_users = json.load(file)

with open("./guhitApp/images.json") as file:
    data_imgs = json.load(file)

with open("./guhitApp/comments.json") as file:
    data_comments = json.load(file)
##
api_v2_cors_config = {
  "origins": ["http://localhost:5000"],
  "methods": ["OPTIONS", "GET", "POST"],
  "allow_headers": ["Authorization", "Content-Type"]
}
parser = reqparse.RequestParser()
class GuhitUsers(Resource) : 
    def get(self):
        users = data_users
    
        if users:
            return jsonify(users)
        return {"user_id": "None"}, 404

    def post(self):
        # print("HELLLLLLOOOOO---------")
        json_data = request.get_json()
        _data = (json_data)
        # args = parser.parse_args()
        # ok = args["TRY"]
        print(_data)
        data_users.append(_data)
        return _data
class GuhitUser(Resource) : 
    def get(self,user_id):
        users = data_users
        for user in users:
            if user["user_id"] == (user_id):
                return jsonify(user)
        return {"user_id": "None"}, 404

class GuhitImages(Resource) : 
    def get(self):
        imgs = data_imgs
    
        if imgs:
            return jsonify(imgs)
        return {"user_id": "None"}, 404

    def post(self):
        json_data = request.get_json()
        _data = (json_data)
        # args = parser.parse_args()
        # ok = args["TRY"]
        print(_data)
        data_imgs.append(_data)
        return _data
    @cross_origin()
    def put(self):
        json_data = request.get_json()
        json_data.headers.add("Access-Control-Allow-Origin", "*")
        _data = (json_data)
        # args = parser.parse_args()
        # ok = args["TRY"]
        user_id=_data["user_id"]
        fname=_data["fname"]
        lname=_data["lname"]
        prof_pic=_data["prof_pic"]

        for user in data_users:
            if user.user_id == user_id:
                user.fname=fname
                user.lname=lname
                user.prof_pic=prof_pic
        print(_data)
        data_imgs.append(_data)
        return _data

class GuhitImagePerUser(Resource) : 
    def get(self,user_id):
        imgs = data_imgs
        user_imgs = []
        for img in imgs:
            if img["user_id"]==user_id:
                user_imgs.append(img)
        return jsonify(user_imgs)

class GuhitImage(Resource) : 
    def get(self,img_id):
        imgs = data_imgs
        for img in imgs:
            if img["id"]==img_id:
                return jsonify(img)
            return {"img_id": "None"}, 404



class GuhitComments(Resource) : 
    def get(self):
        comments = data_comments
    
        if comments:
            return jsonify(comments)
        return {"user_id": "None"}, 404
    def post(self):
        json_data = request.get_json()
        _data = (json_data)
        # args = parser.parse_args()
        # ok = args["TRY"]
        print(_data)
        data_comments.append(_data)
        return _data

api.add_resource(GuhitUsers,"/api/users")
api.add_resource(GuhitUser,"/api/users/<string:user_id>")
api.add_resource(GuhitImages,"/api/images")
api.add_resource(GuhitImagePerUser,"/api/images/<string:user_id>")
api.add_resource(GuhitImage,"/api/images/<int:img_id>")
api.add_resource(GuhitComments,"/api/comments")
