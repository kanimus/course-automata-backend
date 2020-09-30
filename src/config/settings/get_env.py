import os


def try_get_env(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError:
        return False


def get_env_or_default(env_name, default):
    data = try_get_env(env_name)
    if data: return data
    return default
