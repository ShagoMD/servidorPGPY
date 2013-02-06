#!/usr/bin/python
import os
os.chdir("C:/Users/Eric/Favorites/Documents/Eclipse Projects/servidorPGPY")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from publicidadGeolocalizada.models import *
from django.contrib.auth.models import User


from django.db import transaction
transaction.rollback()
from django.db import connection
connection._rollback()


usuarioTest = User.objects.create_user('pokachu', 'rikrdoxweb_ass@hotmail.com', '123456')
usuarioTest.is_staff = True

print usuarioTest.get_full_name()


usuarioTest.save