from django.urls import path
from . import views

urlpatterns = [
    path("", views.SearchListView.as_view(), name="search"),
    path("algolia/", views.SearchThroughAlgoliaListView.as_view(), name="search"),
]
