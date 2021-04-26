## Project Purpose - 
- This is a Data Validation project which automates the process of validating a excel file and logs the error and problems very precisely on what the error is and at what place the error has occured.
- The excel file is imported and validated with a very well know library from python know as Pandas which is very well know for data wrangling, transformation and analysis.

## Project Setup
- Clone the project ` git clone HTTPurl`

- cd into the dir `cd Django-Data-Validation`

- then follow the steps below from creating the virtual env, installing requirements.txt to testing the API on postman. 


## virtual ENV 

- installing `py -m pip install --user virtualenv`

- creating `py -m venv env`

- Activating `.\env\Scripts\activate`

## Uploading and validating the Excel file in Django through Postman

- Clone this repo to your system.

- Create a virtual environment and activate it.

- Install the dependencies using `pip install -r requirement.txt`.

- Start the python server, `python manage.py runserver`.

- Go to postman `localhost:8000/upload/` in body add field name as excel_file and change the type to file and upload the `Orders-With Nulls.xlsx` file.

- Content will be displayed on reponse as JSON.

### Postman collection is also provided with the code for ease.

