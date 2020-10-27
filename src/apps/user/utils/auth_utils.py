from apps.user.models import School, User, Auth


def is_school_exist(school_id):
    return School.objects.filter(id=school_id).first()


def is_auth_exist(login, user_school_id, school_id):  # TODO: Maybe needs check password for user
    return Auth.objects.filter(login=login,
                               user_school_id=user_school_id,
                               school_id=school_id
                               ).first()


def is_user_exist(auth):
    return auth.user if auth else None
    # return User.objects.filter(auth=auth).first()


def is_auth_data_exist(login, user_school_id, school_id):
    school = is_school_exist(school_id)
    auth = is_auth_exist(login, user_school_id, school_id)
    user = is_user_exist(auth)
    return user, school, auth
