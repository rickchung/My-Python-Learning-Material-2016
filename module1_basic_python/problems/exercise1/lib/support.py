from os import listdir

def get_dir_filenames(dir_path, extension='.txt'):
    """ Get the list of filenames having <extension> in <dir_path>
    """
    return [ i for i in listdir(dir_path) if i.find(extension) > 0 ]

# This is for test
if __name__ == '__main__':
    print(get_dir_filenames('data'))
