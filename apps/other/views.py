from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.users.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.other.models import Expectation, Partner, SMI, B2B, News
from apps.other.serializers import ExpectationSerializer, PartnerSerializer, SMISerializer, B2BSerializer, NewsSerializer


class ExpectationView(ListAPIView):
    queryset = Expectation.objects.all()
    serializer_class = ExpectationSerializer


class PartnerView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class SMIView(ListAPIView):
    queryset = SMI.objects.all()
    serializer_class = SMISerializer


class B2BView(ListAPIView):
    queryset = B2B.objects.all()
    serializer_class = B2BSerializer


class NewsView(ListAPIView, RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@receiver(post_save, sender=News)
def send_notification_email(sender, instance, created, **kwargs):
    # Если новость только что создана, отправьте сообщение на почту всем пользователям
    if created:
        users = User.objects.all()

        subject = 'Новость: ' + instance.title
        message = 'Новость: {}\nОписание: {}\nДата: {}'.format(instance.title, instance.description, instance.date)

        for user in users:
            send_mail(subject, message, 'Info@hit-expo.org', [user.email])
