from flask import Flask, send_file, request, render_template, redirect, url_for
import pymongo
import json
import image

mongolab_uri="mongodb://admin:liger72724@liger0-shard-00-00-gyl2h.mongodb.net:27017,liger0-shard-00-01-gyl2h.mongodb.net:27017,liger0-shard-00-02-gyl2h.mongodb.net:27017/test?ssl=true&replicaSet=Liger0-shard-0&authSource=admin&retryWrites=true&w=majority"

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
    
    length = collection.count()
    uniqueID = length + 1
    userInfo = { "name": name, "nationality": nationality, "uniqueID": uniqueID }
    y = collection.find({"name": name})
    print(y)
    x = collection.insert_one(userInfo)
    print(x)
    name = name.upper()
    nationality = nationality.upper()
    imageName = image(name,nationality,uniqueID) 

    return redirect(url_for('ticket', name=name))
#  return send_file(name)


@app.route('/')
def name():
    return render_template('index.html', title="Vuthy", username="Reaksmy")

@app.route('/ticket')
def ticket():
    imageName = request.args['name'] 
    return render_template('ticket.html', image=imageName)

if __name__ == "__main__":
    app.run(debug=True)