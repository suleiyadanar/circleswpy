from django.urls import path
from home.views import Home, Explore, Contacts, Connector, Forum

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('/explore', Explore.as_view(), name='explore'),
    path('/contacts', Contacts.as_view(), name='contacts'),
    path('/connector', Connector.as_view(), name='connector'),
    path('/forum', Forum.as_view(), name='forum'),
]
