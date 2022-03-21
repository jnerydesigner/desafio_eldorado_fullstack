import json
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import Users, CarsModel, ClientCar, configure as conf_mod
from flask_marshmallow import Marshmallow
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:13306/eldorado-mecanica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

ma = Marshmallow(app)

migrate = Migrate(app, db)

conf_mod(app)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users


class CarClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClientCar
        include_fk = True

# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)

#     def to_json(self):
#         return {"id": self.id, "name": self.name}


@app.route("/user", methods=["GET"])
def select_users():
    users_object = Users.query.all()
    return UserSchema(many=True).jsonify(users_object), 200
    # users_json = [users.to_json() for users in users_object]
    # return get_response(200, "users", users_json)


@app.route("/user-create", methods=["POST"])
def create_user():
    body = request.get_json()
    try:
        user = Users(name=body['name'])
        db.session.add(user)
        db.session.commit()
        return get_response(201, "usuario", user.to_json(), "Criado com sucesso")
    except Exception as e:
        print(e)
        return get_response(400, "usuario", {}, "Erro ao cadastrar")


@app.route("/cars", methods=["GET"])
def select_cars():
    cars_object = CarsModel.query.all()
    cars_json = [cars.to_json() for cars in cars_object]
    return get_response(200, "cars", cars_json)


@app.route("/cars/client", methods=["GET"])
def select_cars_client():
    client_cars_object = ClientCar.query.all()
    return CarClientSchema(many=True).jsonify(client_cars_object), 200
    # client_cars_json = [client_cars.to_json()
    #                     for client_cars in client_cars_object]
    # return get_response(200, "cars", client_cars_json)


@app.route("/car-create", methods=["POST"])
def create_car():
    body = request.get_json()
    try:
        cars = CarsModel(model=body['model'],
                         manufacturer=body['manufacturer'])
        db.session.add(cars)
        db.session.commit()
        return get_response(201, "car", cars.to_json(), "Criado com sucesso")
    except Exception as e:
        print(e)
        return get_response(400, "car", {}, "Erro ao cadastrar")


def get_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()
