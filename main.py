from flask import Flask, request, jsonify

app = Flask(__name__)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserController:
    def __init__(self):
        self.users = []

    def create_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        return user

    def get_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

user_controller = UserController()

@app.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    user = user_controller.create_user(name, email)
    return jsonify({'message': f"User created: {user.name} ({user.email})"})

@app.route('/users/<name>', methods=['GET'])
def get_user_route(name):
    user = user_controller.get_user(name)
    if user:
        return jsonify({'message': f"User found: {user.name} ({user.email})"})
    else:
        return jsonify({'message': 'User not found'})

if __name__ == '__main__':
    app.run()