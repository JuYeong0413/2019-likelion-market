from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
import pdb

# Create your views here.
def main(request):
    items = Item.objects.all()
    return render(request, 'items/main.html', {'items': items})
    
    
# 상품 상세보기 페이지
def show(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'items/show.html', {'item': item})
    
    
# 관심상품 목록
def favourite(request):
    user = request.user
    items = Item.objects.filter(favourites = user)
    return render(request, 'items/favourite.html', {'items': items})
    
    
# 관심상품 등록
def like(request, id):
    user = request.user
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        if item.favourites.filter(id = user.id).exists():
            item.favourites.remove(user)
        else:
            item.favourites.add(user)
    return redirect('items:show', item.id)
    
    
# 관심상품 해제
def unlike(request, id):
    user = request.user
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        item.favourites.remove(user)
    return redirect('items:favourite')
    
    
# 구매하기 (1개)
def single_order(request):
    user = request.user
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = Item.objects.get(id=item_id)
        total_price = item.price
        order = Order.objects.create(user=user, total_price=total_price)
        order.items.add(item)
        
        default_bought = item.bought
        item.bought = default_bought + 1
        item.cart.remove(user)
        item.save()
        
    return render(request, 'items/order_success.html', {'order': order})
    
    
# 구매하기 (2개 이상)
def order(request):
    user = request.user
    if request.method == 'POST':
        var = request.POST.getlist('item')
        items = []
        if '1' in var:
            items.append("돌")
        if '2' in var:
            items.append("MacBook Air")
        if '3' in var:
            items.append("MacBook Pro")
        if '4' in var:
            items.append("iMac")
        if '5' in var:
            items.append("Magic Mouse")
        if '6' in var:
            items.append("Magic Trackpad")
        if '7' in var:
            items.append("AirPods")
        if '8' in var:
            items.append("iPad Pro")
        if '9' in var:
            items.append("Apple Pencil")
        if '10' in var:
            items.append("Magic Keyboard")
            
        order = Order.objects.create(user=user)
        
        for item_name in items:
            item = Item.objects.get(name=item_name)
            order.items.add(item)
            default_price = order.total_price
            order.total_price = default_price + item.price
            order.save()
            
            default_bought = item.bought
            item.bought = default_bought + 1
            item.cart.remove(user)
            item.save()
    return render(request, 'items/order_success.html', {'order': order})
    
    
# 장바구니에 상품 추가
def cart_success(request):
    user = request.user
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, pk=item_id)
        if item.cart.filter(id = user.id).exists():
            None
        else:
            item.cart.add(user)
    return render(request, 'items/cart_success.html')
    
    
# 장바구니
def cart(request):
    user = request.user
    items = Item.objects.filter(cart = user)
    return render(request, 'items/cart.html', {'items': items})
    
    
# 장바구니에서 상품 삭제
def cart_delete(request):
    user = request.user
    if request.method == 'POST':
        var = request.POST.getlist('item')
        items = []
        if '1' in var:
            items.append("돌")
        if '2' in var:
            items.append("MacBook Air")
        if '3' in var:
            items.append("MacBook Pro")
        if '4' in var:
            items.append("iMac")
        if '5' in var:
            items.append("Magic Mouse")
        if '6' in var:
            items.append("Magic Trackpad")
        if '7' in var:
            items.append("AirPods")
        if '8' in var:
            items.append("iPad Pro")
        if '9' in var:
            items.append("Apple Pencil")
        if '10' in var:
            items.append("Magic Keyboard")
            
        for item_name in items:
            item = Item.objects.get(name=item_name)
            item.cart.remove(user)
            
    return redirect('items:cart')
    
    
# 주문내역
def buylist(request):
    user = request.user
    orders = Order.objects.filter(user = user)
    return render(request, 'items/buylist.html', {'orders': orders})
    
    
# 후기 작성 페이지
def write_review(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
    return render(request, 'items/write_review.html', {'order': order})
    
    
# 후기 작성
def create_review(request):
    user = request.user
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        content = request.POST.get('content')
        star = request.POST.get('star')
        review = Review(content=content, star=star, user=user, order=order)
        review.save()
        
        order.review_written = True
        order.save()
        
    return redirect('items:review')
    
    
# 후기 목록
def review(request):
    reviews = Review.objects.all()
    return render(request, 'items/review.html', {'reviews': reviews})