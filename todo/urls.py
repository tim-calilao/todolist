"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

"""
put the account management (login/logout) in navbar - done
mail when nearing deadline
settings for email and when how many days before deadline
do the viewing and adding in one page
for update (completed specifically) don't put in modal for easier use
"""


urlpatterns = [
    url(r'^login$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^admin', admin.site.urls),
    # url(r'^$', auth_views.login, name = 'index'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    #url(r'^tables.php$', views.tables, name='tables'),
    url(r'^register$', CreateView.as_view(
                template_name='register.html',
                form_class=UserCreationForm,
                success_url='/'
        )),

]
