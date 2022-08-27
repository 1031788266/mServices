from app import main_app
import tornado.ioloop
import tornado.options




if __name__ == '__main__':
    tornado.options.define('port', default=54321, type=int, help="bind port")
    tornado.options.define('host', default='127.0.0.1', type=str, help='bind addr')

    tornado.options.parse_command_line()

    app = main_app(tornado.options.options.host)
    app.listen(tornado.options.options.port)
    print(f'tornado service start... http://127.0.0.1:{tornado.options.options.port}')
    tornado.ioloop.IOLoop.current().start()
