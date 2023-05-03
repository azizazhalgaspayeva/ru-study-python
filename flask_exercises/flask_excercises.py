from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users = {}

        def create_dict_item(d, key, data):
            users[key] = data

        def change_dict_key(d, old_key, new_key):
            d[new_key] = d.pop(old_key)

        def delete_dict_item(d, key):
            d.pop(key)
            return key

        @app.route("/user", methods=["POST"])
        def create():
            data = request.get_json()
            try:
                name = data.pop("name")
            except:
                name = None
            error = None

            if name is None:
                error = {"errors": {"name": "This field is required"}}

            if error is None:
                create_dict_item(users, name, data)
                message = {"data": "User {} is created!".format(name)}
                return message, 201
            else:
                return error, 422

        @app.route("/user/<name>", methods=["GET", "PATCH", "DELETE"])
        def user(name):
            if request.method == "GET":
                if name in users.keys():
                    message = {"data": "My name is {}".format(name)}
                    return message, 200

                error = {"errors": {"name": "Not found."}}
                return error, 404

            elif request.method == "PATCH":
                data = request.get_json()
                new_name = data["name"]
                if name in users.keys():
                    change_dict_key(users, name, new_name)
                    message = {"data": "My name is {}".format(new_name)}
                    return message, 200

                error = {"errors": {"name": "Not found."}}
                return error, 404

            elif request.method == "DELETE":
                if name in users.keys():
                    user = delete_dict_item(users, name)
                    return user, 204

                error = {"errors": {"name": "Not found."}}
                return error, 404

        @app.route("/404")
        def not_found():
            error = {"errors": {"name": "Not found."}}
            return error, 404
