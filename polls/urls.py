from django.urls import path
from polls.views import PollList,PollDetail,ChoiceList,CreateVote,UserCreate,LoginView
urlpatterns = [
    path("login/",LoginView.as_view(), name="login"),
    path('user-create',UserCreate.as_view(),name="user-create"),
    path('polls/',PollList.as_view(),name="poll-list"),
    path('poll/<int:id>',PollDetail.as_view(),name="poll-detail"),
    path("poll/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("poll/<int:pk>/choice/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    
]