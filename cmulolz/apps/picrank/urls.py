from django.conf.urls import patterns, include, url
import views

# Main URL Patterns
urlpatterns = patterns('',
    url(r'^vote$', views.vote, name="vote"),
    url(r'^result$', views.result, name="result"),
)