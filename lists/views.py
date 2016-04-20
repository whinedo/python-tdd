from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lists.models import Item

# Create your views here.

@csrf_exempt
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'home.html')

@csrf_exempt
def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html',{'items':items})

@csrf_exempt
def new_list(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')
