from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers, permissions
# para Swagger
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# ApiViews
from restaurant.apiviews.menuApiviews import MenuView
from restaurant.apiviews.menuApiviews import MenuItemView
from restaurant.apiviews.menuApiviews import MenuItemCategoryView
from restaurant.apiviews.ingredienteApiviews import UnidadMedidaView
from restaurant.apiviews.ingredienteApiviews import IngredienteView
from restaurant.apiviews.ingredienteApiviews import IngredienteDetallesView
from restaurant.apiviews.ingredienteApiviews import IngredienteExistenciaView
from restaurant.apiviews.mesaApiview import MesaView
from restaurant.apiviews.mesaApiview import MesaUbicacionView
from restaurant.apiviews.mesaApiview import MesaStatusView
from restaurant.apiviews.ordenApiviews import OrdenView
from restaurant.apiviews.ordenApiviews import OrdenStatusView
from restaurant.apiviews.ordenApiviews import OrdenDetalleView
from restaurant.apiviews.ventaApiviews import VentaView
from restaurant.apiviews.ventaApiviews import MetodoPagoView
from restaurant.apiviews.ventaApiviews import MetodoPagoDetalleView
from restaurant.apiviews.meseroApiviews import MeseroView
from restaurant.apiviews.clienteApiviews import ClienteView

# Routing
router = routers.DefaultRouter()
# Menu
router.register(r'menus', MenuView)
router.register(r'menu-items', MenuItemView)
router.register(r'menu-item-categorys', MenuItemCategoryView)
# Ingrediente
router.register(r'unidades-medida', UnidadMedidaView)
router.register(r'ingredientes', IngredienteView)
router.register(r'ingrediente-detalles', IngredienteDetallesView)
router.register(r'ingrediente-existencias', IngredienteExistenciaView)
# Mesa
router.register(r'mesas', MesaView)
router.register(r'mesa-ubicaciones', MesaUbicacionView)
router.register(r'mesa-estados', MesaStatusView)
# Orden
router.register(r'ordenes', OrdenView)
router.register(r'orden-estados', OrdenStatusView)
router.register(r'orden-detalles', OrdenDetalleView)
# Venta
router.register(r'ventas', VentaView)
router.register(r'metodos-de-pago', MetodoPagoView)
router.register(r'metodos-de-pago-detalles', MetodoPagoDetalleView)
# Mesero
router.register(r'meseros', MeseroView)
# Cliente
router.register(r'clientes', ClienteView)

# Swagger Docs
# Creando esquema de configuracion para la auto doc de swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant API",
        default_version='v1',
        description="Practice API that simuling an restaurant",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="brochegomezf@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/', include(router.urls)),

    # End Point para construir el schema de configuracion del Swagger
    path('schema/', swaggerUi_schema, name="schema-apiTask"),

    # End Point para visitar la Documentacion de la Api
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
