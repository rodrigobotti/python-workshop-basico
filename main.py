import os
from dataclasses import dataclass

from flask import Flask, jsonify, redirect, request
from flask_sqlalchemy import SQLAlchemy

# Problema: tudo em um único arquivo
# boa prática: modulos/arquivos separados
app = Flask(__name__)

# Problema: falta de gestão de conexão com banco
# boa prática: módulo responsável por fazer isso
sqlite_file_path = os.path.abspath(os.path.join(os.getcwd(), "tasks.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{sqlite_file_path}"
db = SQLAlchemy()
db.init_app(app)


# ┌───────────────┐
# │   app (web)   │
# └────┬──────────┘
#      │
# ┌────▼──────────────┐
# │ regras de negócio │
# └────┬──────────────┘
#      │
# ┌────▼────────────┐
# │ banco de dados  │
# └─────────────────┘
# Problema: camada de `banco de dados` depende da camada do `servidor web`
# boa prática: camadas "baixas" não devem depender de camadas "acima"
@dataclass
class Task(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title: str = db.Column(db.String, nullable=False)
    description: str = db.Column(db.String, nullable=True)


# Problema: se houver mudanças de tabelas, elas não são sincronizadas
# boa prática: utilizar `migrations`
with app.app_context():  # <- CONTEXT MANAGER
    db.create_all()  # <- Migração de bancos de dados (database migrations)


# atende todas request em http://localhost:5000/
@app.route("/")  # <- DECORATOR
def hello_world():
    return """
  <!DOCTYPE html>
  <html>
    <head></head>
    <body>
      <h1>Hello, World!</h1>
    </body>
  </html>
  """


# atende requests GET http://localhost:5000/tasks
@app.get("/tasks")
def list_tasks():
    # Problema: camada web chamando diretamente a camada de banco de dados
    # boa prática: camada web depender de uma camada de `regras de negócio` (service)

    # Problema: não temos uma abstração de camada de persistência
    # boa prática: Repository, DAO
    loaded_tasks = db.session.query(Task).all()

    # Problema: serializando direto entidade
    # boa prática: `service` retornar objeto não entidade de ORM + camada web serializar

    return jsonify(loaded_tasks)


# atende requests GET http://localhost:5000/tasks/id_da_task
@app.get("/tasks/<int:id>")
def get_task(id):
    task = db.session.query(Task).filter(Task.id == id).first()

    # Problema: falta de gestão de erros
    # boa prática: exceptions customizadas + utilizar `error handlers`
    if task is None:
        return {"error": f"tasks/{id} not found"}, 404

    return jsonify(task)


# atende requests POST http://localhost:5000/tasks
@app.post("/tasks")
def add_tasks():
    task = Task(
        title=request.json["title"],
        description=request.json["description"],
    )
    try:
        db.session.add(task)
        db.session.commit()
        return redirect(app.url_for("get_task", id=task.id))
    except:
        # Problema: exceptions genéricas não te protegem da maneira correta
        # boa prática: exceptions customizadas + utilizar `error handlers`
        return {"error": "bad request"}, 400


if __name__ == "__main__":
    # Problema: configurações hardcoded
    # boa prática: módulo de configurações
    # (possivelmente pegando os valores de variáveis de ambiente, gerenciador de segredos, etc)
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )

# Problema: não tem teste nenhum!
# boa prática: testes unitários + testes de integração
