import os

# Each website you crawl is a separate project (folder)

def create_project_dir (directory):
    if not os.path.exists (directory):
        print ('Creating project ' + directory)
        os.makedirs (directory)

# Create queue and crawled files (if not created)
def create_data_files (project_name):
    queue = 'TennisPlayers.txt'
    data_storage = project_name + '/storage.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile (crawled):
        write_file (crawled, '')

    if not os.path.isfile(data_storage):
        write_file(data_storage, '')


# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
    #if not os.path.isfile (crawled):

# Delete the contents of a file
def delete_file_content (path):
    with open (path, 'w'):
        pass

# Read a file and convert each line to set items
def file_to_set (file_name):
    results = set ()

    with open (file_name, 'rt') as f:
        for line in f:
            results.add (line.replace ('\n', ''))

    return results

# Iterate through a set, each item will be a new line in the file
def set_to_file (links, file):
    delete_file_content (file)

    for link in sorted (links):
        append_to_file (file, link)