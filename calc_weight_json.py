import json
import jsonFileHandler

data = jsonFileHandler.readJsonFile('files/insulin.json')

if data:
    # Ensure the required keys exist in the JSON data
    if 'molecules' in data and 'bInsulin' in data['molecules'] and 'aInsulin' in data['molecules'] and 'molecularWeightInsulinActual' in data:
        bInsulin = data['molecules']['bInsulin']
        aInsulin = data['molecules']['aInsulin']
        insulin = bInsulin + aInsulin
        molecularWeightInsulinActual = data['molecularWeightInsulinActual']
        
        print('bInsulin: ' + str(bInsulin))
        print('aInsulin: ' + str(aInsulin))
        print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    else:
        print("Error: Missing required keys in the JSON data.")
else:
    print("Error: The JSON data is empty or could not be read.")
