# Setting up the environment
- Firstly, install fastapi using command propmt "python -m pip install fastapi". 
- After this, intall uvicorn server to run the application. In cmd write "pip install uvicorn"

# Opening the project in the code editor (I have used vs code) 
- open the entire project folder in code editor.

# Connecting MongoDB server 
- Use Mongo Atlas cloud database.
- Sign-up/sign-in in Mongo Atlas and create a free cluster.
- Then connect the cluster using 'driver' option.
- In driver option, the instructions are there. They say to copy and paste a coomand to install pymongo which is to be written on the vs code project terminal to interate pymongo with the project.
- In drive option, there are also a url which is for connecting the project with this cluster. I have used this in config.py file. 

# Running the project 
- After successfully connection the mongo atlas cluster database, in project terminal write "uvicoen main:app --reload" command to run the project. 
- It will provide a link to follow to see the project output. 
- With that link add /docs in the browser address bar to see the Swagger documentation UI.

# Deploying and maintaining the project 
- I would try deploy this project on Heroku as it is a backend application. 
- I would try to update the dependencies time to time.
- I would add more useful and handy features in accordance with not only the user demand, but also with the own idea.
- I would try to optimize the application using techniques like "Caching" and "Refactoring".