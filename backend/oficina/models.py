from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {"id": self.id, "name": self.name}


class CarsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(255), nullable=False)
    manufacturer = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {"id": self.id, "model": self.model, "manufacturer": self.manufacturer}


class ClientCar(db.Model):
    __tablename__ = 'client_car'
    id = db.Column(db.Integer, primary_key=True)
    characteristics = db.Column(db.String(250), nullable=False)
    license_plate = db.Column(db.String(250), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                          nullable=False)
    # car_model_id = db.Column(db.Integer, db.ForeignKey('cars_model.id'),
    #                          nullable=False)
    # client = db.relationship('CarsModel',
    #                          backref=db.backref('client_car', lazy=True))
    client = db.relationship('Users',
                             backref='client_car', lazy=True)

    def to_json(self):
        return {
            "id": self.id,
            "characteristics": self.characteristics,
            "license_plate": self.license_plate,
            "client_id": self.client_id,
            "client": self.client
        }
