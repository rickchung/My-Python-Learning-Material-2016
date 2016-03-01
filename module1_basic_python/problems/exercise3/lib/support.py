from os import listdir
import csv

def get_dir_filenames(dir_path, extension='.txt'):
    """ Get the list of filenames having <extension> in <dir_path>
    """
    return [ i for i in listdir(dir_path) if i.find(extension) > 0 ]

def get_dict(csvpath):
    """ Generate dictionary object from <csvpath>
    """
    # Load csv file
    with open(csvpath, 'r', encoding='utf-8') as fin:
        csvrows = [i for i in csv.reader(fin)]

    # Delete the header(the first row)
    csvrows.pop(0)

    name_dict = {}
    region_dict = {}
    for row in csvrows:
        # Add name
        if row[0] not in name_dict:
            name_dict[row[0]] = row[2]
        # Add region
        if row[1] not in region_dict:
            region_dict[row[1]] = row[4]

    return (name_dict, region_dict)

# This is for test
if __name__ == '__main__':
    print(get_dir_filenames('data'))
