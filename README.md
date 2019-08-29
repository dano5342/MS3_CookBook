# Cookbook Application
## Milestone Project 3 
### [Demo Here](https://ms3-cookbook.herokuapp.com/)
### Overview
This project is a CRUD application, showcasing skills and knowledge I've picked up whilst working with Python during my Data Centric Development module. The main point of this project is to showcase my understanding of CRUD operations and knowledge of the Flask framework.

### User Experience Design
My wire frames were created in Adobe XD and can be found here: https://drive.google.com/drive/folders/14bAhV6GNAMR6ZMHtpchkEUYtwtR5it1g My design inspiration for this site was taken from other applications with the same scope, such as [My Cookbook Online](https://www.mycookbook-online.net/en-gb/home/)

This website is aimed at a few different types of users:
1. Users who want to be able to store an online copy of their own recipes.
2. Users who are looking for inspiration from others on what and how to cook (more healthily or something different!).
3. Users looking to change and update their own recipes. Or to make changes to others recipes to compare flavours.


### Features
The main Features of this website will be CRUD utilities to be able to Create, Read, Update and Delete from an existing database of information, with subdatbases for storing ~~Cooktime/Preptime and displaying this data with D3/Crossfilter to display this easily. ~~ I decided against displaying cook/prep times as pie charts as this would have looked bad on the page layout.

~~Along side this there will be other subsets of data based on user reviews and how many up/downvotes these recipes have from other users. ~~
This was removed from my scope as CRUD was the main focus of this project. I think that my python logic here is good and that it displays a keen knowledge of how to link backend and front end together.

The application displays the recipe, method and ingredients for each recipe in its own templated page, whilst also allowing the user to determine what type of cuisine this is and allowing them to attribute an image to each recipe that they upload. This can be easily modified too, taking the data back from the DB and parsing it into prepopulated forms for the user to browse and amend as necessary.


#### Potential Future Features


At some point i'd like to revisit this project and implement the data dashboard of cook/prep times on the display page for each recipe, this should be achievable with D3 or matplotlib for Python.
I'd also like to make the page more streamline for example a single login/register page with 2 cards on the same page for easier logging in.
In future I'd like the project to have the reviews displayed after each recipe, with a vote system to see which recipes are more popular and a display for this on a seperate page ranking from top to bottom.
I'd also like to make sure in a future version that usernames are tied to the recipes they've created and therefore only they can access the CRUD functions for their own recipes to ensure the security of them.
-------
### Technologies Used
This application will make use of a few different technologies to help create a good user experience and keep load times low. 

1. Python: There will be a lot of python frameworks which will be found in the requirements.txt file. However the predominant tech used here will be the Flask Framework.
2. BootStrap - Will be used to reduce the amount of SCSS and CSS coding that is necessary.
3. Font Awesome - Used for displaying nice UX icons for the layout in the website
4. jQuery was used for the implementation of DOM manipulation (Buttons for extra fields etc.)
5. MongoDB was used for the backend on this project, I was considering MySQL but the control panel of MongoDB makes for a more user friendly experience for coding.
6. For Additional technologies used please see requirements.txt

### Testing
During Development so far I've added return statements to ensure that the database is connected correctly. This has led me to implemement small changes in the code to make sure that it works each time I've committed - and where this hasnt worked properly, i've included notes in my commit messages to the code what errors were occuring and what my thought process was to get these implemented corretly.
Manual testing was the main part of this project, As I was going for a user focus I wanted to ensure all parts of the project were user-centric and therefore manually adding in the code and ensuring the code was working before moving onto the next stage of development. This can be arduous as when you get stuck on a problem for a day or two you think of nothing else!


Manual testing was done on responsiveness of the site for the following models of phone:
1.  iPhone 5/6/7, X - This required some manipulation in SCSS to ensure that the page was full sized at all times, also using a -120% margin on a certain element that always seemed to get pushed up.
2.  iPad and iPad Pro - Button styling on the medium sized devices was good fun, pushing these down to make sure that they were spaced correctly and displayed in the middle.
3.  MacbookPro 13"
4.  Large screen sizes - Designing from my main PC means I Always style from the top down, this is counter to a mobile first development model however doing it this way for me allows to make the changes in this order and then the media queries can be done in a logical order, ensuring no conflicts in the SCSS.

-----
### Deployment Write-up
Writing this project took me about a month, I had a lot of issues with bcrypt/werkzeug.security for password implementation for users, however after trial and error and the use of YouTube tutorials and reading blogs about this I cracked it after some time. Password hashing was a good challenge. 
On top of this routing the ingredients/method parts of the recipes was a challenge too, as I wanted to store these in arrays as this made for easier inline list displays and template styling, however getting the forms to parse these to the server as arrays proved to be a bit of a beast. Displaying the data was a lot easier than taking it from the user.

The project has been deployed on [Heroku](https://ms3-cookbook.herokuapp.com/) to host the site, and all git changes can be seen on my github profile. My deployed version will not have the following code 
"""python 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True) 
        """
As this enables the user to see any potential bugs on the site and exploit this.
Environment variables were stored in my `.bashrc` folder to prevent malicious coders from exploiting my database and ruining work, I did accidentally upload these in a previous repository as can be seen in the first commit message on this project, however they are fully unavailable now.
#### Deploying Locally
1. Git Clone this application into an IDE or onto a workspace on your computer.
2. Ensure python3 and pip are installed on your machine
3. run ```$ pip install -r requirements.txt --no-index --find-links file:///tmp/packages```
4. ensure you have a [mongodb](https://www.mongodb.com/) username and login. Create yourself a database and a cluster to start using the information on the application
5. modify your .bashrc with your mongodb username + Password into VarEnvs for ```MONGO_DBNAME``` and ```MONGO_URI``` 
6. You now have access to the database, the app should be able to run through any data you give it as long as the routing is correct.

### Acknowledgements
As a student of Code Institute, I'd like to thank my mentor for his help on the project scope and minor testing during our calls
From the other students I'd like to thank Shane Muirhead, as he explained some of the documentation surrounding Indexing for text search, and password hashing.
##### Guides
I'd like to also acknowledge Miguel Grinbergs Flask Mega Tutorial for his amazing guide for a CRUD Blog site, whilst not fully read through it certainly helped in some aspects of the build.
[Corey Schafer](https://www.youtube.com/user/schafer5) and [PrettyPrinted](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)'s Videos were exceptionally helpful during the building of this project.
#### Media
All images of food were sourced from Pexels or BBCGoodFood, acknowledgements will be made below. As above I do not own any copyright or ownership of these images.
