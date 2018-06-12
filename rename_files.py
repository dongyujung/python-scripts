# Rename files in a directory using os.rename()
for path, subdir, files in os.walk(path):
    for name in files:
        if name[0] == 'M':
            os.rename(os.path.join(path, name), os.path.join(path, 'm' + name[1:]))
