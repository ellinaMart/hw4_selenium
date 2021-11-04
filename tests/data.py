import random


test_admin = {'login': "demo", 'password': "demo"}
test_user = {'login': "ivan@test.ru", 'password': "Ivan12"}
new_test_user = {'login': "ivan+%s@test.ru"%random.randint(0,100),
                 'password': "Ivan12",
                 'name': "Ivan",
                 'lastname': "Ivaniv",
                 'phone': "+79271234567"}