"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Load NEO data from the given CSV file.
    with open(neo_csv_path, "r") as f:
        data_list = csv.DictReader(f)
        list_neos = []
        for data in data_list:
            neo_info = {
                "designation": data["pdes"],
                "name": data["name"] or None,
                "diameter": float(data["diameter"]) if data["diameter"] else float("nan"),
                "hazardous": False if data["pha"] in ["", "N"] else True
            }
            try:
                neo = NearEarthObject(**neo_info)
            except Exception as e:
                print(e)
            else:
                list_neos.append(neo)
    return list_neos

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # Load close approach data from the given JSON file.
    with open(cad_json_path, "r") as file:
        json_data = json.load(file)
        list_cad = []
        columns = zip(*json_data['data'])
        result = {field: list(column) for field, column in zip(json_data['fields'], columns)}
        for index in range(len(result['des'])):
            cad_info = {
                "designation": result['des'][index],
                "time": result['cd'][index],
                "distance": float(result['dist'][index]),
                "velocity": float(result['v_rel'][index]) 
            }
            try:
                cad = CloseApproach(**cad_info)
            except Exception as e:
                print(e)
            else:
                list_cad.append(cad)
    
    return list_cad


