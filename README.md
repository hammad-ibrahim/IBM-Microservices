# Hands-on Lab - Creating a Swagger documentation for REST API

        Learning Objectives:
        After completing this exercise, you should be able to perform the following tasks:
        
        Use the Swagger Editor to create Swagger documentation for REST API
        Use SwaggerUI to access the REST API endpoints of an application
        Generate code with the Swagger documentation
        Pre-requisites
        You must be familiar with Docker applications and commands
        You must have a good understanding of REST API.
        Knowledge of Python is highly recommended
        

# Task 1 - Getting your application started
 - Open a terminal window by using the top menu in the IDE: Terminal > New Terminal, if you don’t have one open already.

        In the terminal, clone the repository which has the Swagger documentation and the REST API code ready by pasting the following command.
        The repository that you clone has code that will run a REST API application which can be used to organize tasks.

```bash 
git clone https://github.com/ibm-developer-skills-network/jmgdo-microservices.git
```
- Change the working directory to jmgdo-microservices/swagger_example by running the following command.

```bash 
cd swagger_example
```
- Run the following commands to install the required packages.

```bash 
python3 -m pip install flask flask-cors
```

- Now start the application which serves the REST API on port number 5000.
 ```bash 
python app.py
```
- Click on the Skills Network button on the left, it will open the "Skills Network Toolbox". Then click Launch Application, from there you enter the port no. as 5000 and click Your Application button. This will open a new browser page, which accesses the application you just ran.

- Copy the url on the address bar.

- From the file menu, go to jmgdo-microservices/swagger_example/swagger_config.json to view the file on the file editor.

- In the file editor, paste the application URL that you copied where it says **<Your application URL\>** without the protocol (https://) and do not put a "/" at the end of the URL and save the file.

- Copy the entire content of the file swagger_config.json. You will need this copied content to generate SwaggerUI.

- Click on this link https://editor.swagger.io/ to go to the Swagger Editor.

- From the File menu, click on Clear Editor to clear the content of the Swagger Editor.

- Paste the content you copied from swagger_config.json on the left side. You will get a prompt which says Would you like to convert your JSON into YAML? . Press Cancel to paste the content.

- You will see that the UI is automatically populated on the right.