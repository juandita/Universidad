from model.estudiante import Estudiante
from repository.repository_interface import InterfaceRepository

class RepositorioEstudiante( InterfaceRepository[Estudiante] ):
  pass