from glob import glob
import os
import re

old_pattern = './data/old/USGS_13_*.tif'
old_paths = list(glob(old_pattern))
print(old_paths)

print('Found {} files'.format(len(old_paths)))


for old_path in sorted(old_paths):
    print(old_path)
    folder = os.path.dirname(old_path)
    old_filename = os.path.basename(old_path)

    # Extract northing.
    res = re.search(r'([ns]\d\d)', old_filename)
    old_northing = res.groups()[0]

    # Fix the NS 
    n_or_s = old_northing[0]
    ns_value = int(old_northing[1:3])
    if old_northing[:3] == 'n00':
        new_northing = 's01' + old_northing[3:]
    elif n_or_s == 'n':
        new_northing = 'n' + str(ns_value - 1).zfill(2) + old_northing[3:]
    elif n_or_s == 's':
        new_northing = 's' + str(ns_value + 1).zfill(2) + old_northing[3:]
    new_filename = old_filename.replace(old_northing, new_northing)
    assert new_northing in new_filename

    # Rename in place.
    new_path = os.path.join(folder, new_filename)
    os.rename(old_path, new_path)
