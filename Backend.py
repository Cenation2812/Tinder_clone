from flask import abort, jsonify, request
import flask
import json

#----------------------Flask Initialization---------------------#

app=flask.Flask(__name__)

#----------------------Flask Initialization---------------------#


import firebase_admin
from firebase_admin import auth,credentials,firestore

#----------------------Firebase initialization------------------#

cred = credentials.Certificate("/content/tinder-api-clone-1fd2c-firebase-adminsdk-fvs9t-e8a24ff5b4.json")
firebase_admin.initialize_app(cred)
store=firestore.client()

#----------------------Firebase initialization------------------#

@app.route('/signup',methods=['Post'])
def signup(EmailOfUser,PasswordOfUser):
  data=request.get_json(force=True)
  EmailOfUser=data.get("email")
  PasswordOfUser=data.get("password")
  uid=""
  message=""
  try:
    user=auth.create_user(
      email=EmailOfUser,
      email_verified=False,
      password=PasswordOfUser)
    message="Succesfully created user"
    uid=user.uid
  except:
    message="User already exists"

  return jsonify("uid:",uid,"message:",message)


@app.route('/login',methods=['POST'])
def login(EmailOfUser,PasswordOfUser):
  data=request.get_json(force=True)
  EmailOfUser=data.get("email")
  PasswordOfUser=data.get("password")
  message=""
  uid=""
  try:
    user=auth.get_user_by_email(EmailOfUser)
    message="Woohooo, succesfully logged in"
    uid=user.uid
  except:
    message="User authentication failed"

  return josnify("uid:",uid,"message:",message)

user_data={}

user_data["name"]="Prachi"
user_data["Image"]="gs://tinder-api-clone-1fd2c.appspot.com/InShot_20200109_204623574 (1).jpg"
user_data["Desp"]="Amazing person"
user_data["Location"]={"Latitude":27.2046,"Longitude":77.4977,"City":"London","State":"YK","Country":"England"}
user_data["Job"]="Game developer"
user_data["Passion"]="Teacher"
user_data["Company"]="DJ Sanghvi College"
user_data["Gender"]="Female"
user_data["DOB"]="30th December 2000"
user_data["Number"]="9284573820"
user_data["CreatedAt"]=firestore.SERVER_TIMESTAMP

def userUpdateInfo(uid,user_data):

    user_info={}
    user_info["name"]=user_data["name"]
    user_info["Image"]=user_data["Image"]
    user_info["Desp"]=user_data["Desp"]
    user_info["Location"]=user_data["Location"]
    user_info["Job"]=user_data["Job"]
    user_info["Passion"]=user_data["Passion"]
    user_info["Company"]=user_data["Company"]
    user_info["Gender"]=user_data["Gender"]
    user_info["DOB"]=user_data["DOB"]
    user_info["Number"]=user_data["Number"]
    user_info["CreatedAt"]=user_data["CreatedAt"]

    store.collection("abc").document(uid).set(user_info)


if __name__ == '__main__':
  app.run(host="127.0.0.1",port="5000",debug=False)