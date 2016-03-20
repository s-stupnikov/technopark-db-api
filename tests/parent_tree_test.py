import unittest
import itertools
from mock import MagicMock

from func_test import EntitiesList, ThreadActor, log, TestLog


class TestParentTree(unittest.TestCase):
  params = {
     'since': '2014-01-01 00:00:00',
     'sort' : 'parent_tree',
     'limit': 2,
     'order' : 'asc'
  },
  
  objects = [
  
     {'date': '2014-11-04 15:39:58',
     'dislikes': 0,
     'forum': 'forum1',
     'id': 27,
     'isApproved': True,
     'isDeleted': False,
     'isEdited': False,
     'isHighlighted': False,
     'isSpam': False,
     'likes': 0,
     'message': 'my message 0my message 0my message 0my message 0my message 0my message 0my message 0my message 0my message 0my message 0',
     'parent': None,
     'points': 0,
     'thread': 4,
     'user': 'example4@mail.ru'},

    {'date': '2016-03-17 23:01:12',
     'dislikes': 0,
     'forum': 'forum1',
     'id': 31,
     'isApproved': False,
     'isDeleted': False,
     'isEdited': False,
     'isHighlighted': True,
     'isSpam': True,
     'likes': 0,
     'message': 'my message 4my message 4my message 4my message 4my message 4my message 4my message 4my message 4my message 4my message 4my message 4my message 4my message 4my message 4my message 4',
     'parent': 27,
     'points': 0,
     'thread': 4,
     'user': 'example3@mail.ru'},
               
    {'date': '2016-03-18 12:22:21',
     'dislikes': 0,
     'forum': 'forum1',
     'id': 32,
     'isApproved': True,
     'isDeleted': False,
     'isEdited': True,
     'isHighlighted': True,
     'isSpam': True,
     'likes': 0,
     'message': 'my message 5my message 5my message 5my message 5my message 5my message 5my message 5my message 5my message 5my message 5my message 5my message 5my message 5my message 5my message 5my message 5',
     'parent': 31,
     'points': 0,
     'thread': 4,
     'user': 'example3@mail.ru'},

    {'date': '2016-03-18 08:42:47',
     'dislikes': 0,
     'forum': 'forum1',
     'id': 34,
     'isApproved': True,
     'isDeleted': False,
     'isEdited': True,
     'isHighlighted': False,
     'isSpam': True,
     'likes': 0,
     'message': 'my message 7my message 7my message 7my message 7my message 7my message 7my message 7my message 7my message 7my message 7',
     'parent': 27,
     'points': 0,
     'thread': 4,
     'user': 'example3@mail.ru'},

    {'date': '2015-07-28 09:39:01',
     'dislikes': 0,
     'forum': 'forum1',
     'id': 28,
     'isApproved': False,
     'isDeleted': False,
     'isEdited': False,
     'isHighlighted': True,
     'isSpam': True,
     'likes': 0,
     'message': 'my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1my message 1',
     'parent': None,
     'points': 0,
     'thread': 4,
     'user': 'example@mail.ru'}
  ]
  
  def setUp(self):
      def validate_list(test_obj_list, api_obj_list):
          self.assertEqual(len(api_obj_list), len(test_obj_list))
          for test_obj, api_obj in itertools.izip_longest(test_obj_list, api_obj_list):
              self.assertEqual(test_obj, api_obj)

      def print_beauty(objects):
          for obj in objects:
              print obj
      self.thread_actor = ThreadActor('127.0.0.1:8000')
      self.thread_actor.query_api = MagicMock(return_value=self.objects)
      self.thread_actor._get_api_location = MagicMock(return_value='test')
      self.thread_actor.validate_list = validate_list
      self.elist = EntitiesList([self.thread_actor._create_from_dict(obj_dict, new_type='post') for obj_dict in self.objects],
                                **self.params[0])
      print_beauty(self.elist.objects)

        
  def test_sort(self):
      self.thread_actor.list_posts(self.params, self.elist.objects)


if __name__ == '__main__':
    unittest.main()
    


             
