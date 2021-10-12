from flask import Flask, render_template, url_for, request, redirect
import os
import csv

pages = os.listdir('./templates')
print(pages)


app = Flask(__name__)

        
@app.route("/")
def homePage():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_pages(page_name):
    return render_template(page_name)

def write_to_db(data):
    with open('./database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_db_csv(data):
    with open('./database.csv', mode='a', newline='') as databaseCSV:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = csv.writer(databaseCSV, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_db_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to db'
    else:
        return 'Something went wrong'