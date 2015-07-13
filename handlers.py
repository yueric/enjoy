__author__ = 'eric'
import tornado
import torndb
class indexHandler(tornado.web.RequestHandler):
    def get(self):
        db = torndb.Connection("127.0.0.1:3306","test",user="root",password="")
        sql = "SELECT * FROM enjoy ORDER BY id DESC LIMIT 18"
        rbs = db.query(sql)
       # print rbs
        self.render('index.html',rbs=rbs)

    def post(self):
        keyword=self.get_argument('keyword')
        db = torndb.Connection("127.0.0.1:3306","test",user="root",password="")
        sql = "SELECT * FROM enjoy where title like %s ORDER BY id DESC LIMIT 18"
        rbs = db.query(sql,'%'+keyword+'%')
        self.render('index.html',rbs=rbs)

class ricebookHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/rb')