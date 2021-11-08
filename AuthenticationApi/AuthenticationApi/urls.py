
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# register StudentViewSet with router
#router.register('studentapi',views.StudentViewSet,basename='student')

# register StudentModelViewSet with router
router.register('studentapi',views.StudentModelViewSet,basename='student')

#Register StudentReadOnlyModelViewSet with router
#router.register('studentapi',views.StudentReadOnlyModelViewSet,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]
