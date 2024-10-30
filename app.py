from flask import Flask, send_file, request, render_template, redirect, url_for
from image import createTicket
import sys
import os
import json
import uuid

app = Flask(__name__)

JSON_FILE_PATH = 'users.json'

def read_json():
    # Read data from the JSON file
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def write_json(data):
    # Write data to the JSON file
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def name():
    return render_template('index.html', title="LigerSat Boarding Pass")

@app.route('/create/ticket',methods=["POST"])
def index():
    if request.method == "POST":
        # Extracting form data
        name = request.form['name']
        nationality = request.form['nationality']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
    
        # Read existing users from the JSON file
        users = read_json()

        # Check if the user already exists
        if any(user['email'] == email for user in users):
            return "Your email already exists", 400
        
        # Generate a unique ID
        unique_id = str(uuid.uuid4())

        # Prepare new user info
        user_info = {
            "email": email,
            "firstname": firstname,
            "lastname": lastname,
            "name": name,
            "nationality": nationality,
            "id": unique_id
        }

        # Add the new user to the list
        users.append(user_info)

        # Write the updated user list back to the JSON file
        write_json(users)

        filename = createTicket(f'{name.upper()}', nationality.upper(), 1, unique_id)
        # Redirect to the ticket page with the unique ID
        return redirect(url_for('ticket', id=unique_id))
    
    return "Invalid request method", 405



@app.route('/ticket/<id>')
def ticket(id):
    # Read users from the JSON file
    users = read_json()
    user = next((user for user in users if user['id'] == id), None)
    
    if user:
        return render_template('ticket.html', image=f'{id}.png', name=user['firstname'])
    else:
        return 404

@app.route('/download')
def download():
    image = request.args['image'] 
    return send_file("./static/images/" + image, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)