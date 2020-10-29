from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrapeMars import scraper


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

marsdb= mongo.db.marsdb
marsdb.drop()

@app.route("/")
def index():
    mars_results = marsdb.find()
    return render_template("index.html", mars_results=mars_results)

@app.route("/scrape")
def scraper():

    mars_data = scraper()
    marsdb.insert_many(mars_data)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)