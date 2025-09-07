from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [ #Quanto mais especifica a url coloca ela pra cima.
    path('', views.index, name='index'),
    path('search/', views.search, name='search'), #Porque contact_id? porque esta lá na view!

    #Contact(CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'), #Porque contact_id? porque esta lá na view!
    path('contact/create/', views.create, name='create'), #Porque contact_id? porque esta lá na view!
]