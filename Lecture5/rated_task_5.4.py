"""
def file_search(folder, file):
    path = str(folder[0]) + '/'
    if folder.count(file) == 1:
        return path + file
    else:
        for element in folder:
            if isinstance(element, list) and len(element)>1:
                print len(element)
                new_path = file_search(element, file)
                print 'new_path =', new_path
                path += str(new_path)
                return path
    if path == path:
        return False
    else:
        return path
"""
def file_search(folder, filename):
    if folder == filename:
        return filename
    else:
        if isinstance(folder, list):
            if folder[0] == filename:
                return filename
            for i in folder[1:]:
                print '  CHECK  '
                path = file_search(i, filename)
                print path
                if isinstance(path, str):
                    return folder[0] + '/' + path
            return False
        else:
            return False






print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
print '___________-------------__________'
print file_search(['C:', ['backup.log', 'vasya_pupki', ['mydearlove', 'ideas.txt', 'beach']], 'nope'], 'ideas.txt')
print '___________-------------__________'
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
