from django.shortcuts import render
import weasyprint
from root.utils import render_to_pdf
from django.http import Http404, HttpResponse
from datetime import datetime
from .models import Invoice


def download_to_pdf(request):
    # pdf = weasyprint.HTML('http://127.0.0.1:8000').write_pdf()
    # new_file = file('google.pdf', 'wb').write(pdf)
    pdf = render_to_pdf('dummy_download.html', {'data':'yolololollloloolool'})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %(datetime.now())
        content = "inline; filename='%s'" %(filename)
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response

def preview_template(request, id):
    obj = Invoice.objects.get(invoice_id=id)
    context = {"obj":obj}
    return render(request, "dummy_download.html", context)