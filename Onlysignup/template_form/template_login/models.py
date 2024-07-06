from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Reg(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    '''username = models.CharField(_("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    address = models.TextField(null=True)
    image = models.ImageField(upload_to="img")
    #password=models.
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]'''
    
    '''(ars) E:\django_learning\template_form>python manage.py shell
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: ars>]>
>>> User.objects.all()[0]
<User: ars>
>>> v=User.objects.all()[0]
>>> v.username
'ars'
>>> v.password
'pbkdf2_sha256$720000$0VZdRV9WaaS4JxrdiRkIpI$J1cfp9BfcxQ9xaz9LqYSD6YhA74RgIMZA9vWzBCFGog='
>>> v.first_name
'Anmol'
>>> v.email
'0211csml011@niet.co.in'
>>>'''