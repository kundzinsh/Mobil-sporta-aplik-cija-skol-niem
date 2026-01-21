mport tkinter as tk

users = {}  # username: password

def register():
    username = reg_user.get()
    password = reg_pass.get()
    users[username] = password
    print("Registered:", users)

def login():
    username = log_user.get()
    password = log_pass.get()
    if username in users and users[username] == password:
        print("Login successful")
    else:
        print("Login failed")

root = tk.Tk()
root.title("Login & Register")
root.geometry("250x220")

# Register
tk.Label(root, text="Register").pack()

reg_user = tk.Entry(root)
reg_user.pack()

reg_pass = tk.Entry(root)
reg_pass.pack()

tk.Button(root, text="Register", command=register).pack()

# Login
tk.Label(root, text="Login").pack()

log_user = tk.Entry(root)
log_user.pack()

log_pass = tk.Entry(root)
log_pass.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()