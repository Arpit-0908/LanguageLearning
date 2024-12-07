from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('chat/', views.chat_view, name='chat'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('Japan/', views.Japan_view, name='japan'),
    path('Spanish/', views.Spanish_view, name='Spanish'),
    path('French/', views.French_view, name='French'),
    path('German/', views.German_view, name='German'),
    path('Hindi/', views.Hindi_view, name='Hindi'),
    path('Language/', views.Language, name='lan'),
    path('review/', views.review, name='review'),
    path('Bookclass/', views.book_slot, name='Bookclass'),
    path('payment/', views.payment_view, name='payment'),
    path('', views.index, name='index'),
    # Password reset paths
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
