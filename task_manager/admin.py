from django.contrib import admin

from task_manager.models import Category, Task, SubTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'status')
    search_fields = ('title',)
    list_filter = ('status',)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'status')
    search_fields = ('title',)
    list_filter = ('status',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

#admin.site.register(Category)
#admin.site.register(Task)
#admin.site.register(SubTask)
