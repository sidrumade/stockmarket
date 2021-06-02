from django.urls import path, re_path
from .views import StockRecordsFormView,StockRecordDetailView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'traderecord'

urlpatterns = [
    path('register/', login_required(StockRecordsFormView.as_view(),login_url='userinfo:login'), name='add_record_form'),
    path('display_record/',login_required(StockRecordDetailView.as_view(),login_url='userinfo:login'),name='display'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
