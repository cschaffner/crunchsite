from django.contrib.auth.backends import ModelBackend
from models import Person


class MyModelBackend(ModelBackend):
    """
    My own authentication back-end according to
    https://docs.djangoproject.com/en/1.6/topics/auth/customizing/#authentication-backends
    and
    http://docs.django-cms.org/en/3.0.3/extending_cms/placeholders.html

    This allows to handle extra user permissions such as verifying if somebody is allowed to edit
    a cms placeholder
    """
    def has_perm(self, user_obj, perm, obj=None):
        assert isinstance(user_obj.is_active, object)
        if not user_obj.is_active:
            return False
        if isinstance(obj, Person):
            # allows to edit a placeholder only if obj is the Person that belongs to the user_obj
            if user_obj.profile == obj:
                return True
        return perm in self.get_all_permissions(user_obj, obj)
