# renu-assessment
Technical Assessment Submission for Renu Robotics (Fibonacci calculator app)

Installation:
```git clone https://github.com/JamesPHawk/renu-assessment.git```

Starting the Vue + Vite app:
1. Open a terminal instance (VSCode or standalone app)
2. Run ```cd renu-assessment/renu-fibonacci-app/frontend-files```
3. Run ```npm i```
4. Run ```npm run start```
This should start running on localhost:4173

Starting the python server:
1. In a different terminal instance, ```cd renu-assessment/renu-fibonacci-app/backend-files```
2. Run ```py -3 -m venv .venv```
3. Run ```.venv\Scripts\activate```. Note that you can run ```deactivate``` to exit the virtual environment.
4. Run ```pip install -U flask```
5. Run ```pip install -U flask-cors```
6. Run ```flask run```. This should start the server at localhost:5000

From there, it's as simple as submitting integers!

To run vitest tests:
1. While the python server is running, open a new terminal instance and run <br>```cd renu-assessment/renu-fibonacci-app/tests```
2. Run ```npm i```
3. Run ```npm run test```
<br>Note that you do <strong>not</strong> need to be running the frontend server for vitest to run.

To run Playwright tests:
1. With both the Vue + Vite app <strong>and</strong> the python server running, run ```npx playwright test``` in the tests folder.
    - Running ```npx playwright test``` will just run the tests, but adding the ```--ui``` flag will open an <br>interactive window that lets you see the breakdown of the tests. 

Troubleshooting:
- If you submit a valid integer and get a ```NetworkError when attempting to fetch resource``` message, check the ```app.py``` file in **renu-fibonacci-app/backend-files/.venv**.<br>If the import statement for flask-cors is throwing an import error, try changing your python interpreter to v3.9.13 or higher. <br>This can be changed in Visual Studio Code in the bottom left corner.
