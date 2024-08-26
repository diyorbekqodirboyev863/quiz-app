from . import models, forms
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory

# Home.
def home(request):
	quizzes = models.Quiz.objects.all()
	categories = models.Category.objects.all()
	return render(request, 'home.html', {'quizzes': quizzes, 'categories': categories})

# Quiz Detail View
def quiz_detail(request, quiz_id):
	'''View to attempt all questions.'''
	quiz = get_object_or_404(models.Quiz, id=quiz_id)
	questions = models.Question.objects.filter(quiz=quiz)
	if request.method == 'POST':
		correct_answers = 0
		total_questions = questions.count()
		name = request.POST['name']
		for question in questions:
			choice_id = request.POST.get(f'question-{question.id}')
			if choice_id:
				try:
					choice = models.Choice.objects.get(id=choice_id)
					if choice.is_correct:
						correct_answers += 1
				except models.Choice.DoesNotExist:
					pass
		results = {
			'quiz': quiz,
			'correct': correct_answers,
			'questions': total_questions,
			'name': name.title(),
		}
		return render(request, 'quiz_detail.html', {'quiz': quiz, 'results': results})
	else:
		return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})

# Test view.
def test(request):
	return render(request, 'test.html', {})

# Category Detail View
def category_detail(request, slug):
	'''View for categories.'''
	category = get_object_or_404(models.Category, slug=slug)
	quizzes = models.Quiz.objects.filter(category=category)
	return render(request, 'category_detail.html', {'quizzes': quizzes, 'category': category})
