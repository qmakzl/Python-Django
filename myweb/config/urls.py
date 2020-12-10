
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from config import views
from django.conf import settings

urlpatterns = [
    # http://localhost/admin/ ==> 관리자 페이지로
    path('admin/', admin.site.urls),

    # http://localhost -> views.py의 home 함수 호출
    path('', views.home),
    # address/urls.py를 포함시킴
    path('address/', include('address.urls')),

    path('memo/', include('memo.urls')),

    # survey/urls.py 를 포함시킴(http://localhost/survey)
    path('survey/', include('survey.urls')),

    # guestbook/urls.py 를 포함시킴(http://localhost/guestbook)
    path('guestbook/', include('guestbook.urls')),

    # member/urls.py 를 포함시킴(http://localhost/member)
    path('member/', include('member.urls')),

    # shop/urls.py 를 포함시킴(http://localhost/shop)
    path('shop/', include('shop.urls')),
]

if settings.DEBUG:  # 디버그 모드일 경우
    import debug_toolbar
    # 디버그를 위한 url pattern 추가
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
