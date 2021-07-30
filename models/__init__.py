#!/usr/bin/python3
import models
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.engine import file_storage

storage = file_storage.FileStorage()

models.storage.reload()
