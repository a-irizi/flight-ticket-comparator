from django.urls import path

from comparator.views import IndexTemplateView


app_name = "comparator"

urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index'),
]
