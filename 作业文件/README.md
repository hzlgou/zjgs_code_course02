✅ 第一步：确认你已经安装好 Python
检查是否已安装 Python：
打开终端（Windows 可用 CMD 或 PowerShell），输入：
bash
复制
python --version
如果返回类似于：
Python 3.x.x
说明你已经安装好了。如果提示找不到命令，请先安装 Python：
👉 安装地址：https://www.python.org/downloads/
安装时务必勾选 “Add Python to PATH”。
✅ 第二步：创建项目文件夹
在你电脑任意位置新建一个文件夹，比如叫：
login_app
然后在该文件夹里新建一个文件：
login.py
✅ 第三步：编写登录程序代码
用记事本、VS Code、PyCharm 等任意编辑器打开 login.py，粘贴以下代码：
Python
复制
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
✅ 第四步：运行程序
在终端（或命令提示符）中进入你创建的 login_app 文件夹，然后运行：
bash
复制
python login.py
你应该会看到一个窗口，输入用户名和密码后点击“登录”，下方会显示对应提示。
✅ 第五步：测试一下
输入用户名 mike，密码 m12345 → 应该显示：欢迎您，mike
输入用户名 jack，密码 j12345 → 应该显示：欢迎您，jack
输入错误的用户名或密码 → 应该显示：用户名或密码错误
✅ 总结
你现在完成了：
✅ 安装 Python
✅ 创建项目文件夹
✅ 用 Tkinter 写了一个图形界面登录程序
✅ 运行并测试成功
