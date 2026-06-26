"""
URL configuration for daily_basket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from dd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index",views.indexpage),
    path("about",views.aboutpage),
    path("addproducts",views.addproductspage),
    path("blog",views.blogpage),
    path("blog-single",views.blogsinglepage),
    path("codes",views.codespage),
    path("contact",views.contactpage),
    path("category/<int:id>",views.categorypage),
    path("faq",views.faqpage),
    path("",views.homepage),
    path("indexd060",views.indexd060page),
    path("mail",views.mailpage),
    path("master",views.masterpage),
    path("products1",views.products1page),
    path("products2",views.products2page),
    path("shortcodes",views.shortcodespage),
    path("single/<int:id>",views.singlepage),
    path("fetchproducts",views.fetchproductdata),
    path("fetchregisterdata",views.fetchregisterdata),
    path("checklogindata",views.checklogindata),
    path("logout",views.logout),
    path("manageproduct",views.manageproductpage),
    path("manageorder",views.manageorderpage),
    path("insertiontocart",views.insertiontocart),
    path("showcart",views.showcart),
    path("footer",views.footerpage),
    path("increase/<int:id>", views.increase),
    path("descrease/<int:id>", views.descrease),
    path("deleteitem/<int:id>", views.deleteitem),
    path("deleteproduct/<int:id>", views.deleteproduct),
    path('placeorder', views.placeorder),
    path('payment-success', views.payment_success),
    path('payment', views.payment_page),
    path('showwish', views.showwish),
    path('deletewish/<int:id>',views.deletewish),
    path("change-password", views.change_password),
    path("sellerorder", views.sellerorder),
    path('cancelorder/<int:id>', views.cancelorder),
    path('abortpayment/<int:id>', views.abortpayment),
    path('yourorderdetailes/<int:id>', views.yourorderdetailes),
    path('editproducts/<int:product_id>', views.editproductdata, name='editproduct'),
    path('change_password', views.change_password),
    path('reset_password',views.reset_password),
    path('submit_review/<int:id>/', views.submit_review, name='submit_review'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('edit_review/<int:id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:id>/', views.delete_review, name='delete_review'),
    path('update_profile_image', views.update_profile_image, name='update_profile_image'),
    path('seller_reviews/', views.seller_reviews, name='seller_reviews'),
    path('subscribe_newsletter', views.subscribe_newsletter, name='subscribe_newsletter'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

