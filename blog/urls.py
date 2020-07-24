from django.urls import path

from . import views


urlpatterns=[
    path('blogs/', views.BlogList.as_view()),
    path('readblog/<int:id>/', views.BlogDetail.as_view()),
    path('createblog/',views.Create.as_view()),
    path('delete/<int:pk>/', views.Delete.as_view()),
    path('update/<int:pk>/', views.Update.as_view())
]