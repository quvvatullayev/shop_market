from django.urls import path
from .views.user import (
    AddUser,
    UserList,
    GetUser,
    UpdateUser,
    DeleteUser,
)

urlpatterns = []
urlpatterns += [
    path('add-user/', AddUser.as_view()),
    path('user-list/', UserList.as_view()),
    path('get-user/<int:chat_id>/', GetUser.as_view()),
    path('update-user/', UpdateUser.as_view()),
    path('delete-user/<int:chat_id>/', DeleteUser.as_view()),
]

from .views.category import (
    AddCategory,
    CategoryList,
    GetCategory,
    UpdateCategory,
    DeleteCategory,
)

urlpatterns += [
    path('add-category/', AddCategory.as_view()),
    path('category-list/', CategoryList.as_view()),
    path('get-category/<int:category_id>/', GetCategory.as_view()),
    path('update-category/', UpdateCategory.as_view()),
    path('delete-category/<int:category_id>/', DeleteCategory.as_view()),
]

from .views.sub_category import (
    AddSub_category,
    Sub_categoryList,
    GetSub_category,
    UpdateSub_category,
    DeleteSub_category,
)

urlpatterns += [
    path('add-sub_category/', AddSub_category.as_view()),
    path('sub_category-list/', Sub_categoryList.as_view()),
    path('get-sub_category/<int:sub_category_id>/', GetSub_category.as_view()),
    path('update-sub_category/', UpdateSub_category.as_view()),
    path('delete-sub_category/<int:sub_category_id>/', DeleteSub_category.as_view()),
]       

from .views.product import (
    AddProduct,
    ProductList,
    GetProduct,
    UpdateProduct,
    DeleteProduct,
)

urlpatterns += [
    path('add-product/', AddProduct.as_view()),
    path('product-list/', ProductList.as_view()),
    path('get-product/<int:product_id>/', GetProduct.as_view()),
    path('update-product/', UpdateProduct.as_view()),
    path('delete-product/<int:product_id>/', DeleteProduct.as_view()),
]

from .views.cart import (
    AddCart,
    CartList,
    GetCart,
    UpdateCart,
    DeleteCart,
)

urlpatterns += [
    path('add-cart/', AddCart.as_view()),
    path('cart-list/', CartList.as_view()),
    path('get-cart/<int:cart_id>/', GetCart.as_view()),
    path('update-cart/', UpdateCart.as_view()),
    path('delete-cart/<int:cart_id>/', DeleteCart.as_view()),
]

from .views.order import (
    AddOrder,
    OrderList,
    GetOrder,
    UpdateOrder,
    DeleteOrder,
    AddOrderList,
    GetOrder_by_chat_id
)

urlpatterns += [
    path('add-order/', AddOrder.as_view()),
    path('order-list/', OrderList.as_view()),
    path('get-order/<int:order_id>/', GetOrder.as_view()),
    path('update-order/', UpdateOrder.as_view()),
    path('delete-order/<int:order_id>/', DeleteOrder.as_view()),
    path('add-order-list/', AddOrderList.as_view()),
    path('get-order-by-chat-id', GetOrder_by_chat_id.as_view())
]

from .views.start_category import (
    StartCategory,
)

urlpatterns += [
    path('start/', StartCategory.as_view())
]