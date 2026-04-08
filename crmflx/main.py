from importlib.resources import files, as_file
from . import _model_data


_resources = files(_model_data)

def first_line(filename):
    _file_traversable = _resources.joinpath(filename)
    with as_file(_file_traversable) as _path:
        with open(_path) as f:
            line = f.readline()
    return line