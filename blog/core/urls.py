from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('settings', views.settings, name='settings'),
    path('settings-teacher', views.settings_teacher, name='settings-teacher'),
    path('setup-account', views.setup_acount, name='setup-account'),
    path('setup-account-teacher', views.setup_acount_teacher, name='setup-account-teacher'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('search-page', views.search_page, name='search-page'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('like-lesson', views.like_lesson, name='like-lesson'),
    path('buy-lesson', views.purchase_lesson, name='buy-lesson'),

    path('comment', views.comment, name='comment'),
    path('reply', views.reply, name='reply'),

    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]


