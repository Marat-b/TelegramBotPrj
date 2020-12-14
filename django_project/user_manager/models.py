from django.db import models


class TimedBaseModel(models.Model):
	class Meta:
		abstract = True
	
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class User(TimedBaseModel):
	class Meta:
		verbose_name = "Пользователь"
		verbose_name_plural = "Пользователи"
	
	id = models.AutoField(primary_key = True)
	user_id = models.BigIntegerField(verbose_name = "ID Пользователя Телеграм", unique = True, default = 1)
	
	name = models.CharField(verbose_name = "Имя пользователя", max_length = 100)
	username = models.CharField(verbose_name = "Username Телеграм", max_length = 100, null = True)
	bonus = models.DecimalField(verbose_name = "Бонус", decimal_places = 2, max_digits = 8)
	
	def __str__(self):
		return f"№{self.id} ({self.user_id}) - {self.name}"


class Product(TimedBaseModel):
	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"
	
	id = models.AutoField(primary_key = True)
	name = models.CharField(verbose_name = "Название товара", max_length = 50)
	photo = models.CharField(verbose_name = "Фото file_id", max_length = 200)
	price = models.DecimalField(verbose_name = "Цена", decimal_places = 2, max_digits = 8)
	description = models.TextField(verbose_name = "Описание", max_length = 3000, null = True)
	
	def __str__(self):
		return f"№{self.id} - {self.name}"


class Purchase(TimedBaseModel):
	class Meta:
		verbose_name = "Покупка"
		verbose_name_plural = "Покупки"
	
	id = models.CharField(primary_key = True, max_length = 50)
	buyer = models.ForeignKey(User, verbose_name = "Покупатель", on_delete = models.SET(0))
	product = models.ForeignKey(Product, verbose_name = "Идентификатор Товара", on_delete = models.CASCADE)
	amount = models.DecimalField(verbose_name = "Стоимость", decimal_places = 2, max_digits = 8)
	quantity = models.IntegerField(verbose_name = "Количество")
	shipping_address = models.CharField(verbose_name = "Адрес Доставки", max_length = 255, null = True)
	payed = models.BooleanField(verbose_name = "Оплачено", default = False)
	
	def __str__(self):
		return f"№{self.id} - {self.product_id} ({self.quantity})"
