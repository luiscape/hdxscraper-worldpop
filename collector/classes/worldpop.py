#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
WORLDPOP CLASS:
--------------
This class defines a WorldPop repository instance.
It returns information about it, as well as a list
of datasets.

'''
import os
import json
import requests
import simplejson

class WorldPop:
  '''
  WorldPop classes. Its main methods are
  general information with info() and a list
  of datasets with datasets().

  '''
  def __init__(self):
    self.instance = 'http://www.worldpop.org.uk/getJSON/'
    self.key = os.getenv('WP_KEY')

  def info(self):
    '''
    Returns basic metadata information
    about self.

    '''
    headers = {
      'Authorization': self.key,
      'content-type': 'application/json',
      'user-agent': 'hdx-worldpop-collector/0.0.1'
      }
    request = requests.get(self.instance, headers=headers)
    metadata = {
       'instance': self.instance,
       'key': self.key,
       'success': None,
       'data': None
      }

    try:
      metadata['success'] = True
      metadata['data'] = request.json()

    except simplejson.scanner.JSONDecodeError:
      metadata['success'] = False
      metadata['data'] = request.text

    return metadata

  def datasets(self):
    '''
    Returns a list of datasets.

    '''
    datasets = []
    return datasets

