import json
import smtplib
import requests
import urlparse
import unittest
import ConfigParser

try:
    import MySQLdb
    from pymongo import MongoClient
except ImportError:
    pass

class Configuration(object):
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = ConfigParser.SafeConfigParser()
        self.config.read(config_path)

    def get_section(self, section):
        if self.config.has_section(section):
            return dict((k, v) for k, v in self.config.items(section))
        else:
            raise ValueError("Config at %s has not section %s" % (self.config_path, section))


class Request(object):
    def __init__(self, url, query_args={}, post=False):
        if not isinstance(query_args, dict):
            raise TypeError('Request.query_args must be dict')
        self.headers = {'Content-Type': 'application/json'} if post else {}
        self.method = requests.post if post else requests.get
        self.payload = {"data": json.dumps(query_args)} if post else {"params": query_args}
        self.url = url
        self.prepared_url = url if post else requests.Request("GET", url, params=query_args).prepare().url

    def get_response(self):
        try:
            r = self.method(self.url, timeout=5, headers=self.headers, **self.payload)
        except Exception, e:
            raise ValueError('HTTP error: %s' % str(e))
        if r.status_code >= 300:
            raise ValueError('Request %s return code not 2xx: %s' % (r.url, r.status_code))
        try:
            response = r.json()
        except:
            raise ValueError('Not json response')
        if not response:
            raise ValueError('Empty response')
        if 'response' not in response or 'code' not in response:
            raise ValueError('Bad response body: response or code attribute is missing')
        if response['code'] != 0:
            return response
        if 'response' in response:
            return response['response']
        return response


class mongodb(object):
    def __init__(self, collection):
        client = MongoClient()
        db = client['db_course']
        self.collection = db[collection]

    def save(self, data):
        self.collection.save(data)
    def insert(self, data):
        self.collection.insert(data)
    def find(self, query, limit_to=0):
        return self.collection.find(query, {'quries': False}).limit(limit_to)
    def find_one(self, query):
        return self.collection.find_one(query)
    def update(self, where, fields):
        self.collection.update(where, {"$set": fields})


class Database(object):
    conn = None
    def __init__(self, config):
        self.config = config

    def connect(self):
        self.conn = MySQLdb.connect(host=self.config['host'], user=self.config['user'], passwd=self.config['password'], db=self.config['database'], charset='utf8')

    def dictfetchall(self, cursor):
        "Returns all rows from a cursor as a dict"
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    def query(self, sql):
        try:
            self.conn.ping()
        except:
            self.connect()
        finally:
            cursor = self.conn.cursor()
            cursor.execute(sql)
        return self.dictfetchall(cursor)

def sendemail(to_addr_list, subject, message):
    mail_settings = Configuration('/usr/local/etc/test.conf').get_section('mail')
    sender = mail_settings['login']
    header  = 'From: %s\n' % sender
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    smtp_serv = 'smtp.mail.ru'
    smtp_port = 465
    server = smtplib.SMTP_SSL(smtp_serv, smtp_port)
    server.login(sender, mail_settings['password'])
    problems = server.sendmail(sender, to_addr_list, message)
    server.quit()


def test():
    test_conf = Configuration('/usr/local/etc/test.conf')
    assert test_conf.get_section('testing_section')['foo'] == 'bar'
    db = Database(test_conf.get_section('testing_db'))
    assert db.query('select * from engines limit 1')[0]['ENGINE'] == 'MyISAM'
    test_response = Request('http://127.0.0.1:5000/db/api/1/testing_location/?one=two', query_args={'foo': 'bar'}).get_response()
    assert test_response['foo'][0] == 'bar'
    assert test_response['one'][0] == 'two'
    sendemail(to_addr_list=('s.stupnikov@corp.mail.ru',), subject='Hello', message='World')
    print 'TESTS: OK'

if __name__ == '__main__':
    test()