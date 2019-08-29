#Создание ресторана
class Restaurant():
	'''Вывод информации о ресторане'''
	#Функция для конкретного экземпляра
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
		#Прямое изменение значения атрибута
		self.number_served = 0
		
	#Описание ресторана
	def describe_restaurant(self):
		print('Restaurant name is '+self.restaurant_name)
		print('Cuisine type is '+self.cuisine_type)
		
	#Информация об открытии ресторана
	def open_restaurant(self):
		print('Restaurant '+self.restaurant_name+
		' is open for visitors at the moment!')
	
	#Обновление количества посетителей	
	def served_upd(self, number):
		self.number_served = number
	
	#Приращение количества посетителей
	def served_inc(self, add_visiters):
		self.number_served += add_visiters
	
	#Вывод общего количества посетителей	
	def served(self):
		print('Number of visitors today: '+str(self.number_served))

#Создание кафе по продаже мороженого 
class IceCreamStand(Restaurant):
	'''Вывод информации о ресторане по продаже мороженного'''
	def __init__(self, restaurant_name, cuisine_type):
    #Проведение наследования родительского класса
		super().__init__(restaurant_name, cuisine_type)
    #Список добавок
		self.flavors = ['chocolate','pistachio','fruit','berry',
		'fried','standard','exotic']
    
	#Вывод списка на экран
	def info_ice_cream(self):
		print('This type of restaurant have a big choise of the'+ 
		' ice-creams: ')
		for flavor in self.flavors:
			print('\t-'+flavor.title())
 
#Примеры создания ресторанов с использованием вышеопределённых классов
restaurant = Restaurant('Harakiri', 'japanese')
#print('Restaurant name is '+restaurant.restaurant_name)
#print('Cuisine type is '+restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.served()
restaurant.served_upd(279)
restaurant.served()
restaurant.served_inc(21)
restaurant.served()
print('\n')

baskin_robbins = IceCreamStand('Baskin Robbins', 'american')
baskin_robbins.describe_restaurant()
baskin_robbins.open_restaurant()
baskin_robbins.info_ice_cream()
print('\n')

cafe = Restaurant('KFC','american')
cafe.describe_restaurant()
cafe.served_upd(1423)
cafe.served()
cafe.open_restaurant()
print('\n')

bar = Restaurant('Harats','britain')
bar.describe_restaurant()
bar.open_restaurant()
print('\n')
