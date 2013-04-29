from django.shortcuts import render_to_response
from django.template import RequestContext
from data.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def test(request):
	inp=request.GET.get('u','')
	#books= Book.objects.filter(Year__exact=inp)
	book_list= Book.objects.all()
	paginator = Paginator(book_list, 10)
	page = request.GET.get('page')
    	try:
       	 books = paginator.page(page)
    	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
       	 books = paginator.page(1)
    	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
       	 books = paginator.page(paginator.num_pages)
	return render_to_response('index.html',{"book":books},context_instance=RequestContext(request))	
