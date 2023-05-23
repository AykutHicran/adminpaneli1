from django.shortcuts import render

def product(request, pk=None):
    
    return render(request=request, template_name='product/detail.html', context = {'pk:pk'})
    
def  products(request):
    return render(request=request, template_name='product/list.html')


def  product_archieve(request):
    return render(request=request, template_name='product/archieve.html')
                