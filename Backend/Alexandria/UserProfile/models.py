from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return super().create_user(email, password, **extra_fields)

class UserAlexandria(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, verbose_name="Имя", default='default_value')
    surname = models.CharField(max_length=50, verbose_name="Фамилия", null=True, blank=True)
    fathername = models.CharField(max_length=50, verbose_name="Отчество", null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name="E-mail")
    birth_date = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=50, verbose_name="Usename", null=True, blank=True)

    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class AdditionalInfoUA(models.Model):
    user = models.OneToOneField(UserAlexandria, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    money = models.IntegerField(default=0)

class Friendship(models.Model):
    from_user = models.ForeignKey(UserAlexandria, on_delete=models.CASCADE, related_name='from_user') 
    to_user = models.ForeignKey(UserAlexandria, on_delete=models.CASCADE, related_name='to_user')
    created_at = models.DateTimeField(auto_now_add=True)

class Messages(models.Model):
    content = models.TextField(max_length=1000, verbose_name="Сообщение")
    author = models.ForeignKey(UserAlexandria, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)

class Chats(models.Model):
    participants = models.ManyToManyField(UserAlexandria, related_name='chats')
    messages = models.ManyToManyField(Messages, blank=True)
