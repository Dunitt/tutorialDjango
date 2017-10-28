
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


from .models import Question

# ex: /polls/
def index(request):

	lastest_question_list= Question.objects.order_by("-pub_date")[:5]
	contex= {"lastest_question_list": lastest_question_list}

	return render(request, "polls/index.html", contex)

# ex: /polls/<question_id>/
def detail(request, question_id):

	question= get_object_or_404(Question, pk= question_id)

	return render(request, "polls/detail.html", {"question": question})

# ex: /polls/<question_id>/results/
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# ex: /polls/<question_id>/vote/
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)