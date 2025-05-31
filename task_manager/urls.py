from django.urls import path
from task_manager.views import TaskCreateView, TaskListView, TaskDetailView, TaskStatsView, \
    SubTaskDetailUpdateDeleteView, SubTaskListCreateView, TaskByWeekdayListAPIView, SubTaskListAPIView, \
    FilteredSubTaskListAPIView, TaskListCreateView, TaskRetrieveUpdateDestroyView, SubTaskRetrieveUpdateDestroyView
from rest_framework.routers import DefaultRouter
from task_manager.views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('tasks/by-weekday/', TaskByWeekdayListAPIView.as_view(), name='tasks-by-weekday'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
    path('subtasks/filter/', FilteredSubTaskListAPIView.as_view(), name='subtask-filter'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),

    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail'),
    *router.urls
]