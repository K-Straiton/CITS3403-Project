# CITS3403-Project

## Purpose of the Application

ThinkMad is a discussion forum site that allows ThinkPad users and enthusiasts to share their knowledge, help others, and talk about all things ThinkPad related.
It uses a question and response system, with users being able to create an account, and then use this account to post questions and respond to existing questions from other users.

## Group Members

|Student ID|Name|Github Username|
|:--------|:------|:---------|
|22957747|Kirsty Straiton|K-Straiton|
|23343513|Lauren Pudney|laurenpudz|
|23417131|Sebastian Gazey|Sebagabones|
|23599356|Sersang Ngedup|sersangn|

## Architecture

## How to Launch

For the following steps make sure you are in the root directory of the repository.

1. Create a python virtual environment
```
python -m venv .venv
```
2. Activate the environment
```
source .venv/bin/activate
```
3. Install the requirements
```
pip install -r requirements.txt
```
4. Create the secret key enviroment variable
```
export FLASK_SECRET_KEY='<SECRET_KEY_OF_YOUR_CHOICE>'
```
5. Create the database
```
flask db init
```

```
flask db migrate
```

```
flask db upgrade
```
6. Run the app
```
flask run
```
7. Add dummy data to the server
    - Once the flask app is running, open a new terminal in the same directory.
    - Activate the python virtual enviroment in the new terminal
    - Then run the following command
```
flask add_data
```
## How to Run Tests
