# from django.contrib import admin
from django.urls import path
from . import views

# routing
# localhost:8000/chai
# loaclhost:8000/chai/order
urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.all_chai, name="all_chai"),
    # path("order/", views.order, name="order"),
    # path("about/", views.about, name="about"),
    # path("contact/", views.contact, name="contact"),
    path("<int:chai_id>/", views.chai_detail, name="chai_detail"),
    path("chai_stores/", views.chai_store_view, name="chai_stores"),
    path("chai_form/", views.chai_forms_view, name="chai_forms"),
]

# now the application urls.py is created
# sometime the main urls.py file refer the sub urls.py files
# so now we are creating the sub urls.py files
# but first we have to pass the control.
# so first pass the cortrol.
