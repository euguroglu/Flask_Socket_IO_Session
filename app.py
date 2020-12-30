from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True

socketio = SocketIO(app)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('username',namespace='/private')
def receive_username(username):
    users[username] = request.sid
    print('Username added')

@socketio.on('private_message',namespace='/private')
def private_message(payload):
    recipient_session_id = users[payload['username']]
    message = payload['message']

    emit('new_private_message',message,room=recipient_session_id)

@socketio.on('join_room',namespace='/private')
def handle_join_room(room):
    join_room(room)
    emit('room_message','a new user has joined',room=room)

if __name__ == "__main__":
    socketio.run(app)
