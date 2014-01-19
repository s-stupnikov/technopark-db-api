import json
import urllib
import urllib2
import urlparse
import unittest
import ConfigParser

import MySQLdb

class Configuration(object):
    def __init__(self, config_path):
        self.config = ConfigParser.SafeConfigParser()
        self.config.read(config_path)

    def get_section(self, section):
        if self.config.has_section(section):
            return dict((k, v) for k, v in self.config.items(section))


class Request(object):
    def __init__(self, url, query_args={}, post=False):
        self.url = url
        if not isinstance(query_args, dict):
            raise TypeError('Request.query_args must be dict')
        self.query_args = query_args
        self.post = post
        self.request = urllib2.Request(self.url)
        self._add_params()

    def get_response(self):
        handler = urllib2.urlopen(self.request)
        if handler.getcode() >= 300:
            raise ValueError('Request %s return code not 2xx' % self.request)
        response = handler.read()
        try:
            return json.loads(response)
        except:
            return response

    def _add_params(self):
        if not self.post:
            url_parts = list(urlparse.urlparse(self.url))
            current_query_args = urlparse.parse_qsl(url_parts[4])
            self.query_args.update(current_query_args)
            url_parts[4] = urllib.urlencode(self.query_args)
            self.url = urlparse.urlunparse(url_parts)
            self.request = urllib2.Request(self.url)
        else:
            self.request.add_data(urllib.urlencode(self.query_args))


class Database(object):
    def __init__(self, config):
        db = MySQLdb.connect(host=config['host'], user=config['user'], passwd=config['password'], db=config['database'], charset='utf8')
        self.cursor = db.cursor()

    def dictfetchall(self):
        "Returns all rows from a cursor as a dict"
        desc = self.cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in self.cursor.fetchall()
        ]

    def query(self, sql):
        self.cursor.execute(sql)
        return self.dictfetchall()

def test():
    test_conf = Configuration('/usr/local/etc/test.conf')
    assert test_conf.get_section('testing_section')['foo'] == 'bar'
    db = Database(test_conf.get_section('testing_db'))
    assert db.query('select * from engines limit 1')[0]['ENGINE'] == 'MyISAM'
    test_response = Request('http://127.0.0.1:5000/db/api/v0.1/testing_location/?one=two', query_args={'foo': 'bar'}).get_response()
    assert test_response['foo'][0] == 'bar'
    assert test_response['one'][0] == 'two'
    print 'TESTS: OK'

if __name__ == '__main__':
    test()