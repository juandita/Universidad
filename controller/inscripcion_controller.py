from model.inscripcion import Inscripcion
from repository.inscripcion_repository import RepositorioInscripcion
from repository.materia_repository import RepositorioMateria
from repository.estudiante_repository import RepositorioEstudiante

class ControladorInscripcion:
  def __init__(self):
    self.repo = RepositorioInscripcion()
    self.repo_materia = RepositorioMateria()
    self.repo_estudiante = RepositorioEstudiante()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_inscripcion):

    #Validar que la materia y el estudiante existan en la base de datos

    nuevo_inscripcion = Inscripcion(info_inscripcion)
    return self.repo.save(nuevo_inscripcion)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_inscripcion):
    inscripcion_actualizado = Inscripcion(info_inscripcion)
    return self.repo.update(id, inscripcion_actualizado)

  #delete
  def delete(self, id):
    return self.repo.delete(id)

  def find_by_estudiante(self, id_estudiante):
    inscripciones = self.repo.query({"id_estudiante": id_estudiante})
    for x in inscripciones:
      del x["id_estudiante"]
      id_materia = x["id_materia"]
      del x["id_materia"]
      x["materia"] = self.repo_materia.find_by_id(id_materia)
    return inscripciones

  def find_by_materia(self, id_materia):
    inscripciones = self.repo.query({"id_materia": id_materia})
    for x in inscripciones:
      del x["id_materia"]
      id_estudiante = x["id_estudiante"]
      del x["id_estudiante"]
      x["estudiante"] = self.repo_estudiante.find_by_id(id_estudiante)
    return inscripciones