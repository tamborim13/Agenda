from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [ #Quanto mais especifica a url coloca ela pra cima.
    path('<int:contact_id>/', views.contact, name='contact'), #Porque contact_id? porque esta lá na view!
    path('', views.index, name='index'),
]