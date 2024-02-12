from django.db import models
import datetime
from users.models import IMUser, Cohort


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 2000)
    description = models.TextField(default = 'N/A', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add= True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now= True, blank=True, null=True)


    def __str__(self) -> str:
        return f"{self.name}" 

#Lucky assignment

class ClassSchedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)

   
    def __str__(self):
        return self.title

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='attendances')

  

    def __str__(self):
        return f"{self.attendee} - {self.class_schedule}"

class Query(models.Model):
    RESOLUTION_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DECLINED', 'Declined'),
        ('RESOLVED', 'Resolved'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    submitted_by = models.ForeignKey(IMUser, related_name='submitted_queries', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(IMUser, related_name='assigned_queries', on_delete=models.CASCADE)
    resolution_status = models.CharField(max_length=20, choices=RESOLUTION_STATUS_CHOICES, default='PENDING')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='queries')

    

    def __str__(self):
        return self.title

class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_query_comment')

   

    def __str__(self):
        return f"Comment on {self.query.title}"