from django.contrib.auth.models import BaseUserManager


# Custom Base User Manager
class UserManager(BaseUserManager):
    """
    Custom Manager for custom user class
    """
    def create_user(self, email, first_name,  last_name, password=None):
        """
        Method to create user
        """
        if not email:
            raise ValueError('Please provide email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name,  last_name, password=None):
        """
        Method to create superuser which user create_user method and set the is_admin field to True
        """
        user = self.create_user(
            email=email,
            first_name = first_name,
            last_name = last_name,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
