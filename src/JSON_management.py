#PS 1st CP2 This file manages data so that it can be stored across runs
import json


#JSON reader
def JSON_reader():
    try:
        with open("files/user_info.json", "r") as info:
            data = json.load(info)
            return data
    except:
        with open("Personal-Finance/files/user_info.json", "r") as info:
            data = json.load(info)
            return data

#!TO THE GROUP PROJECT FOR PERSONAL FINANCES! Some of the variable names are the way they are because I stole this code from a previous project I made - I did make the code but some stuff needs to be fixed

#user ID finder
def ID_find():
    try:
        with open("files/user_info.json", "r") as user_data:
            data = json.load(user_data)
            key_list = list(data.keys())
            final_index = len(key_list)-1
            final_key = key_list[final_index]
            user_id = data[final_key]["Id"]+1
            return user_id
    except:
        with open("Personal-Finance/files/user_info.json", "r") as user_data:
            data = json.load(user_data)
            key_list = list(data.keys())
            final_index = len(key_list)-1
            final_key = key_list[final_index]
            user_id = data[final_key]["Id"]+1
            return user_id

#JSON file saving func (dictionary of user information)
def JSON_add(new_info):
    data = JSON_reader()
    new_info["Id"] = ID_find()
    data.update({new_info["Username"]:new_info})
    try:
        with open("files/user_info.json", "w") as info:
            info.truncate(0)
            info.seek(0)
            #upload that new dictionary to the JSON
            json.dump(data,info,indent=4)
    except:
        with open("Personal-Finance/files/user_info.json", "w") as info:
            info.truncate(0)
            info.seek(0)
            #upload that new dictionary to the JSON
            json.dump(data,info,indent=4)