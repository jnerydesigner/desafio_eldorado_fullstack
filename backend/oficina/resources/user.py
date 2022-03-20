from flask import request
from flask_restplus import Resource, fields

from models.user import UserModel
from schemas.user import UserSchema

from server.instance import server

user_ns = server.user_ns

ITEM_NOT_FOUND = "User not found."


user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

# Model required by flask_restplus for expect
item = user_ns.model('User', {
    'name': fields.String('Name from client'),
})


class User(Resource):

    def get(self, id):
        book_data = UserModel.find_by_id(id)
        if book_data:
            return user_schema.dump(book_data)
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        book_data = UserModel.find_by_id(id)
        if book_data:
            book_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @user_ns.expect(item)
    def put(self, id):
        user_data = UserModel.find_by_id(id)
        user_json = request.get_json()

        if user_data:
            user_data.name = user_json['name']
        else:
            user_data = user_schema.load(user_json)

        user_data.save_to_db()
        return user_schema.dump(user_data), 200


class UserList(Resource):
    @user_ns.doc('Get all the Items')
    def get(self):
        return user_list_schema.dump(UserModel.find_all()), 200

    @user_ns.expect(item)
    @user_ns.doc('Create an Item')
    def post(self):
        user_json = request.get_json()
        user_data = book_schema.load(user_json)

        user_data.save_to_db()

        return book_schema.dump(user_data), 201