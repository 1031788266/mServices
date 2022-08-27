from tornado.web import Application

from views.cookie_v import CookieHandler
from views.index_v import IndexHandler
from views.order_v import OrderHandler
from views.search_v import SearchHandler


def main_app(host='localhost'):
    return Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<action_code>\d+)/(?P<order_id>\d+)', OrderHandler)
    ],default_host=host)