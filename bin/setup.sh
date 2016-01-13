#!/bin/bash

#
#  Setting up virtual environment
#  and dependencies.
#
virtualenv --python=python3.4 venv
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt

#
#  Creating data folder.
#
mkdir data
