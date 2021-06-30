#!/usr/bin/python3
import json
import os.path
import models
import datetime


class FileStorage:

    __file_path = "file.json"
    __objects = {}

#    def __init__(self):
#        super().__init__()

   # @property
    def all(self):
        return (FileStorage.__objects)
    
   # @new.setter
    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    def save(self):
        context_obj = {}
#        list1 = ["created_at", "updated_at"]
        for key in FileStorage.__objects.keys():
#            if key not in list1:
            context_obj[key] = FileStorage.__objects[key].to_dict()
#            else:
#                context_obj[key] = value.isoformat() 
            
        with open(FileStorage.__file_path, "w") as f:
            json.dump(context_obj, f)
                
    def reload(self):
        try:
#        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') as f:
                context2 = json.load(f)
            
                for key in context2.keys():
                    new_value = context2[key]
                    clss = new_value['__class__']
#                    self.new(eval(clss)(**value))

        except Exception as e:
            pass
