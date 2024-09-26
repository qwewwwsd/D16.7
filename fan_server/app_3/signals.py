from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Response, Post, User


@receiver(post_save, sender=Post)
def post_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.all().values_list('email', flat=True)
    subject = f'Новое объявление {instance.title}'
    text_content = (
        f'Добавлено новое Объявление в категории: {instance.category}\n'
        f'Ссылка на объявление: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.send()


@receiver(pre_save, sender=Response)
def handler(sender, instance, **kwargs):

    if instance.status:
        mail = instance.author.email
        send_mail(
            subject='',
            message=f' ваш отклик на {instance.post} принят',
            recipient_list=[mail],
            from_email=None,
            fail_silently=False,
        )
    else:
        mail = instance.post.author.email
        send_mail(
            subject='',
            message=f'На вашу публикацию {instance.post} пришёл отклик! от {instance.author}',
            recipient_list=[mail],
            from_email=None,
            fail_silently=False,
        )
