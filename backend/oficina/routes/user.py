
from flask import Blueprint, request, jsonify, current_app
from schemas.user import UserSchema
from models.user import User

bp_user = Blueprint('user', __name__)

@bp_user.route('/findAll', methods=['GET'])
def findAll():
    result = User.query.all()
    return UserSchema(many=True).jsonify(result), 200


