from django.contrib import admin
from address.models import Address


class AddressAdmin(admin.ModelAdmin):
    #관리자 화면에 출력할 필드 목록 정의
    list_display = ('name', 'tel', 'email', 'address')

#관리자 기능에 Address, AddressAdmin 클래스에 등록
#관리자 화면에서 주소록을 관리할 수 있게 됨
admin.site.register(Address, AddressAdmin)
