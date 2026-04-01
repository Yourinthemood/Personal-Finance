#PS 1st CP2 This file manages data so that it can be stored across runs
import json


#JSON reader
def JSON_reader():
    with open("ENTER FILE PATH HERE", "r") as info:
        data = json.load(info)
        return data

#!TO THE GROUP PROJECT FOR PERSONAL FINANCES! Some of the variable names are the way they are because I stole this code from a previous project I made - I did make the code but some stuff needs to be fixed

#JSON file saving func (dictionary of user information)
def JSON_add(new_info):
    #open the JSON with the writing and reading mode and make a dictionary with the current user information
    with open("ENTER FILE PATH HERE", "r+") as shapes:
        #add new dictionary to previous info
        data = json.load(shapes)
        data.update({new_info["Name"]:new_info})
        shapes.truncate(0)
        shapes.seek(0)
        #upload that new dictionary to the JSON
        json.dump(data,shapes,indent=4)

#!STILL WORKING ON JSON EDITOR DONT USE!

#JSON editor - takes in sub second to highest level of the changed dictionary to change
def JSON_edit(changed_dict,name):
    with open("ENTER FILE PATH HERE", "w") as old_data:
        data = JSON_reader() #change Name to whatever info the sub_dicts are named by
        data[changed_dict[name]] = changed_dict
        json.dump(data,old_data,indent=4)
