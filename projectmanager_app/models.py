from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    user_image = models.ImageField(upload_to="profileImg/")
    
    def __str__(self):
        return f'{self.user.username}'
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_author")
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    
class Invitation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_invitation")
    invitee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_invitee")
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.project} --- {self.invitee}'
    
class Note(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_note")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Note_author")
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_task")
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done  = models.BooleanField(default=False)
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_DoneBy", null=True, blank=True)
    done_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_DoneBy", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    
class Member(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_member")
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member_project")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.project} --- {self.member}'