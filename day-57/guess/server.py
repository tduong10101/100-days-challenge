from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)

@app.route('/')
def home():
    ran_num = random.randint(0,10)
    year = datetime.datetime.now().year
    return render_template("index.html",num=ran_num, year=year)

@app.route('/guess/<name>')
def guess(name):
    agify = f"https://api.agify.io/"
    genderize = f"https://api.genderize.io"
    params = {'name': name}
    response = requests.get(agify,params=params)
    age=response.json()['age']
    
    response = requests.get(genderize,params=params)
    gender=response.json()['gender']
    
    return render_template("guess.html",name=name.title(),gender=gender,age=age)

if __name__ == '__main__':
    app.run(debug=True)