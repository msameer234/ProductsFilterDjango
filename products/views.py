from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

from django.contrib.auth.models import User
# Create your views here.


def products(request):
	superusers = User.objects.filter(is_superuser=True)
	print(superusers)
	products = Products.objects.all()
	pFilter = False
	selectedOS = None
	selectedProcessor = None
	minPrice = 0
	maxPrice = 0

	processors = []
	OSs = []

	for product in products:
		add_processor = True
		processor_available = product.pProcessor
		for processor_already in processors:
			if processor_available == processor_already:
				add_processor = False
		if add_processor:
			processors.append(processor_available)


		add_OS = True
		OS_available = product.pOS
		for OS_already in OSs:
			if OS_available == OS_already:
				add_OS = False
		if add_OS:
			OSs.append(OS_available)

	print(OSs)
	print(processors)

	
	# a = product.pPrice <= maxPrice
	# b = product.pPrice >= minPrice
	# c = product.pProcessor == selectedProcessor
	# d = product.pOS == selectedOS

	if request.method == 'POST':		
		if request.POST.get('aFilter'):
			minPrice = (request.POST['minPrice'])
			print(minPrice)

			maxPrice = (request.POST['maxPrice'])
			print(maxPrice)

			selectedProcessor = (request.POST['selectProcessor'])
			print(selectedProcessor)

			selectedOS = (request.POST['selectOS'])
			print(selectedOS)

			pFilter = True
			print('Filter = ' + str(pFilter))
		if request.POST.get('cFilter'):
			pFilter = False
			print('Filter = ' + str(pFilter))
	
	context = {
		'title':'Products',
		'products':products,
		'selectedOS':selectedOS,
		'selectedProcessor':selectedProcessor,
		'minPrice':int(minPrice),
		'maxPrice':int(maxPrice),
		'pFilter':pFilter,
		'processors':processors,
		'OSs':OSs
	}
	return render(request, 'products.html', context)

def details(request, id):
	products = Products.objects.get(id=id)
	
	context = {
		'products': products,
	}
	
	return render( request, 'details.html', context)