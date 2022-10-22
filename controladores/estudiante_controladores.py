from model.estudiante import Estudiante

class ControladorEstudiante:
  def __init__(self):
    print("Creando el contralador de estudiante")

  #Listar
  def index(self):
    print("Listar todos los estudiantes")
    estudiante1 = {
      "_id" : "abc1",
      "cedula" : "123456",
      "nombre" : "Juan Camilo",
      "apellido" : "Castro Pinto"
    }
    estudiante2 = {
      "_id": "abc2",
      "cedula": "654321",
      "nombre": "Pepito",
      "apellido": "Perez"
    }
    return [estudiante1, estudiante2]

  #Crear
  def create(self, info_estudiante):
    print("Crear un estudiante")
    nuevo_estudiante = Estudiante(info_estudiante)
    return nuevo_estudiante.__dict__

  #Leer
  def show(self, id):
    print("Mostrando el estudiante con id", id)
    #Buscamos en la base de datos y el resultado se guarda en estudiante2
    estudiante2 = {
      "_id": id,
      "cedula": "654321",
      "nombre": "Pepito",
      "apellido": "Perez"
    }
    return estudiante2

  #Actualizar
  def update(self, id, info_estudiante):
    print("Actualizando el estudiante con id", id)
    estudiante_actualizado = Estudiante(info_estudiante)
    return estudiante_actualizado.__dict__

  #delete
  def delete(self, id):
    print("Eliminando el estudiante con id", id)
    return {"deleted_count" : 1}