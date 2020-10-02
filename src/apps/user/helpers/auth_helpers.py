from apps.user.models import School
from config.settings.settings import AUTH_USER_MODEL


def is_school_exist(school_id):
    return School.objects.filter(id=school_id).first()

def is_user_exist(login, user_school_id, school_id):
    return AUTH_USER_MODEL.objects.filter(login=login,
                                          user_school_id=user_school_id,
                                          school_id=school_id
                                          ).first()

def is_auth_data_exist(login, user_school_id, school_id, user_id, auth=None):
    school = is_school_exist(school_id)
    user = is_user_exist(login, user_school_id, school_id)
    return user, school