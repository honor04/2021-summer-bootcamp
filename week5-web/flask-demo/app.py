from flask import Flask
from flask import request

app = Flask(__name__)
first_to_last_names = {"anna": "zhang", "mike": "li"}


@app.route('/hello')
def hello_world():
    return 'Hello, '


@app.route('/user/<name>')
def show_user_profile(name: str):
    names = name.split("_")
    if len(names) > 1:
        return look_up_user_info(names[0], names[1])
    return look_up_user_info(names[0])


@app.route('/login', methods=['POST'])
def login():
    name = request.json
    if 'last_name' in name:
        look_up_user_info(name['first_name'], name['last_name'])
    return look_up_user_info(name['first_name'])


def look_up_user_info(first_name: str, last_name: str = None) -> str:
    if first_name in first_to_last_names:
        return "User last name is: " + first_to_last_names[first_name]
    else:
        if last_name is not None:
            first_to_last_names[first_name] = last_name
            return "User Updated!"
        else:
            return "User Update failed, last name is None"


if __name__ == "__main__":
    app.run()
