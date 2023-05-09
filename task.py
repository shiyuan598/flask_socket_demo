from datetime import datetime

def schedule_task(socketio):
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("call schedule_task", dt)
    socketio.emit('my_response', {"message": "call schedule_task " + dt}, broadcast=True)