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
		'pFilter':pFilter
	}
	return render(request, 'products.html', context)

def details(request, id):
	products = Products.objects.get(id=id)
	
	context = {
		'products': products,
	}
	
	return render( request, 'details.html', context)