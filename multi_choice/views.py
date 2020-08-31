from django.shortcuts import render, redirect, get_object_or_404
from .models import Question,Story_text
from .forms import StoryForm, QuestionForm
# Create your views here.
def home(request):
    story = Story_text.objects.all()
    questions = Question.objects.all()
    context = {'story':story,
               'questions':questions
               }
    return render(request, 'multi_choice/home.html', context)
# def Create_story(request):
#     story_model = Story_text.objects.all()
#     return render(request, 'multi_choice/create.html', {'story':story_model})
def Create_story(request):
    story_model = Story_text.objects.all()
    # comments = Comment.objects.all().filter(post_id=pk)

    story_form = StoryForm
    if request.method == 'POST':
        story_form = StoryForm(request.POST)
        if story_form.is_valid():

            story_form.save()

            return redirect('story_home')
    context = {
               'story': story_form
               }
    return render(request, 'multi_choice/create.html', context)
def story_home(request):
    story = Story_text.objects.all()

    context = {'story':story}
    return render(request, 'multi_choice/story_home.html', context)


def Create_Question(request, pk):
    story_model = Story_text.objects.get(id = pk)
    question = Question.objects.all().filter(story_id=pk)

    Question_form = QuestionForm()
    post = get_object_or_404(Story_text, pk=pk)
    if request.method == 'POST':
        Question_form = QuestionForm(request.POST)
        if Question_form.is_valid():
            options = Question_form.save(commit=False)
            options.story = post
            options.save()
            return redirect('question', pk=post.pk)
    # context =
    return render(request, 'multi_choice/create_question.html', {
                'story_obj':story_model,
               'question_form': Question_form,
                'questions':question,
               })


def update_story(request, pk):
    story_m = Story_text.objects.get(id= pk)
    form = StoryForm(instance=story_m)
    if request.method == 'POST':
        form = StoryForm(request.POST,  instance=story_m)
        if form.is_valid():
           form.save()
           return redirect('story_home')
    context = {'form':form}
    return render(request, 'multi_choice/update.html', context)
def delete(request, pk):
    story_m = Story_text.objects.get(id=pk)
    if request.method=='POST':
        story_m.delete()
        return redirect('story_home')

    context = {'story':story_m}
    return render(request, 'multi_choice/delete.html', context)
def instruction(request):
    return render(request, 'multi_choice/instruction.html')
def select_story(request):
    story = Story_text.objects.all()
    context = {'story':story}
    return render(request,'multi_choice/select_story.html', context)


def test(request, pk):
    story= Story_text.objects.get(id=pk)
    question = Question.objects.all().filter(story_id=pk)
    context = {'story':story,
               'question': question}


    return render(request, 'multi_choice/take_test.html', context)


def score(request):
    # question = Question.objects.get(id= pk)
    context = {}
    return render(request,'multi_choice/result.html', context)


# def delete_question(request, pk):
#     question = Question.objects.get(id=pk)
#     if request.method=='POST':
#         question.delete()
#         return redirect('story_home')
#
#     context = {'question':question}
#     return render(request, 'multi_choice/delete_options.html', context)
