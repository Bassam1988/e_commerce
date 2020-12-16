from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shopf/', include("frontend.urls")),
    path('shop/', include("shop.urls")),
    path('account/', include("accounts.urls")),

]
