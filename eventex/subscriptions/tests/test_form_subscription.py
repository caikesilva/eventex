from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_form_has_field(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digits(self):
        """CPF must only accpteds digits"""
        form = self.make_validated_form(cpf='1234567AB')
        field = 'cpf'
        code = 'digits'

        self.assertFormErrorCode(form, field, code)

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        field = 'cpf'
        code = 'length'

        self.assertFormErrorCode(form, field, code)

    def test_name_must_be_captalized(self):
        """Name must be captalized"""
        form = self.make_validated_form(name='CAIKE silva')
        self.assertEqual('Caike Silva', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Email and phone are optional, but one must be informed"""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = {
            'name': 'Caike Silva',
            'cpf': '12345678901',
            'email': 'cs.caikesilva@gmail.com',
            'phone': '89-999011434'
            
        }

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form
