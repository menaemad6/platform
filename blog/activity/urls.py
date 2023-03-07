import core.views
from django.urls import path


urlpatterns = [
    path('upload', core.views.upload, name='upload'),
    # path('upload-activity', core.views.dashboard, name='upload-activity'),
    path('categorys/', core.views.categorys, name='categorys-page'),
    path('get-premium', core.views.get_premium, name='premium-page'),
    path('purchased-lessons', core.views.purchased_lessons, name='purchased-lessons'),
    path('purchase-error', core.views.money_error, name='money-error'),
    path('lessons', core.views.activity, name='home'),
    # path('lessons/<slug:slug>' , core.views.lesson_detail , name="lesson-page"),
    path('lessons/<slug:slug>' , core.views.lecture_detail , name="lesson-page"),
    path('lessons/progress/<slug:slug>' , core.views.lecture_progress , name="lesson-page"),
    path('news', core.views.news, name='news-page'),
    path('news/<slug:slug>' , core.views.news_detail , name="new-page"),

]