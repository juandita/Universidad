from model.materia import Materia
from repository.materia_repository import RepositorioMateria
from repository.departamento_repository import RepositorioDepartamento

class ControladorMateria:
  def __init__(self):
    self.repo = RepositorioMateria()
    self.repo_departamento = RepositorioDepartamento()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_materia):
    try:
      res = self.repo_departamento.find_by_id(info_materia["id_departamento"])
    except:
      return {"message": "El departamento con id " + info_materia["id_departamento"] + " no existe"}

    if len(res) == 0:
      return {"message" : "El departamento con id " + info_materia["id_departamento"] + " no existe"}

    nuevo_materia = Materia(info_materia)
    return self.repo.save(nuevo_materia)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_materia):
    materia_actualizado = Materia(info_materia)
    return self.repo.update(id, materia_actualizado)

  #delete
  def delete(self, id):
    return self.repo.delete(id)

  def find_by_department(self, id_departamento):
    return self.repo.query({"id_departamento" : id_departamento})