import tkinter as tk
from tkinter import messagebox

# 预设用户信息
users = {
    "mike": "m12345",
    "jack": "j12345"
}

# 登录按钮点击事件
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        label_result.config(text=f"欢迎您，{username}", fg="green")
    else:
        label_result.config(text="用户名或密码错误", fg="red")

# 创建主窗口
root = tk.Tk()
root.title("登录界面")
root.geometry("300x200")

# 用户名标签和输入框
label_username = tk.Label(root, text="用户名：")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# 密码标签和输入框
label_password = tk.Label(root, text="密码：")
label_password.pack()
entry_password = tk.Entry(root, show="*")  # show="*" 表示输入时显示为星号
entry_password.pack()

# 登录按钮
button_login = tk.Button(root, text="登录", command=login)
button_login.pack()

# 显示结果
label_result = tk.Label(root, text="")
label_result.pack()

# 启动主循环
root.mainloop()