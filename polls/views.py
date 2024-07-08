from django.shortcuts import  render, redirect, get_object_or_404
from .models import Poll, PollTable, PollHaveOptions, Vote
# Create your views here.

def poll_list(request):
    polls = PollTable.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = get_object_or_404(PollTable, pk=poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

def vote(request, poll_id):
    poll = get_object_or_404(PollTable, pk=poll_id)
    user = get_object_or_404(Poll, pk=request.POST['user_id'])
    try:
        selected_option = poll.polehaveoptions_set.get(pk=request.POST['option'])
    except (KeyError, PollHaveOptions.DoesNotExist):
        return render(request, 'polls/poll_detail.html', {
            'poll': poll,
            'error_message': "You didn't select a valid option.",
        })
    else:
        Vote.objects.create(user_id=user, user_question=poll, user_option=selected_option)
        return redirect('polls:poll_results', poll_id=poll.id)

def poll_results(request, poll_id):
    poll = get_object_or_404(PollTable, pk=poll_id)
    return render(request, 'polls/poll_results.html', {'poll': poll})
