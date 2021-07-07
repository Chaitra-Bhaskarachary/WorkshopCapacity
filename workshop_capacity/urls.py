from django.urls import path,include
from capacity import views

urlpatterns = [
    path('', views.entry_form,name='entry_insert'), # get and post req. for insert operation
    path('<int:id>/', views.entry_form,name='entry_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.entry_delete,name='entry_delete'),
    path('list/',views.entry_list,name='entry_list') # get req. to retrieve and display all records
]