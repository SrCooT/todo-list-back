from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core.views import TarefaViewSet

router = routers.DefaultRouter()
router.register(r'Tarefa', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('tarefas/<int:id>/marcar_concluido/', TarefaViewSet.as_view({'patch': 'marcar_concluido'})),
]
