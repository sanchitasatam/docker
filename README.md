# RESTful-web-service using DOCKER container in python and flask
 FOLLOWING ARE THE STEPS TO RUN WEB SERVICES:
 
 Step 1: Installed Docker Toolbox for Mac/Windows.
 
 Step 2: Created Json database of the name games.json
 
 Step 3: To implement our data in the form of table we used HTML and CSS for alignments and designs.
 
 Step 4: Imported Flask libraries and created function to get request from user.
 
 Step 5: Coding of the web services is implemented in python and flask
 
 Step 6: Created a docker file named Dockerfile
 
 Step 7: Open Docker terminal
 
 Step 8: Build image in docker container using **docker build -t fun-games .** (Here, name of the image is fun-games)
 
 Step 9: Run image using **docker run -d -p 5000:5000 fun-games**(Python uses default port 5000 for execution)
 
 Step 10: To check if the image is assigned with a port we used command **docker ps -a**(This displays the port number)
 
 Step 11: Open browser and insert IP address along with the port number to display the database created in json.
 
 Step 12: To display welcome page for database we used **192.168.99.100:5000**
 
 Step 13: To display entire database we used **192.168.99.100:5000/getgames/**
 
 Step 14: To display specific id parameter we used **192.168.99.100:5000/getgames/7** (id 7 will be diplayed).
 
 Step 15: To display Type parameter we used **192.168.99.100:5000/getgames/Type/Action** (All games with type action will be displayed from the database)
 
 
