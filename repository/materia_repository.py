from model.materia import Materia
from repository.repository_interface import InterfaceRepository
from repository.departamento_repository import RepositorioDepartamento

class RepositorioMateria( InterfaceRepository[Materia] ):

  def __init__(self):
    super().__init__()
    self.repo_dep = RepositorioDepartamento()

  def find_all(self):
    lista_materias = super().find_all()
    for x in lista_materias:
      id_dep = x["id_departamento"]
      del x["id_departamento"]
      x["departamento"] = self.repo_dep.find_by_id(id_dep)
    return lista_materias

  def find_by_id(self, id):
    materia = super().find_by_id(id)
    id_dep = materia["id_departamento"]
    del materia["id_departamento"]
    materia["departamento"] = self.repo_dep.find_by_id(id_dep)
    return materia