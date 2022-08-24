from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Caike Silva",
            cpf="12345678901",
            email="kaykesilva2014.ks@gmail.com",
            phone="89-999011434"
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have on auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Caike Silva', str(self.obj))

    