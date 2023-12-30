from django.urls import path
from . import views
from . import static

urlpatterns = [
    path('', views.index),
    path('lemax/', views.lemax, name='lemax'),
    path('arbol/', views.arbol, name='arbol'),
    path('puntasArbol/', views.puntasArbol, name='puntasArbol'),
    path('guirnaldas/', views.guirnaldas, name='guirnaldas'),
    path('belenes/', views.belenes, name='belenes'),
    path('belenesclasicos/', views.belenesclasicos, name='belenesclasicos'),
    path('lluville/', views.lluville, name='lluville'),
    path('bolas/', views.bolas, name='bolas'),
    path('luces/', views.luces, name='luces'),
    path('guirnaldaled/', views.guirnaldaled, name='guirnaldaled'),
    path('cortinaled/', views.cortinaled, name='cortinaled'),
    path('colecciones/', views.colecciones, name='colecciones'),

]
