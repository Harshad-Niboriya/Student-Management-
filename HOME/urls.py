from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index),
    path('sign_up',views.sign_up),
#     path('courses',views.courses),
#     path('dashboard',views.dashboard),
#     path('hostel',views.hostel),
#     path('notice',views.notice),

]
