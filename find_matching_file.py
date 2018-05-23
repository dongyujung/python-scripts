def find_matching_file(pattern, path):
    """
    Find file within the path that starts with pattern
    """
    for dir_name, subdir_list, file_list in os.walk(path):
        for each_file in file_list:
            if re.match(pattern, each_file):
                return os.path.join(path, each_file)
