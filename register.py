#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
REGISTER:
---------

Caller script. Designed to call all other functions
that register, update, or delete datasets in HDX.

'''
import os
import sys
import json
import requests
import scraperwiki
import progressbar as pb

from termcolor import colored as color
from collector.utilities.item import item as I

from hdx_register import load, delete, create
from collector.utilities.load import load_config


def main():
  '''Wrapper'''

  #
  # Setting up configuration: dev = development; prod = production.
  #
  p = load_config('config/config.json')
  if p is not False:

    print('--------------------------------------------------')
    print('%s HDX Site: %s' % (I('bullet'), p['hdx_site']))

    #
    # Deleting all datasets from org.
    #
    if p['delete_datasets']:
      try:
        delete.delete_all_datasets_from_organization(organization='un-operational-satellite-appplications-programme-unosat', hdx_site=p['hdx_site'], apikey=p['hdx_key'], verbose=p['verbose'])

      except Exception as e:
        print(e)
        return False

    try:
      #
      # Loading JSON data.
      #
      dataset_dict = load.load_data(os.path.join(p['json_folder'], 'datasets.json'))
      resource_dict = load.load_data(os.path.join(p['json_folder'], 'resources.json'))
      # gallery_dict = load.load_data(os.path.join(p['json_folder'], 'gallery.json'))

      # Delete resources before running:
      if p['delete_resources']:
        delete.delete_resources(dataset_dict=dataset_dict, hdx_site=p['hdx_site'], apikey=p['hdx_key'], verbose=p['verbose'])

      if p['update_all_datasets']:
        print('--------------------------------------------------')
        print(color(u" ATTENTION:", "blue", attrs=['bold']) + ' Updating ALL datasets.')
        print('--------------------------------------------------')

      #
      # Create datasets, resources, and gallery items.
      #
      create.create_datasets(dataset_dict=dataset_dict, hdx_site=p['hdx_site'], apikey=os.getenv('HDX_KEY'), verbose=p['verbose'], update_all_datasets=p['update_all_datasets'])
      create.create_resources(resource_dict=resource_dict, hdx_site=p['hdx_site'], apikey=os.getenv('HDX_KEY'), verbose=p['verbose'], update_all_datasets=p['update_all_datasets'])
      # create.create_datasets(gallery_dict=gallery_dict, hdx_site=p['hdx_site'], apikey=os.getenv('HDX_KEY'), verbose=p['verbose'], update_all_datasets=p['update_all_datasets'])

    except Exception as e:
      print(e)
      return False


if __name__ == '__main__':

  if main() != False:
    print('%s IFPRI scraper finished successfully.\n' % I('success'))
    scraperwiki.status('ok')

  else:
    scraperwiki.status('error', 'Failed to register resources.')
    os.system("mail -s 'IFPRI scraper collector failed' luiscape@gmail.com")
