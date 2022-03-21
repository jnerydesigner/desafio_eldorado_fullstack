from flask import Blueprint, request, jsonify, current_app

from schema.users import UserSchema

bp_user = Blueprint('users', __name__)


@bp_user.route('/create-user', methods=['POST'])
def register():
    # import ipdb; ipdb.set_trace()

    us = UserSchema()

    user, error = us.load(request.json)

    if error:
        return jsonify(error), 401

    return us.jsonify(user), 201
