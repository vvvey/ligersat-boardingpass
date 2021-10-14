from flask import Flask, send_file, request, render_template, redirect, url_for
from bson.objectid import ObjectId
import pymongo
import json
import image
import sys
from dotenv import load_dotenv
load_dotenv()
import os


mongolab_uri = os.environ.get("DATABASE_URI")

client = pymongo.MongoClient(mongolab_uri,
                     connectTimeoutMS=10000,
                     socketTimeoutMS=None)

db = client["test"]
collection = db["name"]

app = Flask(__name__)

@app.route('/create/ticket',methods=["POST"])
def index():
    if request.method == "POST":
        name = request.form['name']
        nationality = request.form['nationality']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
    
    length = collection.count()
    order = length + 1
    userInfo = {"email": email, "firstname": firstname, "lastname": lastname, "name": name, "nationality": nationality, "order": order }
    user = collection.find({"email": email})
    if user.count() > 0:
        return "Your email is already exist"
    y = collection.find({"name": name})
    print(y)
    _id = collection.insert(userInfo)

    return redirect(url_for('ticket', id=_id))
#  return send_file(name)


@app.route('/')
def name():
    return render_template('index.html', title="LigerSat Boarding Pass")

@app.route('/ticket')
def ticket():
    _id = request.args['id'] 
    user = collection.find({"_id": ObjectId(_id)})
 
    name = user[0]["name"].upper()
    nationality = user[0]["nationality"].upper()
    order = user[0]["order"]

    print(user[0]["name"], file=sys.stderr)


    imageName = image(name,nationality,order) 
    print(imageName, file=sys.stderr)

    return render_template('ticket.html', image=imageName, name=name.capitalize())

@app.route('/download')
def download():
    image = request.args['image'] 
    return send_file("static/" + image, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)