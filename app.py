from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrapeMars import doIt


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

marsdb= mongo.db.marsDB
marsdb.drop()

@app.route("/")
def index():
    newVariable=""
    mars_results = marsdb.find()
    for x in mars_results:
        newVariable=x
    
    return render_template("index.html", mars_results=newVariable)

@app.route("/scrape")
def scraper():

    mars_data = doIt()
    marsdb.insert_one(mars_data)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

# mars_data = doIt()
# marsdb.insert_one(mars_data)
# mars_results = marsdb.find()
# for x in mars_results:
#     print(x)