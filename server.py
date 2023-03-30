from flask import Flask,render_template,request,redirect,url_for
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/<string:page_name>")
def new_page(page_name):
	return render_template(page_name)

def write_to_csv(data):
    with open ("database.csv", mode= "a") as database:
        name = data['name']
        email = data['email']
        csv_writter = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([name,email])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Something went wrong"