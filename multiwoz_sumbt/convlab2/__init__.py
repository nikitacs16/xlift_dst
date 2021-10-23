import os

from convlab2.dst import DST


from os.path import abspath, dirname


def get_root_path():
    return dirname(dirname(abspath(__file__)))


DATA_ROOT = os.path.join(get_root_path(), 'data')
