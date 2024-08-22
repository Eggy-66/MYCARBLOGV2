from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Message
from .forms import ItemForm, MessageForm
from django.core.paginator import Paginator

from django.urls import reverse_lazy

def item_list(request):
    items = Item.objects.all()
    model = request.GET.get('model')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    cabin_type = request.GET.get('cabin_type')
    fuel = request.GET.get('fuel')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    if model:
        items = items.filter(model__icontains=model)
    if year_min:
        items = items.filter(year__gte=year_min)
    if year_max:
        items = items.filter(year__lte=year_max)
    if cabin_type:
        items = items.filter(cabin_type=cabin_type)
    if fuel:
        items = items.filter(fuel=fuel)
    if price_min:
        items = items.filter(price__gte=price_min)
    if price_max:
        items = items.filter(price__lte=price_max)
    paginator = Paginator(items, 15)  # Show 24 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/item_list.html', {'page_obj': page_obj})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    message_form = MessageForm()
    return render(request, 'shop/item_detail.html', {'item': item, 'message_form': message_form})



def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('shop:item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'shop/item_update.html', {'form': form})

def item_confirm_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('shop:item_list')
    return render(request, 'shop/item_confirm_delete.html', {'item': item})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('shop:item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'shop/add_item.html', {'form': form})

@login_required
def send_message(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = item.owner
            message.item = item
            message.save()
            return redirect('shop:item_detail', pk=item.pk)
    return redirect('shop:item_detail', pk=item.pk)
