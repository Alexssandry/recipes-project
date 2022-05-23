from authors.forms import RegisterForm
from django.test import TestCase


class AuthorRegisterFormUnitTest(TestCase):
    def test_first_name_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['first_name'].field.widget.attrs['placeholder']

        # placeholder == 'Ex.: Alexssandry'
        self.assertEqual('Ex.: Alexssandry', placeholder)

    def test_last_name_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['last_name'].field.widget.attrs['placeholder']
        # placeholder == 'Ex.: Pereira'
        self.assertEqual('Ex.: Pereira', placeholder)

    def test_username_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['username'].field.widget.attrs['placeholder']

        # placeholder == 'Type your username here. Ex.: alexssandry.pereira'
        self.assertEqual(
            'Type your username here. Ex.: alexssandry.pereira', placeholder)

    def test_email_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['email'].field.widget.attrs['placeholder']
        # placeholder == 'Ex.: alexssandry.pereira@teste.django.com'
        self.assertEqual(
            'Ex.: alexssandry.pereira@teste.django.com', placeholder)

    def test_password_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['password'].field.widget.attrs['placeholder']
        # placeholder == 'Type your password here'
        self.assertEqual('Type your password here', placeholder)

    def test_password2_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['password2'].field.widget.attrs['placeholder']
        # placeholder == 'Repeat your password here'
        self.assertEqual('Repeat your password here', placeholder)

    def test_email_help_test_is_correct(self):
        form = RegisterForm()
        help_text = form['email'].field.help_text
        # help_text == 'The e-mail must be valid.'
        self.assertEqual(help_text, 'The e-mail must be valid.')

    def test_password2_help_test_is_correct(self):
        form = RegisterForm()
        help_text = form['password2'].field.help_text
        # help_text == 'Repeat your password here.'
        self.assertEqual(help_text, 'Repeat your password here.')
