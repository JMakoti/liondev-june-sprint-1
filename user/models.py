# from django.db import models
# from django.utils import timezone

# class CommunityMember(models.Model):
#     ROLE_CHOICES = [
#         ('member', 'Member'),
#         ('visitor', 'Visitor'),
#         ('staff', 'Staff'),
#         ('attachee', 'Attachee'),
#         ('not_sure', 'Not_Sure'),
#     ]

#     DEPARTMENT_CHOICES = [
#         ('tech_department', 'Tech_Department'),
#         ('entrepreneurship', 'Entrepreneurship'),
#         ('heritage', 'Heritage'),
#         ('finance', 'Finance'),
#         ('youth_engagement', 'Youth_Engagement'),
#         ('finance', 'Finance'),
#         ('creatives', 'Creatives'),
#     ]
#     department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, default='engineering')
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     joined_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class StaffMember(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     joined_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('staff', 'Staff'),
        ('community', 'Community Member'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
