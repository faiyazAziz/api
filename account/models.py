from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
import uuid


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name,tc, password=None,password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,tc, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=60)
    bio = models.CharField(max_length=500,blank=True,null=True)
    profile_url = models.CharField(default="https://firebasestorage.googleapis.com/v0/b/social-2f752.appspot.com/o/profile_pics%2Fdefault_profile_pic.png?alt=media&token=78bff1b3-b8c5-497d-a4d5-831f8c5e8360",max_length=600)
    following = models.ManyToManyField('self',symmetrical=False,related_name='follower',blank=True)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","tc"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    description = models.CharField(max_length=200)
    post_url = models.CharField(max_length=600,default="default")
    type = models.CharField(default="image",max_length=250)
    time_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)



