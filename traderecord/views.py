from .forms import StockRecordsForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .models import StockRecords
from django.shortcuts import reverse


class StockRecordsFormView(FormView):
    form_class = StockRecordsForm
    template_name = 'traderecord/AddRecord.html'

    def form_valid(self, form):
        # form.save_record(form,self.request)
        # look content of request usign form.request.POST
        if self.request.user.is_authenticated:
            username = self.request.user.username
            data = form.save(commit=False)
            data.user = username
            data.save()
        return super(StockRecordsFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse("traderecord:add_record_form")


class StockRecordDetailView(TemplateView):
    template_name = 'traderecord/DisplayRecord.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trade_records'] = StockRecords.objects.filter(user=self.request.user)
        return context
