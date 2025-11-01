from django.urls import path  # --- To create url
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('display/',views.display,name="display"),
    path('specific/<int:key>/',views.specific,name="specific"),
    path('update/<int:key>/',views.update,name="update"),
    path('delete/<int:key>/',views.delete,name="delete"),
    path('create/',views.create,name='create'),


    path('createPrior/',views.create_priority,name='createprior'),
    path('displayPrior/',views.read_priority,name='displayprior'),
    path('updatePrior/<int:key>/',views.update_priority ,name='updateprior'),
    path('deletePrior/<int:key>/',views.delete_priority,name='deleteprior'),
    path('history/',views.history,name='history'),
    path('deletePrior/<int:key>/',views.restore,name='restore'),
]