from tornado.web import RequestHandler
import hashlib


class IndexHandler(RequestHandler):
    def get(self):
        if self.request.arguments.get('wd'):
            wd = self.get_query_argument('wd')
            cookie = self.get_cookie(wd)
            self.write(cookie)
        else:
            cookies: dict = self.cookies
            html = '<ul>%s</ul>'
            lis = []
            for key in cookies:
                lis.append('<li>%s</li>' % self.get_cookie(key))
            self.write("显示所有cookies" + html % ''.join(lis))

    def post(self):
        username = self.get_body_argument('username')
        password = hashlib.md5(self.get_argument('password').encode()).hexdigest()
        if all([username == 'admin', password == hashlib.md5('123456'.encode()).hexdigest()]):
            self.write('<h1 style="color:blue">用户名:%s 密码:%s</h1>' % (username, password))
        else:
            self.write('<h1 style="color:red">用户名或密码错误</h1>')
