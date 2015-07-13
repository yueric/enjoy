__author__ = 'eric'

import os
import tornado.web
import tornado.ioloop
from handlers import *
handlers=[
    (r'/',indexHandler)
    ]

settings={
    'static_path':os.path.join(os.path.dirname(__file__),'static'),
    'template_path':os.path.join(os.path.dirname(__file__),'template'),
}

app=tornado.web.Application(handlers,**settings)
app.listen(8888)
tornado.ioloop.IOLoop.instance().start()