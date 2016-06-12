from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from .forms import ContactUsView
from django.contrib import messages

# Create your views here.


def index(request):
    """TODO: Docstring for index.
    :returns: TODO

    """
    t = loader.get_template('index.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))


def contact(request):
    """TODO: Docstring for contact.
    :returns: TODO

    """
    if request.method == 'POST':
        form = ContactUsView(request.POST)
        if form.is_valid():
            our_form = form.save(commit=False)
            our_form.save()
            messages.add_message(
                request, messages.INFO, 'Your message has been sent. Thank you.'
            )
            return HttpResponseRedirect('/success')
        else:
            pass
    else:
        form = ContactUsView()
    t = loader.get_template('contact.html')
    c = RequestContext(request, {'form': form, })
    return HttpResponse(t.render(c))
