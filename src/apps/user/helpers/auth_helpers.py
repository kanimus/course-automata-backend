from apps.user.models import School, Auth, User


def is_school_exist(school_id):
    return School.objects.filter(id=school_id).first()


def is_user_exist(login, user_school_id, school_id):
    return User.objects.filter(login=login,
                               user_school_id=user_school_id,
                               school_id=school_id
                               ).first()


def is_auth_exist(user):
    return Auth.objects.filter(user=user).first()


def is_auth_data_exist(login, user_school_id, school_id):
    school = is_school_exist(school_id)
    user = is_user_exist(login, user_school_id, school_id)
    auth = is_auth_exist(user)
    return user, school, auth
