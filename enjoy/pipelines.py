# -*- coding: utf-8 -*-

from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request

import MySQLdb
import MySQLdb.cursors

class EnjoyPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db = 'test',
                user = 'root',
                passwd = '',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = False
        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        #print item
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self,tx,item):
        if(item):
            print "================================"+item['url']
            tx.execute("select * from enjoy where url= %s",(item['url'],))
            result=tx.fetchone()
            log.msg(result,level=log.DEBUG)
            #print result
            if result:
                log.msg("Item already stored in db:%s" % item,level=log.DEBUG)
            else:
                type = ''
                if(item['type']):
                    type = item['type'][0]

                tx.execute(\
                "insert into enjoy (title,type,descp,price,unit,address,tel,url,purl,close,pdate) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())",\
                (item['title'][0],type,item['desc'][0],item['price'][0],item['unit'][0],item['address'][0],item['tel'][0],item['url'],item['purl'][0],item['close']))
               # log.msg("Item stored in db: %s" % item, level=log.DEBUG)
        else:
            log.meg("Item null!")

    def handle_error(self, e):
        log.err(e)