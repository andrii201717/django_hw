from django.utils import timezone
from rest_framework.views import APIView
from rest_framework import generics
from task_manager.models import Task
from task_manager.serializers import TaskSerializer
from rest_framework.response import Response
from django.db import models

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskStatsView(APIView):
    def get(self, request):
        total_tasks = Task.objects.count()


        status_counts = Task.objects.values('status').order_by().annotate(count=models.Count('status'))

        status_summary = {item['status']: item['count'] for item in status_counts}


        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

        data = {
            'total_tasks': total_tasks,
            'tasks_by_status': status_summary,
            'overdue_tasks': overdue_tasks,
        }
        return Response(data)