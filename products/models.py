from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام محصول")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")
    stock = models.PositiveIntegerField(verbose_name="موجودی انبار")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")

    def __str__(self):
        return self.name
