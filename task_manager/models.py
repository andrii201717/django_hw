from django.db import models

status_choises = [
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Pending", "Pending"),
        ("Blocked", "Blocked"),
        ("Done", "Done")
    ]

class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=50, unique_for_date="deadline")
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=100, choices=status_choises)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=status_choises)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title