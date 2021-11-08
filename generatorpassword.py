import random

ListR = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
		 'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

def start():

	nubmer = int(input('Кол-во паролей: '))
	lenght = int(input('Длина строки: '))
	print(' ')

	for x in range(nubmer):
		password = ''

		for i in range(lenght):
			password += random.choice(ListR)

		print(password)

		file = open('password.txt', 'a')
		file.write('\n' + password)
		file.close()

while True:
	start()
