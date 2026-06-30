from django.contrib.auth.backends import ModelBackend

from .models import User


class EmailBackend(ModelBackend):

    def authenticate(
        self,
        request,
        username=None,
        password=None,
        email=None,
        **kwargs
    ):

        email = email or username

        if email is None:
            return None

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None