from django import template

register = template.Library()


@register.filter
def in_cart(request, pk):
    return pk in request.session.get('cart', [])
