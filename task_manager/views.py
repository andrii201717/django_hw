from django.utils import timezone
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import generics, status
from task_manager.models import Task, SubTask
from task_manager.serializers import TaskSerializer, TaskCreateSerializer, SubTaskCreateSerializer, SubTaskSerializer
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


class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubTaskListCreateView(APIView):
    def get(self, request):
        subtasks = SubTask.objects.all()
        serializer = SubTaskCreateSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class SubTaskDetailUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            return None

    def get(self, request, pk):
        subtask = self.get_object(pk)
        if not subtask:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubTaskCreateSerializer(subtask)
        return Response(serializer.data)

    def put(self, request, pk):
        subtask = self.get_object(pk)
        if not subtask:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubTaskCreateSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subtask = self.get_object(pk)
        if not subtask:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskByWeekdayListAPIView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        weekday = self.request.query_params.get('weekday')

        if weekday:
            days = {
                'понеділок': 0,
                'вівторок': 1,
                'середа': 2,
                'четвер': 3,
                'п’ятниця': 4,
                'субота': 5,
                'неділя': 6,
            }
            weekday_number = days.get(weekday.lower())
            if weekday_number is not None:
                queryset = queryset.filter(deadline__week_day=weekday_number + 1)  # Django: 1 — неділя
        return queryset

class SubTaskListAPIView(ListAPIView):
    queryset = SubTask.objects.all().order_by('-created_at')
    serializer_class = SubTaskSerializer

class FilteredSubTaskListAPIView(ListAPIView):
    serializer_class = SubTaskSerializer

    def get_queryset(self):
        queryset = SubTask.objects.all().order_by('-created_at')
        task_title = self.request.query_params.get('task')
        status = self.request.query_params.get('status')

        if task_title:
            queryset = queryset.filter(task__title__icontains=task_title)
        if status:
            queryset = queryset.filter(status=status)
        return queryset