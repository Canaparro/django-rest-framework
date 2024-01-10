from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIVIew.as_view()),
    path("<int:pk>/delete/", views.ProductDeleteAPIVIew.as_view()),
    path("<int:pk>/", views.ProductDetailAPIVIew.as_view()),
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view),
    # path("", views.ProductMixinView.as_view()),
    # path("<int:pk>/update/", views.ProductMixinView.as_view()),
    # path("<int:pk>/delete/", views.ProductMixinView.as_view()),
    # path("<int:pk>/", views.ProductMixinView.as_view()),
]
