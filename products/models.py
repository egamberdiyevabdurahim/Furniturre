from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class CategoryModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Category name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class TagModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Tag name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class BrandModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Brand name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class ColorModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Color name"))
    code = models.CharField(max_length=128, verbose_name=_("Color code"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")


class SizeModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Size name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")


class ProductModel(BaseModel):
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=128, verbose_name=_("Product name"))
    short_description = models.TextField()
    long_description = models.TextField()
    is_stock = models.BooleanField(verbose_name=_("Is stock"), default=True)
    sku = models.CharField(max_length=10, unique=True)
    quantity = models.PositiveIntegerField(default=1)
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    real_price = models.DecimalField(max_digits=10, decimal_places=2)

    categories = models.ManyToManyField(CategoryModel, related_name='products')
    tags = models.ManyToManyField(TagModel, related_name='products')
    sizes = models.ManyToManyField(SizeModel, related_name='products')
    colors = models.ManyToManyField(ColorModel, related_name='products')

    brands = models.ForeignKey(BrandModel, related_name='products', on_delete=models.CASCADE)

    def is_discount(self):
        return True if self.discount != 0 else False

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')
