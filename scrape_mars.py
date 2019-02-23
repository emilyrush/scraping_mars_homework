from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
  destination_data = mongo.db.collection.find_one()
  return render_template("index.html", mars=destination_data)

@app.route("/scrape")
def startscrape():
  print(mission_to_mars.scrape())
  mars_data = mission_to_mars.scrape()
  mongo.db.mars.update({}, mars_data, upsert=True)
  return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
#----------------------------------------------

# * Start by converting your Jupyter notebook into a Python script called
#  `scrape_mars.py` with a function called `scrape` that will execute all 
#  of your scraping code from above and return one Python dictionary containing 
#  all of the scraped data.

# * Next, create a route called `/scrape` that will import your `scrape_mars.py` 
# script and call your `scrape` function.

#   * Store the return value in Mongo as a Python dictionary.

# * Create a root route `/` that will query your Mongo database and pass the
#  mars data into an HTML template to display the data.

# * Create a template HTML file called `index.html` that will take the mars data
#  dictionary and display all of the data in the appropriate HTML elements. Use the following
#   as a guide for what the final product should look like, but feel free to create your own design.