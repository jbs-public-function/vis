import pickle
from functools import wraps

def pickle_data(func):
    """
    Guys, I'm getting into wrappers, now!
    In the spirit of this repo, I do this a lot and will probably continue to do so. 
    Adding this bad boy to the code base
    
    given a list of tags-['x', 'y', 'z'], a format string 'my_file_{}.pkl' and a pathlib Path object
    load all the data and return as a dict[tag_0] = 
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        datapath = kwargs.get('datapath')
        file_format = kwargs.get('file_format')
        tags = kwargs.get('tags')
        data = []
        for t in tags:
            with datapath.joinpath(file_format.format(t)).open('rb') as f:
                data.append([t, pickle.load(f)])
        kwargs.update(dict(data=data))
        return func(*args, **kwargs)
    
    return wrapper
