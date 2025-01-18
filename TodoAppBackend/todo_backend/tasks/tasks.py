from celery import shared_task
from django.core.mail import send_mail
from .models import Task
from datetime import datetime

@shared_task
def send_task_reminder(task_id):
    task = Task.objects.get(id=task_id)
    if task.deadline < datetime.now():
        send_mail(
            'Task Reminder',
            f'Remember to complete your task: {task.title}',
            'from@example.com',
            [task.user.email],
        )
