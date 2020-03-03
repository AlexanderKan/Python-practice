print("Q to quit")
n = 0
user_input = ""
while (1):
	print("Your number is " + str(n))
	user_input = input("(+/-) to inc or dec: ")
	if (user_input.lower() == "q"):
		break
	elif (user_input == "+"):
		n = n+1
	elif (user_input == "-"):
		if (n-1 < 0):
			continue
		else:
			n = n-1
	else:
		print("Invalid input")


