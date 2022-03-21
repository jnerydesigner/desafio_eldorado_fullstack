from flask_marshmallow import Marshmallow
from .models import Users, CarsModel, ClientCar


ma = Marshmallow()


def configure(app):
    ma.init_app(app)
    app.ma = ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users


# class CarModelSchema(ma.ModelSchema):
#     class Meta:
#         model = CarsModel


# class CarClientSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = ClientCar
#         include_fk = True
