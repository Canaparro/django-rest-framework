from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view(), name="product-list"),
    path("<int:pk>/update/", views.ProductUpdateAPIVIew.as_view(), name="product-edit"),
    path("<int:pk>/delete/", views.ProductDeleteAPIVIew.as_view()),
    path("<int:pk>/", views.ProductDetailAPIVIew.as_view(), name="product-detail"),
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view),
    # path("", views.ProductMixinView.as_view()),
    # path("<int:pk>/update/", views.ProductMixinView.as_view()),
    # path("<int:pk>/delete/", views.ProductMixinView.as_view()),
    # path("<int:pk>/", views.ProductMixinView.as_view()),
]
