from django.conf.urls import url
from .views import home, visit, check_out

urlpatterns = [
    url(r"^$", home, name="home"),
    url(r"^record/", visit, name="visit"),
    url(r"^checkout/", check_out, name="checkout"),

]
