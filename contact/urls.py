from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [ #Quanto mais especifica a url coloca ela pra cima.
    path('', views.index, name='index'),
    path('search/', views.search, name='search'), #Porque contact_id? porque esta lá na view!

    #Contact(CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'), #Porque contact_id? porque esta lá na view!
    path('contact/create/', views.create, name='create'), #Porque contact_id? porque esta lá na view!
    path('contact/<int:contact_id>/update/', views.update, name='update'), #Porque contact_id? porque esta lá na view!
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), #Porque contact_id? porque esta lá na view!
]