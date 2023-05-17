from django.db import models


class Products(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(max_length=150, verbose_name='Название')
    model = models.CharField(max_length=50, verbose_name='Модель')
    release = models.DateField(verbose_name='Дата выпуска')

    def __str__(self):
        return f'{self.title} {self.model}'


class Company(models.Model):
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    class Level(models.IntegerChoices):
        factory = 1, 'Завод'
        distributor = 2, 'Дистрибьютор'
        dealer = 3, 'Дилер'
        retailer = 4, 'Розничная сеть'
        individual_entrepreneur = 5, 'Индивидуальный предприниматель'

    title = models.CharField(max_length=30, verbose_name='Название компании')
    level = models.PositiveSmallIntegerField(verbose_name='Вид компании', choices=Level.choices)
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')
    country = models.CharField(max_length=20, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    user = models.ForeignKey('users.User', verbose_name='Сотрудник', on_delete=models.CASCADE)
    provider = models.ForeignKey('self', verbose_name='Поставщик', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class CompanyProducts(models.Model):
    """
    Many-to-many связь через отдельную таблицу.
    Для удобства вывода в админ-панели товаров в несколько строк.
    """

    class Meta:
        verbose_name = 'Товар Компании'
        verbose_name_plural = 'Продукт Компании'

    products = models.ForeignKey('Products', verbose_name='Продукция', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', verbose_name='Компания', on_delete=models.CASCADE)
