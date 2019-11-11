"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

from stretch_goals import views

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'goals', views.GoalViewSet)
router.register(r'records', views.RecordViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/add_record', views.home, name='add_record'),
    path('records/', views.records, name='records'),
    path('create_new_goal/', views.create_new_goal, name='create_new_goal'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api_root'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path('api-goals/', views.GoalsList.as_view(), name='api_goals_list'),
    # path('api-goal/<int:pk>/', views.GoalDetail.as_view(), name='api_goal_detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
