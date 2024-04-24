from django.db import models


class Check(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True, verbose_name='Идентификатор')
    timestamp = models.DateTimeField(verbose_name="Дата и время")
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Общая сумма чека')
    nds_amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Сумма НДС')
    tips_amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Сумма чаевых',
                                      null=True, blank=True)
    payment_method = models.CharField(max_length=35, verbose_name='Метод оплаты')
    place = models.ForeignKey('Place', on_delete=models.SET_NULL, verbose_name='Продукт', null=True, blank=True)

    def __str__(self):
        return self.transaction_id

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"


class Product(models.Model):
    product_id = models.CharField(max_length=100, unique=True, verbose_name='Идентификатор')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductCheck(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    check_obj = models.ForeignKey(Check, on_delete=models.CASCADE, verbose_name='Чек', related_name='items')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.product} in {self.check}: {self.quantity}'

    class Meta:
        verbose_name = "Продукт в чеке"
        verbose_name_plural = "Продукты в чеках"


class Category(models.Model):
    name = models.CharField(max_length=35, verbose_name="Название", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Place(models.Model):
    place_id = models.CharField(max_length=100, verbose_name='Идентификатор')
    place_name = models.CharField(max_length=35, verbose_name='Название')

    def __str__(self):
        return self.place_id

    class Meta:
        verbose_name = "Место покупки"
        verbose_name_plural = "Места покупок"
