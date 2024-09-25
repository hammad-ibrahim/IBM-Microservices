# Hands-on Lab - CRUD operations with Python. 
    In this lab, you will learn how to create a Products's list using a Flask server. Your application should allow you to add a product, retrieve the products, retrieve a specific product with its id, update a specific product with its id, and delete a product with its id. All these operations will be achieved through the REST API endpoints in your Flask server.

    You will create an application with API endpoints to perform Create, Retrieve, Update, and Delete operations on the above data using a Flask server.
    
    You will use cURL and POSTMAN to test the implemented endpoints.

# Objectives: -
    After completing this lab you will be able to:
    
 - Create API endpoints to perform Create, Retrieve, Update, and Delete operations on transient data with a Flask server.
 - Create REST API endpoints, and use POSTMAN to test your REST APIs.


# Set-up : Create application

- Open a terminal window by using the menu in the editor: Terminal > New Terminal.
- Change to your project folder, if you are not in the project folder already. 
 ```bash
1 cd /home/project 
```

- Run the following command to clone the Git repository that contains the starter code needed for this lab, if it doesn't already exist.

```bash
[ ! -d 'jmgdo-microservices' ] && git clone https://github.com/ibm-developer-skills-network/jmgdo-microservices.git
```

- Change to the directory jmgdo-microservices/CRUD to start working on the lab.
```bash
cd jmgdo-microservices/CRUD
```
 - List the contents of this directory to see the artifacts for this lab.
```bash
ls
```

- Run the following command on the terminal to install the packages that are required.
```bash
ls
```

- Run the following command on the terminal to install the packages that are required.
```bash
python3 -m pip install flask flask_cors
```

