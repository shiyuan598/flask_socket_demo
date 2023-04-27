# coding=utf8
from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='./')
socketio = SocketIO(app)

# 全局允许跨域
CORS(app, supports_credentials=True)

@app.route('/')
def hello():
    print("call hello")
    return 'Hello World!'

@app.route('/page')
def page():
    return render_template('index.html')

@socketio.on('my_event')
def handle_my_custom_event(data):
    print('received message: ' + str(data))
    emit('my_response', data, broadcast=True)

if __name__ == '__main__':
    print("run ...")
    socketio.run(app, host="172.16.12.84", port=9004)
