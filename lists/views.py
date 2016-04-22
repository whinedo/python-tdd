from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lists.models import Item, List

# Create your views here.

@csrf_exempt
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'home.html')

@csrf_exempt
def view_list(request,list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'list.html',{'list':list_})

@csrf_exempt
def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'],list=list_)
	return redirect('/lists/%d/'%(list_.id,))

@csrf_exempt
def add_item(request,list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'],list=list_)
	return redirect('/lists/%d/'%(list_.id,))
