import pymongo
import json
from bson.objectid import ObjectId
from typing import TypeVar, Generic, List, get_args

T = TypeVar('T')

class InterfaceRepository(Generic[T]):

  def __init__(self):
    data_config = self.load_config()
    client = pymongo.MongoClient(data_config["database-url"])
    self.base_datos = client[data_config["database-name"]]
    the_class = get_args(self.__orig_bases__[0])
    self.coleccion = the_class[0].__name__.lower()

  def load_config(self):
    with open("config.json") as f:
      data = json.load(f)
    return data

  def save(self, item: T):
    col = self.base_datos[self.coleccion]
    _id = col.insert_one(item.__dict__)
    inserted_id = _id.inserted_id.__str__()
    x = col.find_one({"_id": ObjectId(inserted_id)})
    x["_id"] = x["_id"].__str__()
    return x

  def find_by_id(self, id):
    col = self.base_datos[self.coleccion]
    x = col.find_one({"_id": ObjectId(id)})
    x["_id"] = x["_id"].__str__()
    return x

  def delete(self, id):
    col = self.base_datos[self.coleccion]
    cuenta = col.delete_one({"_id": ObjectId(id)}).deleted_count
    return {"deleted_count": cuenta}

  def update(self, id, item: T):
    col = self.base_datos[self.coleccion]
    delattr(item, "_id")
    item = item.__dict__
    update_item = {"$set":item}
    x = col.update_one({"_id" : ObjectId(id)}, update_item)
    return {"update_count": x.matched_count}

  def find_all(self):
    col = self.base_datos[self.coleccion]
    data = []
    for x in col.find():
      x["_id"] = x["_id"].__str__()
      data.append(x)
    return data

  def query(self, the_query):
    col = self.base_datos[self.coleccion]
    data = []
    for x in col.find(the_query):
      x["_id"] = x["_id"].__str__()
      data.append(x)
    return data