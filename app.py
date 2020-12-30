from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True

socketio = SocketIO(app)

users = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('username',namespace='/private')
def receive_username(username):
    users.append({username:request.sid})
    print(users)


if __name__ == "__main__":
    socketio.run(app)
