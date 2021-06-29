import json
import os.path
from models.base_model import BaseModel

class FileStorage():

    __file_path = "file.json"
    __objects = {}

#    def __init__(self):
#        super().__init__()

   # @property
    def all(self):
        return self.__objects
    
   # @new.setter
    def new(self, obj):
        name = obj.__class__.__name__ + "." + obj.id
        self.__objects[name] = obj

    def save(self):
        context_obj = {}
        list1 = ["created_at", "updated_at"]
        for key, value in self.__objects.items():
            if key not in list1:
                context_obj[key] = value.to_dict()
            else:
                context_obj[key] = value.isoformat() 
            
        with open(__class__.__file_path, "w") as f:
            json.dump(context_obj, f)
                
    def reload(self):
        if os.path.isfile(__class__.__file_path):
            with open(__class__.__file_path, "r") as f:
                context2 = json.load(f)
                obj_new = {}
                for key, value in context2.items():
                    clss = value['__class__']
                    obj_new[key] = eval(clss)(**value)
                __class__.__objects.update(obj_new)
        else:
            return
