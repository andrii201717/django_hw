from django.urls import path
from task_manager.views import (
    TaskCreateView, TaskListView,
    TaskStatsView,
    SubTaskDetailUpdateDeleteView,
    SubTaskListCreateView,
    TaskByWeekdayListAPIView,
    FilteredSubTaskListAPIView,
    TaskListCreateView, RegisterView,
    TaskRetrieveUpdateDestroyView,
    SubTaskRetrieveUpdateDestroyView
    )
from rest_framework.routers import DefaultRouter
from task_manager.views import CategoryViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('tasks/by-weekday/', TaskByWeekdayListAPIView.as_view(), name='tasks-by-weekday'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
    path('subtasks/filter/', FilteredSubTaskListAPIView.as_view(), name='subtask-filter'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),

    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    *router.urls
]