from tornado.web import RequestHandler
import json

class SearchHandler(RequestHandler):
    def get(self):
        self.mapper = {
            'python': 'I\'m is Python!',
            'java': 'I\'m is Java!',
            'javascript': 'I\'m is javascript!'
        }

        html = """
            <h1>搜索%s结果</h1>
            <span>%s</span>
        """

        wd = self.get_query_argument('wd')
        data = {
            'wd': wd,
            'result': self.mapper.get(wd)
        }
        self.write(json.dumps(data))
        self.set_status(200)
        self.set_header('Content-Type', 'application/json;charset=utf-8')
        self.set_cookie('user_role', 'admin')