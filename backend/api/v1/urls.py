from django.urls import include, path

urlpatterns = [

    path(
        "auth/",
        include("users.urls"),
    ),

    path(
        "categories/",
        include("categories.urls"),
    ),

    path(
        "products/",
        include("products.urls"),
    ),

    path(
        "orders/",
        include("orders.urls"),
    ),

    path(
        "reports/",
        include("reports.urls"),
    ),

]