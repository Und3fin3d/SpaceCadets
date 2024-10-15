from flask import Flask, render_template
from flask_socketio import SocketIO
from interpreter import Interpreter

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('run')
def run(request):
    I = Interpreter([x.split() for x in request.replace(';','').splitlines()])
    socketio.emit('output', str(I.mem))

if __name__ == "__main__":
    socketio.run(app)