from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.core.exceptions import ValidationError


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Caike Silva',
            slug='caike-silva',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker = self.speaker,
            kind = Contact.EMAIL,
            value = 'cs.caikesilva@gmail.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker = self.speaker,
            kind = Contact.PHONE,
            value = '89999011434'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact.objects.create(
            speaker = self.speaker,
            kind = 'A',
            value = 'B'
        )

        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker = self.speaker,
            kind = Contact.EMAIL,
            value = 'cs.caikesilva@gmail.com'
        )
        self.assertEqual('cs.caikesilva@gmail.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Caike Silva',
            slug='caike-silva',
            photo='http://hbn.link/hb-pic'
        )

        s.contact_set.create(
            kind = Contact.EMAIL,
            value = 'cs.caikesilva@gmail.com'
        )

        s.contact_set.create(
            kind = Contact.PHONE,
            value = '89999011434'
        )

    def test_email(self):
        qs = Contact.objects.emails()
        expected = ['cs.caikesilva@gmail.com']

        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phone(self):
        qs = Contact.objects.phones()
        expected = ['89999011434']

        self.assertQuerysetEqual(qs, expected, lambda o: o.value)