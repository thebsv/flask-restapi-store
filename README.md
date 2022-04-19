# A REST API in Flask for a store

## Installation:

Running the application natively using virtualenv:

- `pip3 install virtualenv`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install -r requirements.txt`
- `python3 app.py`

Running the application using docker:

- `docker build -t restapi:latest -f Dockerfile .`
- `docker run -it -p 8000:8000 restapi:latest`

## API:

Request Type: GET
Request: `0.0.0.0:8000/`
Expected Response: Welcome message

Request Type: GET
Request: `0.0.0.0:8000/store`
Expected Response: 200, Total bill, with total price and tax calculated
Error Response: 503, 500

Request Type: POST
Request: `0.0.0.0:8000/store`
Expected Body: Json list of inputs of purchases made
Expected Response: 200, List of True/False for each item inserted into the db.
Error Response: 503, 500

## References:
https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python