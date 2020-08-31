from .import views
from django.urls import path
urlpatterns = [
    path('',views.home, name = 'home'),
    path('create/',views.Create_story, name = 'create'),
    path('test/<str:pk>',views.test, name = 'test'),
    path('result/',views.score, name = 'result'),
    path('guide/',views.instruction, name = 'instruction'),
    path('select/',views.select_story, name = 'selected'),
    path('update/<str:pk>',views.update_story, name = 'update'),
    path('story/',views.story_home, name = 'story_home'),
    path('create/<str:pk>',views.Create_Question, name = 'question'),
    path('delete/<str:pk>',views.delete, name = 'delete'),
    # path('delete_question/<str:pk>',views.delete_question, name = 'delete_question'),


]