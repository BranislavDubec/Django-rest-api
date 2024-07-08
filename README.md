# Simple Django REST api project
This is simple project to get hands on framework Django. 
 

## Prerequisities
- Python3 

## Installation

1.  **Clone github repository**:
    ```sh
    git clone https://github.com/BranislavDubec/Django-rest-api.git

    cd Django-rest-api/
    ```
2. (*optional*) **Create virtual environment**:
    
    ```virtualenv -p python3 env``` or

    ```python -m venv env```

    and activate it
3.  **Install requirements**:
    ```sh
    pip install -r requirements.txt
    ```
4.  **Migrate database and run server**:
    
    ```sh
    cd apichall/
    python manage.py migrate
    python manage.py runserver
    ```

## Usage

After successfull instalation, the project should be running on localhost on port 8000: http://127.0.0.1:8000/. E.g.:
#### Get
- http://127.0.0.1:8000/countries/?country-code=CZ&limit=500&offset=0
- http://127.0.0.1:8000/countries/?limit=2&offset=3
- http://127.0.0.1:8000/countries
- http://127.0.0.1:8000/countries/2
#### Put 
- http://127.0.0.1:8000/countries/2
    - Required name, countryCode, optional groupId
    - {
    "name": "Czechia",
    "countryCode": "CZ",
    "groupId": 5
}
#### Post
- http://127.0.0.1:8000/countries
    - Required name, countryCode, optional groupId
    - {
    "name": "Czechia",
    "countryCode": "CZ",
    "groupId": 10
}

