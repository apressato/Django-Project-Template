from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import md5
from django.utils.safestring import mark_safe
from django.conf import settings
import collections
from itertools import groupby
import uuid
from django.db.models.deletion import CASCADE, SET_NULL
from .utilities import secure_upload_filename
from ckeditor.fields import RichTextField
import logging

# Create your models here.


class Roles(models.Model):
    Role_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Name = models.CharField(max_length=100, unique=True, null=False, blank=True)
    Description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name


class ExtendedUser(AbstractUser):
    profile_image = models.ImageField(max_length=500, upload_to=secure_upload_filename, verbose_name="Profilo Avatar",
                                      blank=True, null=True, default=settings.DEFAULT_PROFILE_PIC)
    UseGravatar = models.BooleanField(default=False, verbose_name="Use Gravatar")
    Short_Intro = RichTextField(blank=True, null=True, verbose_name="Short Intro")
    Social_LinkedIn = models.URLField(max_length=500, blank=True, verbose_name="LinkedIn")
    Social_Instagram = models.URLField(max_length=500, blank=True, verbose_name="Instagram")
    Social_facebook = models.URLField(max_length=500, blank=True, verbose_name="Facebook")
    CultureId = models.CharField(max_length=150,
                                 blank=False,
                                 choices=(('it_IT', 'it_IT'),
                                          ('en_US', 'en_US'),
                                          ('fr_FR', 'fr_FR')),
                                 default='en_US', verbose_name="Language Culture")
    Screen_scale = models.IntegerField(blank=False,
                                    choices=((100, '100%'),
                                             (125, '125%'),
                                             (150, '150%'),
                                             (175, '175%')),
                                    default=100, verbose_name="Screen Scale")
    roles = models.ManyToManyField(Roles, blank=True, verbose_name="Roles")

    def gravatar_url(self, size=80):
        return "http://www.gravatar.com/avatar/%s?d=identicon&s=%d" % \
               (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)

    def image_tag(self):
        imagefile = self.get_ProfileImage
        return mark_safe('<img src="%s" width="150" height="150" />' % imagefile)

    @property
    def get_roles(self):
        result = []
        for role in self.roles.all():
            result.append(role.Name)
        return result

    @property
    def get_ProfileImage(self, size=80):
        try:
            url = self.profile_image.url
            logging.warning(f"{url=}")
        except:
            url = settings.DEFAULT_PROFILE_PIC

        if settings.DEFAULT_PROFILE_PIC in url and self.UseGravatar:
            url = self.gravatar_url(size)
        return url

    def has_role(self, RoleName):
        RolesList = []
        for role in self.roles.all():
            RolesList.append(role.Name)
        return RoleName in RolesList

    def __repr__(self):
        return f"{self.get_full_name} ({self.email})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
