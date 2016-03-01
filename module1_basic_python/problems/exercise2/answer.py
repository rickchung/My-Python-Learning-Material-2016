from lib.support import get_dir_filenames, get_dict

# Test Code
filenames = get_dir_filenames('data')
print(filenames)

name_dict, region_dict = get_dict('csv_data/clean_votes.csv')
print(name_dict['1'])
print(region_dict['710001200000000'])

# Write your answer below