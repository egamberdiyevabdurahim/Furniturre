from django.views.generic import TemplateView, ListView

from products import models


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = models.ProductModel
    context_object_name = 'products'

    @staticmethod
    def get_colors():
        new_colors = list()
        colors = models.ColorModel.objects.all()
        temp_colors = list()

        for color in colors:
            if len(temp_colors) != 2:
                temp_colors.append(color)
            else:
                new_colors.append(temp_colors)
                temp_colors.clear()

        if len(temp_colors) == 1:
            new_colors.append(temp_colors)
        return new_colors

    def get_queryset(self):
        return models.ProductModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.CategoryModel.objects.all()
        context['tags'] = models.TagModel.objects.all()
        context['brands'] = models.BrandModel.objects.all()
        context['colors'] = self.get_colors()
        return context


class ProductDetailView(TemplateView):
    template_name = 'products/product-detail.html'


