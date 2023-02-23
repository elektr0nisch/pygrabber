#!/usr/bin/python3
import yaml
import sys

with open('config.yml') as file:
    config = yaml.load(file)

sys.path.insert(0, config['app.working_directory'])

from pygrabber import app as application