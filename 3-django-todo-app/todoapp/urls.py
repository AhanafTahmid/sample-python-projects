from django.urls import path

from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>',views.deletes,name="deleted"),
    path('m_com/<int:id>',views.m_com,name="mark_completed"),
    path('m_incom/<int:id>',views.m_incom,name="mark_incompleted"),
    path('edit/<int:id>', views.edit, name="edit"),

]