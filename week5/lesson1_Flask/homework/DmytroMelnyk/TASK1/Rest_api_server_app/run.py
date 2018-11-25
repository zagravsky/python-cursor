from app import app
from app.main import routes

"""
Task 1
Create REST-api server app which will return json data. It should have options to create and delete data.
Create fabric for Dev and Test mode.
Topics: Cars, Flowers, Football, Food, Movies. (Choose one of them)
Get all elements, get certain element, add new element, delete element by name;
Use dict instead of the database
"""

if __name__ == "__main__":
    app.run()
