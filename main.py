from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controller.estudiante_controller import ControladorEstudiante
from controller.materia_controller import ControladorMateria
from controller.departamento_controller import ControladorDepartamento
from controller.inscripcion_controller import ControladorInscripcion

app = Flask(__name__)
cors = CORS(app)
estudiante_controller = ControladorEstudiante()
materia_controller = ControladorMateria()
departamento_controller = ControladorDepartamento()
inscripcion_controller = ControladorInscripcion()

def load_file_config():
  with open("config.json") as f:
    data = json.load(f)
  return data

@app.route("/estudiantes", methods=["GET"])
def listar_estudiante():
  lista_estudiantes = estudiante_controller.index()
  return jsonify(lista_estudiantes)

@app.route("/estudiante", methods=["POST"])
def crear_estudiante():
  info_estudiante = request.get_json()
  estudiante_creado = estudiante_controller.create(info_estudiante)
  return jsonify(estudiante_creado)

@app.route("/estudiante/<string:id>", methods=["GET"])
def mostrar_estudiante(id):
  est = estudiante_controller.show(id)
  return jsonify(est)

@app.route("/estudiante/<string:id>", methods=["PUT"])
def actualizar_estudiante(id):
  info_estudiante = request.get_json()
  estudiante_actualizado = estudiante_controller.update(id, info_estudiante)
  return jsonify(estudiante_actualizado)

@app.route("/estudiante/<string:id>", methods=["DELETE"])
def eliminar_estudiante(id):
  resp = estudiante_controller.delete(id)
  return jsonify(resp)

@app.route("/materias", methods=["GET"])
def listar_materias():
  lista_materias = materia_controller.index()
  return jsonify(lista_materias)

@app.route("/materia", methods=["POST"])
def crear_materia():
  info_materia = request.get_json()
  materia_creado = materia_controller.create(info_materia)
  return jsonify(materia_creado)

@app.route("/materia/<string:id>", methods=["GET"])
def mostrar_materia(id):
  est = materia_controller.show(id)
  return jsonify(est)

@app.route("/materia/departamento/<string:id>", methods=["GET"])
def buscar_materia_departamento(id):
  est = materia_controller.find_by_department(id)
  return jsonify(est)

@app.route("/materia/<string:id>", methods=["PUT"])
def actualizar_materia(id):
  info_materia = request.get_json()
  materia_actualizado = materia_controller.update(id, info_materia)
  return jsonify(materia_actualizado)

@app.route("/departamentos", methods=["GET"])
def listar_departamentos():
  lista_departamentos = departamento_controller.index()
  return jsonify(lista_departamentos)

@app.route("/departamento", methods=["POST"])
def crear_departamento():
  info_departamento = request.get_json()
  departamento_creado = departamento_controller.create(info_departamento)
  return jsonify(departamento_creado)

@app.route("/inscripciones", methods=["GET"])
def listar_inscripciones():
  lista_inscripciones = inscripcion_controller.index()
  return jsonify(lista_inscripciones)

@app.route("/inscripcion", methods=["POST"])
def crear_inscripcion():
  info_inscripcion = request.get_json()
  inscripcion_creado = inscripcion_controller.create(info_inscripcion)
  return jsonify(inscripcion_creado)

@app.route("/inscripcion/estudiante/<string:id>", methods=["GET"])
def buscar_inscripcion_estudiante(id):
  est = inscripcion_controller.find_by_estudiante(id)
  return jsonify(est)

@app.route("/inscripcion/materia/<string:id>", methods=["GET"])
def buscar_inscripcion_materia(id):
  est = inscripcion_controller.find_by_materia(id)
  return jsonify(est)

if __name__ == "__main__":
  data_config = load_file_config()
  print(f"Server running : http://{data_config['url-backend']}:{data_config['port']}")
  serve(app, host=data_config["url-backend"], port=data_config["port"])