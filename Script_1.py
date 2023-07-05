import json
import csv
import ast


def csv_to_json(csv_file, json_file):
    jsonList = []

    with open(csv_file, encoding="utf-8") as csvf:
        csvreader = csv.DictReader(csvf)

        counter = 0
        for row in csvreader:
            row['genre'] = ast.literal_eval(row['genre'])
            jsonList.append(row)
            counter += 1
            if counter == 200:
                break

    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonList, indent=4)
        jsonf.write(jsonString)


csvFile = "movies.csv"
jsonFile = "movies.json"
csv_to_json(csvFile, jsonFile)
