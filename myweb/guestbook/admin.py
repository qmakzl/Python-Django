from django.contrib import admin
from guestbook.models import Guestbook


class GuestbookAdmin(admin.ModelAdmin):
    # 관리자 화면에서 사용할 필드 정의
    list_display = ('name', 'email', 'passwd', 'content')


# 테이블 클래스와 관리자화면 클래스를 등록함
admin.site.register(Guestbook, GuestbookAdmin)
