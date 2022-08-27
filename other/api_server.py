import uuid

from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
import json


class UserHandler(RequestHandler):
    user = {
        'id': 1,
        'username': 'admin',
        'password': '123456'
    }

    def get(self):
        Bytes = self.request.body
        print(Bytes.decode())
        json_data = json.loads(Bytes.decode())
        print(json_data.keys())

        msg = {}
        if 'username' and 'password' in json_data.keys():
            if json_data['username'] == self.user.get('username') and json_data['password'] == self.user.get(
                    'password'):
                msg['code'] = '200'
                msg['text'] = '登录成功'
                msg['token'] = uuid.uuid4().hex
            else:
                msg['code'] = '401'
                msg['text'] = '用户名或密码错误'
        else:
            msg['code'] = '400'
            msg['text'] = '参数错误'

        self.write(msg)
        self.set_header('Content-Type', 'application/json')

    def post(self):
        self.write('my port')

    def put(self, *args, **kwargs):
        self.write('my put')

    def delete(self, *args, **kwargs):
        self.write('my delete')


def make_app():
    return Application([
        ('/login', UserHandler)
    ], default_host=options.host)


if __name__ == '__main__':
    define(name='host', default='127.0.0.1', type=str, help="绑定ip")
    define(name='port', default=8000, type=int, help="绑定端口")
    app = make_app()

    parse_command_line()
    app.listen(options.port)
    print('service start in http://%s:%s' % (options.host, options.port))
    IOLoop.current().start()
