from django.urls import path
from django.views.generic import TemplateView
from . import views


# ici je vais jute tester de javascripts très basique
# pour cela je vais juste display des pages html :

app_name = 'js_first'

urlpatterns = [
        path('page_color/', TemplateView.as_view(template_name='js_first/page_color.html'), name='page_color')

]