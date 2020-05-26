import json


def create_json_file(data):
    with open('answer.json', 'w') as f:
        f.write(str(data))


def update_json_file(field, text):
    jsonFile = open("answer.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()

    ## Working with buffered content
    data[field] = text

    ## Save our changes to JSON file
    jsonFile = open("answer.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()
