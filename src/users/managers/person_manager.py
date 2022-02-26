import uuid
from typing import Union
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager


class PersonManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not email:
            raise ValueError(_('The given email must be set'))
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # """Create and save a regular User with the given phone and password."""
        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_superuser', False)
        # return self._create_user(phone, password, **extra_fields)
        if not email:
            raise ValueError(_('The given email must be set'))
        user = self.model(email=email, **extra_fields)
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        #
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')
        #
        # return self._create_user(phone, password, **extra_fields)

        if not email:
            raise ValueError(_('The given phone must be set'))
        user = self.model(email=email, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def load_by_id(self, id: Union[uuid.uuid4, str]):  # pylint: disable=no-self-use,redefined-builtin
        return super().filter(id=id).first()
