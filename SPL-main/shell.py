import main

while True:
	text = input('prompt > ')
	result, error = main.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)
