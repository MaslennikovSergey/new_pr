from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, StreamingHttpResponse, FileResponse, JsonResponse
from django.urls import reverse
from django.template.loader import get_template
from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist

from .models import Product

# Create your views here.

#def index(request):
	#return HttpResponse('Hello, World')

def index(request):
	return render(request,'index.html')

#def index(request):
	#template = get_template('index.html')
	#return HttpResponse(template.render())

#def index(request):
	#№cont = ('Hello', ' world')
	#resp = StreamingHttpResponse(cont)
	#return resp

def page(request, page_num):
		return HttpResponse(f'Page {page_num}')


def about(req, id):  # параметр req(request) - обязательный параметр контроллера
		#req.headers
		#return HttpResponse('About')  # HttpResponse - класс вывода на экран
		#return HttpResponse(f'{req.headers}')
		#return HttpResponse(f'{req.body}')
		#return HttpResponse(f'{req.get}')
		#return HttpResponse(f'{dict(req.GET)}')
		#a = int(req.GET.get('a'))
		#b = int(req.GET.get('b'))
		#return HttpResponse(f'{a + b}')
		#return HttpResponse(f'{req.method}')
		#return HttpResponse(f'{req.scheme}')

		#res = HttpResponse()
		#return HttpResponse(f'{res.status_code}')
		#return HttpResponse(f'{res.content}')

		#return HttpResponseRedirect('service')

		#return HttpResponseRedirect(reverse('service'))

		try:
			var = Product.objects.get(pk = id)
		except Product.DoesNotExist:
			#r eturn HttpResponseNotFound('NOT FOUND')
			#raise HttpResponseNotFound('NOT FOUND')
			raise Http404('NOT FOUND')
	
		return HttpResponse('OK')

def  file_show(req):
	file = 'service/whitehouse.jpg'
	return FileResponse(open(file, 'rb'), as_attachment = True, filename = 'home')

def json_show(req):
	data = {'cost':14, 'title':'book'}
	return JsonResponse(data)