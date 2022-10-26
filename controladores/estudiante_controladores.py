from model.estudiante import Estudiante
from repository.estudiante_repository import RepositorioEstudiante

class ControladorEstudiante:
  def __init__(self):
    self.repo = RepositorioEstudiante()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_estudiante):
    nuevo_estudiante = Estudiante(info_estudiante)
    return self.repo.save(nuevo_estudiante)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_estudiante):
    estudiante_actualizado = Estudiante(info_estudiante)
    return self.repo.update(id, estudiante_actualizado)

  #delete
  def delete(self, id):
    return self.repo.delete(id)