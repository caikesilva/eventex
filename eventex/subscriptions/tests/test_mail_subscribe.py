from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(
            name="Caike Silva",
            cpf="12345678901",
            email="cs.caikesilva@gmail.com",
            phone="89999011434"
        )
        self.client.post(
            r('subscriptions:new'),
            data
        )
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        
        expect = 'kaykesilva2014.ks@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        
        expect = ['kaykesilva2014.ks@gmail.com', 'cs.caikesilva@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Caike Silva',
            '12345678901',
            'cs.caikesilva@gmail.com',
            '89999011434'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

