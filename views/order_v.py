from tornado.web import RequestHandler


class OrderHandler(RequestHandler):

    def initialize(self):
        self.write('-----initialize-----</br>')

    def prepare(self):
        self.write('-----prepare-----</br>')

    product = [
        {
            'id': 1,
            'name': '西红柿炒番茄',
            'price': 20,
            'count': 100
        },
        {
            'id': 2,
            'name': '扬州炒饭',
            'price': 14,
            'count': 200
        },
        {
            'id': 3,
            'name': '炸鸡饭',
            'price': 15,
            'count': 123
        }
    ]

    action = {
        1: '取消',
        2: '评价',
        3: '购买'
    }

    def query(self, order_id):
        for item in self.product:
            if item.get('id') == order_id:
                return item


    def get(self, order_id, action_code):
        self.write('订单查询</br>')
        order = self.query(int(order_id))
        if order and self.action.get(int(action_code)):
            self.write('商品编号: %s</br>' % order.get('id'))
            self.write('商品编号: %s</br>' % order.get('name'))
            self.write('商品编号: %s</br>' % order.get('price'))
            self.write('商品编号: %s</br>' % order.get('count'))
            self.write('商品状态: %s</br>' % self.action.get(int(action_code)))
        else:
            self.write('<h3 style="color:red;">查询失败</h3>')