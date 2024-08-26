from django.db import models
from django.utils.text import slugify


# Category.
class Category(models.Model):
	emoji = models.CharField(max_length=5, blank=True, null=True)
	name = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128, blank=True, null=True)
	description = models.TextField(blank=True, null=True)

	def save(self, *args, **kwargs):
		self.name = self.name.title()
		if not self.slug:
			self.slug = slugify(self.name.lower())
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'

# Quiz.
class Quiz(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	category = models.ForeignKey(to=Category, on_delete=models.CASCADE, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Quizzes'

# Question.
class Question(models.Model):
	quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE, related_name='questions')
	text = models.CharField(max_length=255)

	def __str__(self):
		return self.text

# Choice.
class Choice(models.Model):
	question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='choices')
	text = models.CharField(max_length=255)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.text