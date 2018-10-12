import json
import pickle


def exporter():
    with open("input.json", "r") as f:
        json_object = json.dumps(f.read())

    with open("output.bin", "wb") as f:
        pickle.dump(json_object, f)


def importer():
    with open("output.bin", "rb") as f:
        print(pickle.load(f))


exporter()
importer()
