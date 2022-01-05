import json




def saveJson(item_to_save, write_mode='w', save_path=None):
    """
    Saves a json file with the dict you gave (item to save).
    IN:
        item_to_save: (dict) An item you want to save into a json file.
        json_path: (path) Where you want to save the json. 
            By defaut is in a temp file into the project folder.
        write_mode: (Parameter) the way you want to save it.
            By defaut is 'w' (write mode), but you can save it in any write mode supported by json.
    """
    
    save__path = save_path if save_path != None else 'temp_json.json'
    with open(save__path, write_mode) as file:
        json.dump(item_to_save, file, indent=4, sort_keys=False, ensure_ascii=False)
    file.close()



def readJson(json_path):
    """
    Returns a dictionary from the json_path you gave.
    IN:
        json_path: (path) The path of the json you want to read.
    OUT:
        readed_json: (dictionary) A dictionary from the json you gave.
    """

    with open(json_path) as file:
        readed_json = json.load(file)
    return readed_json
