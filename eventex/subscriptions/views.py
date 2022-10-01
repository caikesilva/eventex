from eventex.subscriptions.mixins import EmailCreateMixin
from eventex.subscriptions.models import Subscription
from .forms import SubscriptionForm
from django.views.generic import DetailView
from django.views.generic import CreateView


class EmailCreateView(EmailCreateMixin, CreateView): 
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object = form.save()
        self.send_mail()
        return response

new = EmailCreateView.as_view(
                            model=Subscription,
                            form_class = SubscriptionForm,
                            email_subject = 'Confirmação de inscrição'
                            )

detail = DetailView.as_view(model=Subscription)