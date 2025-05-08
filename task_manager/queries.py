import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject_test.settings')
django.setup()

from django.db.models import Q, F, Count
from django.db.models.functions import ExtractWeekDay, ExtractDay
from django.utils import timezone
from datetime import timedelta

from task_manager.models import Task, SubTask

today = timezone.now()


# new_task = Task.objects.create(
#     title="Prepare presentation",
#     description="Prepare materials and slides for the presentation",
#     status="New",
#     deadline=(today + timedelta(days=3))
# ).id
#
# SubTask.objects.bulk_create([
#     SubTask(
#         title="Gather information",
#         description="Find necessary information for the presentation",
#         status="New",
#         deadline=(today + timedelta(days=2)),
#         task_id=new_task),
#
#     SubTask(
#         title="Create slides",
#         description="Create presentation slides",
#         status="New",
#         deadline=(today + timedelta(days=1)),
#         task_id=new_task
#     )
# ])

tasks_with_status_new = Task.objects.filter(status="New")
for task in tasks_with_status_new:
    print(f"{task.title=},{task.status=},{task.deadline=}")


all_subtasks_done = SubTask.objects.filter(
    Q(status="Done") & Q(deadline__lt=today)
)
for subtask in all_subtasks_done:
    print(f"{subtask.title=},{subtask.description=},{subtask.status=},{subtask.deadline=}")

Task.objects.filter(title="Prepare presentation").update(status="In progress")

SubTask.objects.filter(title="Gather information").update(
    deadline=F('deadline') - timedelta(days=2)
)

subtask = SubTask.objects.get(title="Create slides")
subtask.description = "Create and format presentation slides"
subtask.save()


Task.objects.filter(title="Prepare presentation").delete()

test = Task.objects.values("status").annotate(Count("id"))
print(test.query)
for t in test:
    print(t)



testweek = Task.objects.all().annotate(weekday=ExtractWeekDay('deadline'))


print(testweek)


for t in testweek:
    print(f"Task: {t}, Weekday: {t.weekday}")