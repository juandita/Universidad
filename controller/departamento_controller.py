from model.departamento import Departamento
from repository.departamento_repository import RepositorioDepartamento

class ControladorDepartamento:
  def __init__(self):
    self.repo = RepositorioDepartamento()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_departamento):
    nuevo_departamento = Departamento(info_departamento)
    return self.repo.save(nuevo_departamento)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_departamento):
    departamento_actualizado = Departamento(info_departamento)
    return self.repo.update(id, departamento_actualizado)

  #delete
  def delete(self, id):
    return self.repo.delete(id)