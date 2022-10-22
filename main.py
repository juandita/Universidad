from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controladores.estudiante_controladores import ControladorEstudiante

app = Flask(__name__)
cors = CORS(app)
estudiante_controller = ControladorEstudiante()

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



@app.route("/suma", methods=["POST"])
def suma():
  jj = request.get_json()
  res = jj["n1"] + jj["n2"]
  data = { "result" : res }
  return jsonify(data)


@app.route("/post", methods=["POST"])
def test():
  data = { "message" : "The server is running (POST)...." }
  return jsonify(data)

@app.route("/put", methods=["PUT"])
def test1():
  data = { "message" : "The server is running (PUT)...." }
  return jsonify(data)

@app.route("/get", methods=["GET"])
def test2():
  data = { "message" : "The server is running (GET)...." }
  return jsonify(data)


if __name__ == "__main__":
  data_config = load_file_config()
  print(f"Server running : http://{data_config['url-backend']}:{data_config['port']}")
  serve(app, host=data_config["url-backend"], port=data_config["port"])