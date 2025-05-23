from django.contrib import admin
from django.db.models import QuerySet
from task_manager.models import Category, Task, SubTask

class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 1

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    actions = ['set_subtask_status_in_done']
    list_display = ('task_title', 'title', 'description', 'deadline', 'status')

    def task_title(self, obj: SubTask) -> str:
        return obj.task.title
    task_title.short_description = "Task"

    def set_subtask_status_in_done(self, request, objs: QuerySet) -> None:
        for obj in objs:
            obj.status = "Done"
            obj.save()
        self.message_user(request, f"Статус оновлено для {objs.count()} підзадач.")

    set_subtask_status_in_done.short_description = "Оновити статуси на Done"

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTaskInline]
    list_display = ('short_title', 'description', 'category_names', 'deadline', 'status')
    list_filter = ('title', 'categories', 'deadline', 'status')
    list_per_page = 5

    def short_title(self, obj: Task) -> str:
        if not obj.title:
            return "(порожньо)"
        return obj.title[:10] + "..." if len(obj.title) > 10 else obj.title
    short_title.short_description = "Short_title"

    def category_names(self, obj: Task) -> str:
        return ", ".join(cat.name for cat in obj.categories.all())
    category_names.short_description = "Categories"


# admin.site.register(Task)
# admin.site.register(SubTask)
admin.site.register(Category)
