from django.urls import path
from myapp import views

urlpatterns = [
    path('display/', views.display_all, name='dis'),
    path('add/', views.add_student, name='add'),
    path('delete/<int:id>', views.delete_view, name='delete'),
    path('update/<int:id>', views.update_view, name='update'),
]
