#### 启动命令
gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:app
gunicorn -c gunicorn.conf app:app

#### 使用
1.访问http://127.0.0.1:9004/page

#### 说明
1.服务端通过schedule实现websocket服务
2.前端需要相应版本的socket.io.js实现客户端功能
3.如果是在其他方法中需要emit,则需要将socketIo对象传递过去
4.使用gunicorn启动项目时需要设置worker_class= "geventwebsocket.gunicorn.workers.GeventWebSocketWorker"