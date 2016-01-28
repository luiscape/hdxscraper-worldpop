#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
COLLECTOR:
---------
Here includes the main part of the collector program.
We list all the contents from the WorldPop repository and
proceed to instantiate its results.

'''
from collector.parser import parse_dataset

from collector.utilities.item import item
from collector.utilities.export import export_json

from collector.classes.worldpop import WorldPop

def main():
    '''
    Program wrapper.

    '''
    contents = WorldPop().info()

    #
    #  Collects data and organizes
    #  in lists and dictionaries.
    #
    datasets = []
    resources = []
    for dataset in contents['data']['worldPopData']:
        d = parse_dataset(dataset)
        if d is not None:
            datasets.append(d['metadata'])
            resources.append(d['resource'])

    export_json(datasets, 'data/datasets.json')
    export_json(resources, 'data/resources.json')
    print('%s Total datasets downloaded %s' % (item('success'), str(len(datasets))))


if __name__ == '__main__':
    main()
