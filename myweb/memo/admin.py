from django.contrib import admin
from memo.models import Memo


class MemoAdmin(admin.ModelAdmin):
    # 관리자 화면에서 관리할 필드 목록 정의
    list_display = ("writer", "memo")


# 관리자 사이트에서 사용할 클래스로 등록
admin.site.register(Memo, MemoAdmin)

