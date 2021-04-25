## virtual ENV 

- installing `py -m pip install --user virtualenv`

- creating `py -m venv env`

- Activating `.\env\Scripts\activate`

## Uploading and validating the Excel file in Django

- Clone this repo to your system.

- Create a virtual environment and activate it.

- Install the dependencies using `pip install -r requirement.txt`.

- Start the python server, `python manage.py runserver`.

- Go to postman `localhost:8000/upload/` in body add excel_file and type as file and upload the `Orders-With Nulls.xlsx` file.

- Content will be displayed on reponse as JSON.

### Postman collection is also provided with the code for ease.

