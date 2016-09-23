from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscrptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name='Diego Ubirajara',
                cpf='12345678901',
                email='diego@ubirajara.com',
                phone='626556608'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subcription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Diego Ubirajara', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must be False"""
        self.assertEqual(False, self.obj.paid)
