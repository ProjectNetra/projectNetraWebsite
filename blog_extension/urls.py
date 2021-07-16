from django.urls.conf import path
from .views import toggle_subscription, contact_view
urlpatterns = [
    path('toggle_subscription/',
         toggle_subscription, name='toggle_subscription'),
    path('contact_form/', contact_view, name='submit_contact_form')
]

app_name = 'blog_extension'
