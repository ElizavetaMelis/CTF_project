from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from applications.product.models import Product, Category, Difficulty


class ProductListView(ListView):
    paginate_by = 4
    model = Product
    template_name = 'product_page.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['difficulties'] = Difficulty.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        if category is not None:
            queryset = queryset.filter(category_id=category)
        return queryset

def product_page(request):
    products = Product.objects.all()
    return render(request, "product_page.html", {"products": products})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        rating = 0
        context['rating'] = rating
        return context
