from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Task

@receiver(pre_save, sender=Task)
def notify_on_task_status_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_task = Task.objects.get(pk=instance.pk)
    except Task.DoesNotExist:
        return

    if old_task.status != instance.status:
        subject = f"[Task Manager] Зміна статусу задачі: {instance.title}"
        message = (
            f"Ваша задача «{instance.title}» змінила статус:\n"
            f"З {old_task.status} на {instance.status}"
        )

        print(f"\n[EMAIL SIMULATION] To: {instance.owner.email}\nSubject: {subject}\n\n{message}\n")

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.owner.email],
            fail_silently=True,
        )