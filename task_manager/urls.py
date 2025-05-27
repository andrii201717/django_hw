from django.urls import path
from task_manager.views import TaskCreateView, TaskListView, TaskDetailView, TaskStatsView, \
    SubTaskDetailUpdateDeleteView, SubTaskListCreateView, TaskByWeekdayListAPIView, SubTaskListAPIView, \
    FilteredSubTaskListAPIView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('tasks/by-weekday/', TaskByWeekdayListAPIView.as_view(), name='tasks-by-weekday'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),  # створення та список
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
    path('subtasks/filter/', FilteredSubTaskListAPIView.as_view(), name='subtask-filter'),
]