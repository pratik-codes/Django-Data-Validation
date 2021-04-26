import pandas as pd
import math
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from pandas.api.types import is_numeric_dtype

def index(request):
    """
        This function is just to check if the app is running
    """
    if "GET" == request.method:
        return HttpResponse('Server is running...')

@csrf_exempt
def upload(request):
    """
        This function takes xlsx file as an input and validates
        the fields and send the response as the error if any.
    """
    if "POST" == request.method:
        excel_file = request.FILES["excel_file"]

        #check if the file is not uploaded
        if excel_file is None:
            return HttpResponse('File not uploaded')

        # importing file using pandas excel for xlsx file 
        df = pd.read_excel(excel_file)

        # getting no of records
        number_of_rows = len(df)

        # main data with validation of all records 
        allValidation = {}
        # to check the ship modes
        shipModes = ['Regular Air', 'Delivery Truck', 'Express Air']

        #iterating over the records and validating the required columns with the rules 
        for row in range(number_of_rows):
            # used to store the record errors
            colValidation = {}
            #gets the record at index == row
            record = df.iloc[row]
            
            # if statements validating the columns on the basis of rules 
            if math.isnan(record[0]) == True:
                colValidation['A' + str(row + 2)] = 'OrderId is NaN'
            else:
                if str(record[0]).isnumeric() == False:
                    colValidation['A' + str(row + 2)] = 'OrderId contains non numeric values.'

            if math.isnan(record[2] == True):
                colValidation['C' + str(row + 2)] = 'Order Id is NaN'
            else:
                if record[2] == 0:
                    colValidation['C' + str(row + 2)] = 'Order qty is Zero' 
            
            if math.isnan(record[3]) == True :
                colValidation['D' + str(row + 2)] = 'Sales is NaN'
            else: 
                if isinstance(record[3], float) == False:
                    colValidation['D' + str(row + 2)] = 'Sales contains non numeric values.'

            if record[4]:
                mode = record[4]
                if mode not in shipModes:
                    colValidation['E' + str(row + 2)] = 'Ship Mode is Wrong.'
            else:
                colValidation['E' + str(row + 2)] = 'Ship mode is NaN'

            if math.isnan(record[5]) == True:
                colValidation['F' + str(row + 2)] = 'Profit is NaN'
            else:
                if record[5] == 0:
                    colValidation['F' + str(row + 2)] = 'Profit is Zero' 

            if math.isnan(record[6]) == True:
                colValidation['G' + str(row + 2)] = 'Unit Price is NaN'
            else:
                if record[6] == 0:
                    colValidation['G' + str(row + 2)] = 'Unit Price is Zero'   

            # store the record validation to the main json object
            # why +2 indexing starts with 0 and row 1 is header row 
            allValidation[row + 2] = colValidation
        
        #creating response structure 
        response = {}
        response['statusCode'] = 200
        response['message'] = 'Request successful.'
        response['data'] =  allValidation

       
        return JsonResponse(response)








