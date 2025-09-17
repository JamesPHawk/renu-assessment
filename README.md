# renu-assessment
Technical Assessment Submission for Renu Robotics (Fibonacci calculator app)

Installation:
git clone https://github.com/JamesPHawk/renu-assessment.git

Starting the Vue + Vite app:
1. Open a terminal instance (VSCode or standalone app)
2. Run ```cd renu-fibonacci-app/frontend-files```
3. Run ```npm i```
4. Run ```npm run build```
5. Run ```npm run preview```
This should start running on localhost:4173

Starting the python server:
1. In a different terminal instance, ```cd renu-fibonacci-app/backend-files```
2. Run ```.venv\Scripts\activate```
3. Run ```pip install -U flask```
4. Run ```pip install -U flask-cors```
5. Run ```flask run```. This should start the server at localhost:5000

To run the tests:
1. While the python server is running, open a new terminal instance and cd into ```cd renu-fibonacci-app/frontend-files/tests```
2. Run ```npm run test```


From there, it's as simple as submitting integers!

Troubleshooting:
- If you submit a valid integer and get a ```NetworkError when attempting to fetch resource``` message, check the ```app.py``` file in **renu-fibonacci-app/backend-files/.venv**.<br>If the import statement for flask-cors is throwing an import error, try changing your python interpreter to v3.9.13. <br>This can be changed in Visual Studio Code in the bottom left corner.
