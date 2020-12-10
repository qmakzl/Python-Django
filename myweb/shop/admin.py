from django.contrib import admin
from shop.models import Product


# 상품정보 관리 클래스
class ProductAdmin(admin.ModelAdmin):
    # 관리자 화면에 표시할 필드 목록
    list_display = ('product_name', 'price', 'description', 'picture_url')


# 상품 클래스와 상품관리클래스를 연결시키는 작업
admin.site.register(Product, ProductAdmin)
