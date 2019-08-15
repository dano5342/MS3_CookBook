# Cookbook Application
## Milestone Project 3
### Overview
This project is a CRUD application, showcasing skills and knowledge I've picked up whilst working with Python during my Data Centric Development module. The main point of this project is to showcase my understanding of CRUD operations and knowledge of the Flask framework.

### User Experience Design
My wire frames were created in Adobe XD and can be found here: https://drive.google.com/drive/folders/14bAhV6GNAMR6ZMHtpchkEUYtwtR5it1g My design inspiration for this site was taken from other applications with the same scope, such as [My Cookbook Online](https://www.mycookbook-online.net/en-gb/home/)

This website is aimed at a few different types of users:
1. Users who want to be able to store an online copy of their own recipes.
2. Users who are looking for inspiration from others on what and how to cook.
3. Users looking to change and update their own recipes. Or to make changes to others recipes to compare flavours.


### Features
The main Features of this website will be CRUD utilities to be able to Create, Read, Update and Delete from an existing database of information, with subdatbases for storing Cooktime/Preptime and displaying this data with D3/Crossfilter to display this easily. 

Along side this there will be other subsets of data based on user reviews and how many up/downvotes these recipes have from other users. 

The application will display the recipe, method and ingredients for each recipe in its own templated page, whilst also allowing the user to determine what type of cuisine this is and allowing them to attribute an image to each recipe that they upload.

### Technologies Used
This application will make use of a few different technologies to help create a good user experience and keep load times low. 

1. Python: There will be a lot of python frameworks which will be found in the requirements.txt file. However the predominant tech used here will be the Flask Framework.
2. D3/Crossfilter: This will be used to visualize cooktimes better.
3. BootStrap - Will be used to reduce the amount of SCSS and CSS coding that is necessary.
4. Font Awesome - Used for displaying nice UX icons for the layout in the website

### Testing
During Development so far I've added return statements to ensure that the database is connected correctly.

### Deployment Write-up

## Credits

### Media
All Flags were sourced from Wikipedia, please note I do not claim to own any copyright or ownership of these images.
All images of food were sourced from pexels, acknowledgements will be made below. As above I do not own any copyright or ownership of these images.

### Acknowledgements


### Sources

## Further Write up

### Deploying Locally
1. Git Clone this application into an IDE or onto a workspace on your computer.
2. Ensure python3 and pip are installed on your machine
3. run ```$ pip install -r requirements.txt --no-index --find-links file:///tmp/packages```
4. ensure you have a [mongodb](https://www.mongodb.com/) username and login. Create yourself a database and a cluster to start using the information on the application
5. modify your .bashrc with your mongodb username + Password into VarEnvs for ```MONGO_DBNAME``` and ```MONGO_URI``` 
6. You now have access to the database, the app should be able to run through any data you give it as long as the routing is correct.


test line