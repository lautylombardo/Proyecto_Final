from django.urls import path
from .views import EliminarView, HomeView, ArticuloView, AgregarView, EditarView

urlpatterns = [
    path('', HomeView.as_view(), name = "Home"),
    path('agregar/', AgregarView.as_view(), name = 'agregar'),
    path('articulo/<int:pk>', ArticuloView.as_view(),name = 'articulo'),# pk=Primary Key, sirve para numerar los articulos
    path('articulo/editar/<int:pk>', EditarView.as_view(),name = 'editar'),
    path('articulo/<int:pk>/eliminar', EliminarView.as_view(),name = 'eliminar'),
]
