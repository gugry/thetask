from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User


class SomeTests(TestCase):

    def some_test(self):
        superusers_emails = User.objects.filter(is_superuser=True).values_list('email')
        self.assertEqual(len(superusers_emails) > 0, True)



