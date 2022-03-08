# Tutorials
#### 07/03/2022   
#### By **Annalis Kirwa** 
## Description  
This is a python application that hosts the backend of the Tutorials web application <a href = "https://annaliskirwa.github.io/_App_Diecisiete/tutorials">link</a>.
It deals with the dtabases, views and API endpoints that will be consumed by the Tutorials web application on the frontend.  

## Features  
As a user of Tutorials application, you will be able to: 
* Get the various API endpoints  
* Interact with data from the various endpoints  

## API Endpoints  
* Create a tutorial: ``POST``  ``https://anntutorial.herokuapp.com/api/tutorials``  
* Retrieve tutorials: ``GET``  ``https://anntutorial.herokuapp.com/api/tutorials``   
* Retrieve a single tutorial:  ``GET``  ``https://anntutorial.herokuapp.com/api/tutorials/<id>``  
* Update a tutorial: ``PUT`` ``https://anntutorial.herokuapp.com/api/tutorials/<id>``  
* Search for a tutorial:  ``GET`` ``https://anntutorial.herokuapp.com/api/tutorials?title=<name of tutorial>``  
* Get all published tutorials:  ``GET`` ``https://anntutorial.herokuapp.com/api/tutorials/published``  
* Delete a tutorial:  ``DELETE`` ``https://anntutorial.herokuapp.com/api/tutorials<id>``  

## Setup/Installation Requirements  
 ### To interact with the Tutorials Application:
 * Have the latest version of browser installed   
 * Click on this <a href = "https://anntutorial.herokuapp.com/api/tutorials">link</a>    
  ### To contribute to Hoods web application:  
 #### Clone the Repo  
 * Create an account on Github
* Fork the repository from Github with this <a href = "https://github.com/Annaliskirwa/_App_Diecis-is" >link </a>
* Clone the repository
* Open the project cloned project
####  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `virtualenv -p /usr/bin/python3 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE tutorial;  
    
#### Run initial Migration
    python3.8 manage.py makemigrations    
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000  
    
  ## Known Bugs
There are no known bugs so far
## Technologies Used  
* Python v3.8  
* Django  
* Postgres  
* Rest APIs  
## Support and contact details
In case of any problem while interacting with the web application, reach out to me at ``annaliskirwa@gmail.com``
### License.
MIT Copyright (c) 2022 **[MITlicense](LICENSE)**



