from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic

# Create your views here.
# def index(request):
#     lastest_question_list = Question.objects.all()
#     return render(request, "polls/index.html", {
#         "lastest_question_list": lastest_question_list
#         })

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)  # se utiliza el object or 404 para que si no encuentra la pregunta muestre un error 404
#     return render(request, "polls/detail.html", {
#         "question": question
#         })


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {
#         "question": question
#         })

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "lastest_question_list"

    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # se utiliza el object or 404 para que si no encuentra la pregunta muestre un error 404
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No seleccionaste una opcion",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))