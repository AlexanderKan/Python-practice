print("Q to quit")
n = 0
user_input = ""
step_size = 1
while (1):
	print("Your number is " + str(n))
	user_input = input("(+/-) to inc or dec: ")
	if (user_input.lower() == "q"):
		break
	elif (user_input.lower() == "c"):
		temp_size = int(input("New step size: "))
		if (temp_size >0):
			step_size = temp_size
		else:
			print("Step size should not be negative")
	elif (user_input == "+"):
		n = n + step_size
	elif (user_input == "-"):
		if (n - step_size < 0):
			n = 0
			continue
		else:
			n = n - step_size
	else:
		print("Invalid input")


