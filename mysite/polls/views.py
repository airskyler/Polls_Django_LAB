from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone



# The render() defintion below are reference from URL of
# https://docs.djangoproject.com/en/1.9/intro/tutorial03/

# The render() function takes the request object as its first argument,
# a template name as its second argument and a dictionary as its optional third argument.
# It returns an HttpResponse object of the given template rendered with the given context.



# display a list of object
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # return the last 5 published question filter by time from now
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# display a detail page of particular object
class DetailView(generic.DetailView):
    model = Question    # use Question model
    template_name = 'polls/detail.html'  # appearance code for detail view
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

		
		
		# display the result web page 
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'




	
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

