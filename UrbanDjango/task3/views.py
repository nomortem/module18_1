from django.shortcuts import render

def main_page(request):
    return render(request, 'third_task/main.html')

def shop_page(request):
    game_list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']  # Проще без описаний
    return render(request, 'third_task/shop.html', {'game_list': game_list})

def cart_page(request):
    return render(request, 'third_task/cart.html')