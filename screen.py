import tkinter
import config

def click(e):
    pass

def main():
    # 清除左侧主界面的内容
    cvs.delete("main_area")

    # 绘制左侧白色主界面
    cvs.create_rectangle(0, 0, config.width - 300, config.height, fill="white", width=2, tags="main_area")

    # 更新右侧黑色信息区域（假设右侧区域的宽度为300）
    update_info_area()

    # 继续循环调用 main()，实现周期性更新
    #root.after(100, main)

def update_info_area():
    # 清除右侧信息区域的内容
    cvs.delete("info_area")

    # 绘制右侧黑色信息区域的内容，例如状态、物品等信息
    # 以下是示例代码，你需要根据具体需求来绘制状态和物品信息
    info_text = "Player Status:\nHealth: 100\nMana: 50\nLevel: 5"
    cvs.create_text(config.width - 150, 50, anchor="nw", text=info_text, fill="white", font=("Arial", 12), tags="info_area")

    # 可以继续添加其他需要显示的信息

root = tkinter.Tk()
root.title("RPG GAME")
root.resizable(False, False)
root.bind("<Button>", click)

# 创建Canvas，宽度为config.width，高度为config.height
cvs = tkinter.Canvas(width=config.width, height=config.height, bg="black")
cvs.pack()

# 启动主循环
root.after(100, main)
root.mainloop()
