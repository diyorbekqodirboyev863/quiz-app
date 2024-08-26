from django.contrib import admin
from . import models

# Category.
admin.site.register(models.Category)

# Quiz.
admin.site.register(models.Quiz)

# Question.
admin.site.register(models.Question)

# Choice.
admin.site.register(models.Choice)