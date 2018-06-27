# Catalog Application

Udacity Front End Developer - Project 4 - Clay Haberly 4/25/2018
Written with Python 2.7.13 using Flask and sqlalchemy. 

I utilized code samples from the Udacity Full Stack Web Developer's "The Backend: Databases & Applications" module as a guide to build this application. Futher credit goes to Google, StackOverflow and BootSnip. https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
https://bootsnipp.com/snippets/M2me  

The Python code was validated using the current version of pycodestyle and the CSS was validated using the W3C CSS Validation Service. However, the template HTML pages will not pass the W3C Markup Validation Service due to the use of templates instead of indivual straight forward HTML pages.

# Detail

The application will display a list of categories and the items within the categories. Authenticated users will have full CRUD functions. Authenticated users can only edit or delete items for which they created. 
The program also includes 3 JSON endpoints.

# Installation

Vagrant and VirtualBox will need to be installed and instructions on how to do so can be found [here](https://www.udacity.com/wiki/ud088/vagrant).

### Obtain the Files:

Unzip the project file to your vagrant directory.
Within the zipped file, there is a folder named catalog and within that folder there are two other folders named static (contains css and image files) and templates (contains html template files). Also in catalog are the 3 primary files needed to install and run the program. Lastly, the client_secrets.json file is needed for the Google OAuth to function properly.

### Let's Get It Running!

##### Step 1 - Database Creation

From the vagrant console, run `database_setup.py`
This program will create a database with 3 tables: users, category and category_item

##### Step 2 - Populate the Database

From the Vagrant console run `populate_catalog.py`
This program will populate the dtabase tables with data for the application.

##### Step 3 - Start the Application

From the Vagrant console run `catalog_app.py`
This program will start the webserver and the application.

##### Step 4 - Naviagte to the web application

Open your web browser of choice and navigate to http://localhost:5000 to ensure the site is working.

## Site Useage

Once you have navigated to http://localhost:5000, the main catalog page will be rendered. 
Do not login at this point. 
From the main category page, you can click on each category item to see a list of items for that category and since you are not logged in - none of the create, edit or delete functions are availiable.
Now log in to the application and as before, you can click on each category item to see a list of items for that category but now since you are logged in - create, edit and delete functions are availiable.
Please note the edit and delete functions are limited to the user that created the entry.

## JSON endpoint Useage

This program contains 3 JSON endpoints that can be used to drill down to a specific item.
First you need to list of all categories to obtain a category_id integer value with this URL: http://localhost:5000/category/JSON
Sample response:
{
  "categories": [
    {
      "category_name": "Football", 
      "id": 1, 
      "image": "football.jpg"
    }, 
    {
      "category_name": "Baseball", 
      "id": 2, 
      "image": "baseball.jpg"
    }, 
    {
      "category_name": "Snowboarding", 
      "id": 3, 
      "image": "snowboard.jpg"
    }, 
Once you have this response, determine the category you wish to select and obtain its id value. In this case we will use "Baseball", id =2 and utilize this URL format to list items by category: http://localhost:5000/category/<int:category_id>/items/JSON
So for our sample:
http://localhost:5000/category/2/items/JSON
Response:
{
  "CategoryItems": [
    {
      "created_date": "Tue, 24 Apr 2018 18:33:11 GMT", 
      "description": "Padded leather glove for the                                 catcher", 
      "id": 7, 
      "item_name": "Baseball Catcher's Mitt", 
      "price": "$45.99", 
      "season": "Summer"
    }, 
    {
      "created_date": "Tue, 24 Apr 2018 18:33:11 GMT", 
      "description": "Padded leather glove for the out                               field.", 
      "id": 8, 
      "item_name": "Baseball Fielder's Mitt", 
      "price": "$42.50", 
      "season": "Summer"
    }, 

Now that we have our category list, we can choose a specific item using this URL format: http://localhost:5000/category/<int:category_id>/items/<int:item_id>/JSON
So to look at just "Baseball" (id=2) and "Baseball Catcher's Mitt"(id=7), we would use this URL:
http://localhost:5000/category/2/items/7/JSON
Sample response
{
  "Category_Item": {
    "created_date": "Tue, 24 Apr 2018 18:33:11 GMT", 
    "description": "Padded leather glove for the                                 catcher", 
    "id": 7, 
    "item_name": "Baseball Catcher's Mitt", 
    "price": "$45.99", 
    "season": "Summer"
  }
}


** Please note the seperation of text in the description line is due to the line wrapping in the Python code to stay under 80 characters wide.

### Markdown

Markdown written with [DILLINGER](https://dillinger.io/)

License
---
MIT
