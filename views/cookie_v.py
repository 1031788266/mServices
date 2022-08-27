from tornado.web import RequestHandler


class CookieHandler(RequestHandler):
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
                lis.append('<li>%s:%s</li>' % (key, self.get_cookie(key)))
            html += """
                <form method="post">
                    <input name="name" placeholder="请输入要删除的cookie">
                    <button>提交</button>
                </form>
            """
            self.write("显示所有cookies" + html % ''.join(lis))

    def post(self):
        name = self.get_argument('name')
        if self.request.cookies.get(name, None):
            self.clear_cookie(name)
            self.write('<h3 style="color:blue;">删除%s成功' % name)
            self.redirect('/cookie')
        else:
            self.write('<h3 style="color:red;">删除%s失败' % name)