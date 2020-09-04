# PubMedAPI

## Pre-requisites
Install the following on your local machine:
* pip
* Python3

## Setup

### Linux/Mac OS X
Create a virtual environment in the root directory:
```
python3 -m venv venv
```
Activate the virtual environment:
```
source venv/bin/activate
```
Install the required packages/dependencies:
```
pip install -r requirements.txt
```
Run the app:
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```

Development server will now be running at http://127.0.0.1:8000/

