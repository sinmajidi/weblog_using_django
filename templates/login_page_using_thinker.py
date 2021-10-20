# import modules

from tkinter import *
import os
import requests
# defining the api-endpoint
API_ENDPOINT = "http://cybele.ir/login.php"
# Designing window for registration

def register():
	global register_screen
	register_screen = Toplevel(main_screen)
	register_screen.title("Register")
	register_screen.geometry("300x250")

	global username
	global password
	global username_entry
	global password_entry
	username = StringVar()
	password = StringVar()

	Label(register_screen, text="Please enter details below", bg="blue").pack()
	Label(register_screen, text="").pack()
	username_lable = Label(register_screen, text="Username * ")
	username_lable.pack()
	username_entry = Entry(register_screen, textvariable=username)
	username_entry.pack()
	password_lable = Label(register_screen, text="Password * ")
	password_lable.pack()
	password_entry = Entry(register_screen, textvariable=password, show='*')
	password_entry.pack()
	Label(register_screen, text="").pack()
	Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():
	global login_screen
	login_screen = Toplevel(main_screen)
	login_screen.title("Login")
	login_screen.geometry("300x250")
	Label(login_screen, text="Please enter details below to login").pack()
	Label(login_screen, text="").pack()

	global username_verify
	global password_verify

	username_verify = StringVar()
	password_verify = StringVar()

	global username_login_entry
	global password_login_entry

	Label(login_screen, text="Username * ").pack()
	username_login_entry = Entry(login_screen, textvariable=username_verify)
	username_login_entry.pack()
	Label(login_screen, text="").pack()
	Label(login_screen, text="Password * ").pack()
	password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
	password_login_entry.pack()
	Label(login_screen, text="").pack()
	Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
	username_info = username.get()
	password_info = password.get()

	file = open(username_info, "w")
	file.write(username_info + "\n")
	file.write(password_info)
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
	# your API key here
	print(username_verify.get())
	print(password_verify.get())
	uusername = username_verify.get()

	# your source code here
	ppassword = password_verify.get()

	# data to be sent to api
	data = {'user': uusername,
	        'pass': ppassword
	        }

	# sending post request and saving response as response object
	r = requests.post(url=API_ENDPOINT, data=data)

	print(r.content)

# Designing popup for login success

def login_sucess():
	  pass

# Designing popup for login invalid password

def password_not_recognised():
		pass


# Designing popup for user not found

def user_not_found():
	  pass


# Deleting popups

def delete_login_success():
	pass

def delete_password_not_recognised():
	pass


def delete_user_not_found_screen():
	pass


# Designing Main(first) window

def main_account_screen():
	global main_screen
	main_screen = Tk()
	main_screen.geometry("300x250")
	main_screen.title("Account Login")
	Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
	Label(text="").pack()
	Button(text="Login", height="2", width="30", command=login).pack()
	Label(text="").pack()
	Button(text="Register", height="2", width="30", command=register).pack()

	main_screen.mainloop()


main_account_screen()