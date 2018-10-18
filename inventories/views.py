from django.shortcuts import render
from .models import Inventory
# Create your views here.
def inventory_list(request):
	
    context = {
        "inventories": Inventory.objects.all()
    }
    return render(request, 'inventory_list.html', context)