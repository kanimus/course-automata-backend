import json
import os

from apps.user.models import School
from config.settings import PATTERNS_DIR, SCHOOLS_DIR


def _get_json(path):
    try:
        with open(path) as f:
            data = json.load(f)
            return data
    except IOError:
        return None


def get_patterns_or_none():
    return _get_json(PATTERNS_DIR)


def get_school_config_or_none(school_id):
    school =  School.objects.filter(id=school_id).first()
    if not school:
        return None
    dir = os.path.join(SCHOOLS_DIR, school.short_name, 'config.json')
    return _get_json(dir)
