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
4. Create the database
```
flask db init
```

```
flask db migrate
```

```
flask db upgrade
```
5. Run the app
```
flask run
```
## How to Run Tests