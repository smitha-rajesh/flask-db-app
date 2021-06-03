# flask-db-app
A repo for setting up a Flask + MySql app. The app has a form with 3 fields, which once submitted, saves the data into the MySql database.

**Instructions:**
1. Create virtualenv and run the requirements file.
2. Login to MySql. Create database employees. Create User "db_user" with password. Grant all privileges to this user.
3. Update the password within the app.
4. To run the flask db app on a local machine: python app.py

**How to use the app:**
- Launch the URL and proceed with filling up the form:
http://localhost:5000/form
- Enter the name, email and department and click on Submit.
- You should http://localhost:5000/login and text "Records inserted successfully into Employees and Department table!"
- Open MySql and login with db_user. Use employees database and check the tables Employee and Department for the inserted records.
