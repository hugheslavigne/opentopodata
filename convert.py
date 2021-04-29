from glob import glob
import os
import re

old_pattern = './data/ned10m/USGS_13_*.tif'
old_paths = list(glob(old_pattern))
print('Found {} files'.format(len(old_paths)))

for old_path in old_paths:
    folder = os.path.dirname(old_path)
    filename = os.path.basename(old_path)
    prefix = filename[0:8]

    # Fix the NS 
    n_or_s = filename[8]
    ns_value = int(filename[9:11])
    if filename[8:11] == 'n00':
        filename = prefix + 's01' + filename[12:]
    elif n_or_s == 'n':
        filename = prefix + 'n' + str(ns_value - 1).zfill(2) + filename[11:]
    elif n_or_s == 's':
        filename = prefix + 's' + str(ns_value + 1).zfill(2) + filename[11:]


    # Rename in place.
    new_path = os.path.join(folder, filename)
    os.rename(old_path, new_path)
