# sendmail-back
Using Python Flask to build an api that sends an email

### Install Pipenv:
```brew install pipenv```

### Then, create a new virtual environment with Python 3:
```pipenv --python 3```

### You can also use a specific version of Python 3:
```pipenv --python 3.6```

If you use Visual Studio Code, select a Python interpreter following the steps below:
Open the Command Palette with `Sift+Cmd+P`
Enter “python sel” and select Python: Select Interpreter
Select your virtualenv for this project

### Install the packages used in this project:
`pipenv install flask flask-sqlalchemy`

### Run the following command to activate this project’s virtualenv:
```pipenv shell```

### Run the app file:
```python app.py```
Then, go to http://127.0.0.1:5000/ 

## To send an email, run 
`http://127.0.0.1:5000/sendmail`
Emails are currently sent to 'martinkatamba@gmail.com', and 'amoswelike@gmail.com', feel free to add another

### Visit hosted app
- Backend: https://sendflaskmail20.herokuapp.com/sendmail 
- Frontend:  https://ezyagricprice.web.app/
