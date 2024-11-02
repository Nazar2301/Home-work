import inspect


def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None
    info['doc'] = obj.__doc__
    return info


number_info = introspection_info(42)
print(number_info)
