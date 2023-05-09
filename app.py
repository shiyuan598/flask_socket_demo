# coding=utf8
from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from apscheduler.schedulers.background import BackgroundScheduler
from task import schedule_task

app = Flask(__name__, template_folder='./')
socketio = SocketIO(app)

# 全局允许跨域
CORS(app, supports_credentials=True)

@app.route('/')
def hello():
    print("call hello")
    socketio.emit('my_response', {"message": "call hello"}, broadcast=True)
    # emit('my_response', "call hello", broadcast=True)
    return 'Hello World!'

@app.route('/page')
def page():
    return render_template('index.html')

@socketio.on('my_event')
def handle_my_custom_event(data):
    print('received message: ' + str(data))
    emit('my_response', data, broadcast=True)


# 定时任务, 更新流程的状态
def run_schedule_task():
    # 注意上下文，No application found. Either work inside a view function or push an application context.
    with app.app_context():
         schedule_task(socketio)

scheduler = BackgroundScheduler()
# 每隔60s执行一次
scheduler.add_job(run_schedule_task, "interval", seconds=20)
scheduler.start()

if __name__ == '__main__':
    print("run ...")
    socketio.run(app, host="127.0.0.1", port=9004)
