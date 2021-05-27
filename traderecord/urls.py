from django.urls import path, re_path
from .views import StockRecordsFormView,StockRecordDetailView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

app_name = 'traderecord'

urlpatterns = [
    path('register/', login_required(StockRecordsFormView.as_view(),login_url='userinfo:login'), name='add_record_form'),
    path('display_record/',login_required(StockRecordDetailView.as_view(),login_url='userinfo:login'),name='display'),
]
 #             + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
