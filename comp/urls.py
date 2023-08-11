from django.urls import path
from .views import ComplistALLView,CompDetalesView,CompCreateView,CompDeleteView,CompUpdateView
urlpatterns=[
    path('get_all/',ComplistALLView.as_view()),
    path("get_by_index/<int:comp_id",CompDetalesView.as_view()),
    path('create/',CompCreateView.as_view()),
    path("update/<int:comp_id>/",CompUpdateView.as_view()),
    path('delete/<int:comp_id>/',CompDeleteView.as_view()),
]