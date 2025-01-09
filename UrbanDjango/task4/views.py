from django.shortcuts import render

def main_page(request):
    return render(request, 'fourth_task/menu.html')

def shop_page(request):
    game_list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']
    return render(request, 'fourth_task/shop.html', {'game_list': game_list})

def cart_page(request):
    return render(request, 'fourth_task/cart.html')


