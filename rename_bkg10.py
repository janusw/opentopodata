#!/usr/bin/python3
from glob import glob
import os
import re

old_pattern = './data/bkg-dgm10/dgm10_32*_*_20.tif'
old_paths = list(glob(old_pattern))
print('Found {} files'.format(len(old_paths)))

for old_path in old_paths:
    folder = os.path.dirname(old_path)
    old_filename = os.path.basename(old_path)

    # Extract north and east coords, pad with zeroes.
    res = re.search(r'32(\d\d\d)_(\d\d\d\d)_20', old_filename)
    easting, northing = res.groups()
    northing = 'N' + northing + '000'
    easting = 'E' + easting + '000'

    # Rename in place.
    new_filename = '{}{}.tif'.format(northing, easting)
    #print('old: {}, new: {}'.format(old_filename, new_filename))
    new_path = os.path.join(folder, new_filename)
    os.rename(old_path, new_path)
