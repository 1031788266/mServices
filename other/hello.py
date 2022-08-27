from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler
import tornado.options


class indexHandler(RequestHandler):
    def get(self):
        self.write('<h3>hello.tornado!');


if __name__ == '__main__':
    app = Application([
        ('/', indexHandler)
    ])
    app.listen(7000)
    print(f'starting... http://localhost:{7000}')

    IOLoop.current().start()
