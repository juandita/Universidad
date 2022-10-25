import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb://djrufo:djrufo@ac-chtmtax-shard-00-00.zfgnppe.mongodb.net:27017,ac-chtmtax-shard-00-01.zfgnppe.mongodb.net:27017,ac-chtmtax-shard-00-02.zfgnppe.mongodb.net:27017/bd-registro-academico?ssl=true&replicaSet=atlas-uj6q8j-shard-0&authSource=admin&retryWrites=true&w=majority", tlsCAFile=ca)
ra_db = client["bd-registro-academico"]
coll_estudiantes = ra_db["estudiantes"]
estudiante = {
  "nombre" : "Roberto",
  "apellido" : "Lopez",
  "Edad" : 25,
  "telefonos" : ["369214578"],
  "materias" : [
    {
      "nombre" : "Fisica",
      "creditos" : 1
    },
    {
      "nombre" : "Calculo",
      "creditos" : 2
    }
  ]
}
coll_estudiantes.insert_one(estudiante)