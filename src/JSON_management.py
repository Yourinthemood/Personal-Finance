#PS 1st CP2 This file manages data so that it can be stored across runs
import json


#JSON reader
def JSON_reader():
    with open("files/user_info.json", "r") as info:
        data = json.load(info)
        return data

#!TO THE GROUP PROJECT FOR PERSONAL FINANCES! Some of the variable names are the way they are because I stole this code from a previous project I made - I did make the code but some stuff needs to be fixed

#JSON file saving func (dictionary of user information)
def JSON_add(new_info):
    #open the JSON with the writing and reading mode and make a dictionary with the current user information
    with open("files/user_info.json", "w") as info:
        data = JSON_reader()
        #add new dictionary to previous info
        data.update({new_info["Name"]:new_info})
        info.truncate(0)
        info.seek(0)
        #upload that new dictionary to the JSON
        json.dump(data,info,indent=4)
