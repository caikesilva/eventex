from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name="Caike Da Silva Reis",
            email="cs.caikesilva@gmail.com",
            cpf="12345678901",
            phone="89-99011434"
        )

        self.response = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf,
                    self.obj.email, self.obj.phone
        )
        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, response.status_code)
