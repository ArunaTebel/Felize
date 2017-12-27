**ArCheun - Felize | REST API**
=======

This is the REST API of the Felize - Project Management Application. The API is built using Django + Django REST Framework + Django OAuth Toolkit

---

**How to setup and run the API Server**

1. Install python (version 3.4 is recommended)
2. Setup a MySQL database server. (This is optional. The sqlite database which comes bundled with Django can also be used. If you prefer sqlite, change the settings.py DATABASE setting accordingly)
3. If using MySQL, install the python mysql clients. Below is the Linux command to install them
    
    >`sudo apt-get install python3-dev libmysqlclient-dev`
3. Clone this repository (or a fork) into your working environment.
4. Using the terminal navigate into the project root directory.
5. Install Django + dependencies. This can be done in two ways.

    1. Using `virtualenv` (RECOMMENDED)
        1. Install `virtualenv` by referring to **[this](https://virtualenv.pypa.io/en/stable/installation/)** guide
        2. Using the terminal navigate into the project root directory (the one we just cloned above).
        3. Execute the below command (Replace python3.4 with the correct python version you installed)
            
            >`virtualenv -p /usr/bin/python3.4 env` 
        4. This will setup a virtual environment which contains python 3.4 and required other modules.
        5. If the above step is successful, activate the virtual environment by executing,
            
            >`source env/bin/activate`
        6. Now your terminal entry will have (env) prefix.
        7. Install the re-requisites by executing,
            
            >`pip install -r requirements.txt`
        8. The above command will install django + all other pre requisites in order to run the API Server.
        
    2. Globally installing (NOT RECOMMENDED)
        1. Install the below mentioned python libraries [Omit `mysqlclient` if you do not use MySQL as your database]
           
                 Django==2.0
                 django-oauth-toolkit==1.0.0
                 djangorestframework==3.7.7
                 mysqlclient==1.3.12

7. Migrate the models and flush the database by executing the below command.
    
    >`python manage.py makemigrations`
8. Create a super user account to use with the Admin site.
    
    >`python manage.py createsuperuser`
6. Navigate inside the `[app_root]/FelizeAPI` directory and start the server by executing the below command.
    
    >`python manage.py runserver`
    
---
    
**How to setup a client application**

1. After starting the server, using the browser open the admin site using the below url and log into the system using super user account credentials we just created above.
    
    >`http://127.0.0.1:8000/admin/`
2. Under **`Site administration > DJANGO OAUTH TOOLKIT > Applications`** click on the **`+Add`** button to register a client app.
3. Provide the below basic information. Keep other fields blank/default. Keep a note on the `Client id` and the `Client secret`.
    Client Type: Confidential
    Authorization grant type: Resource owner password-based
    Name: Provide any name
    
4. Save

---

**How to communicate with the API**
1. After successfully setting up an application, you can communicate to the API using any HTTP client of your preference. Below examples are using `curl` shell command
1. Request an access token. 
    Replace <user_name>, <password> with the super user account credentials (or any user account you created in the admin site) 
    Replace <client_id>, <client_secret> with the relevent values generated when registering the client application.

    >`curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/`
2. The response for the above request will be similar to below
 
    >`{
        "access_token": "<your_access_token>",
        "token_type": "Bearer",
        "expires_in": 36000,
        "refresh_token": "<your_refresh_token>",
        "scope": "read write groups"
    }`
3. Now you can communicate with the API Endpoints using the above received access token. For eg: to retrieve users list and a single user

    >`curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/users/`
    
    >`curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/users/1/`

