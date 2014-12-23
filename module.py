namespace = {
    'load_count': 0
}


def load():
    namespace['load_count'] = namespace['load_count'] + 1
    return namespace['load_count']
