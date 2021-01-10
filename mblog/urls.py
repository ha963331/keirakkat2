from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, showpost, mychart, chart, mountain


urlpatterns = [
    path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('mountain/<int:mountain_high>/', mountain ),
    path('mountain/', mountain),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('chartbydate/<int:year>/<int:month>/', chart),
    path('chartbydate/<int:year>/', chart),
    path('', homepage),
    
]
