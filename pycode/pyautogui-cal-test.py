"""
使用PyAutoGUI 调用计算器执行计算
# 找到计算器图标位置
# 打开计算器并初始化
# 执行计算
"""


import pyautogui as pag
cal_png = "../Files/Win10-tubar-cal.png"

# 找到计算器图标位置
def findImageOnScreen(mi_png):
    """
    根据传入的图像信息找到在当前界面上的位置，返回该对应图像的中位点
    :param mi_png:目标图像
    :return:对应图像的中位点，元组类型
    """
    mi_png_center = pag.locateCenterOnScreen(mi_png)
    return mi_png_center


# 打开计算器并初始化
def clickOn_a_point(point):
    """
    在指定的点上单击鼠标左键
    :param point:给定的点，元组类型point(x,y)
    :return:Windows窗口对象
    """
    pag.click(point[0], point[1])
    app_name = pag.getWindow(title="计算器")
    app_name.set_position(0,0,600,800)
    return app_name

# 执行计算
# def cal_numadd()

def main():
    clickOn_a_point(findImageOnScreen(cal_png))
    return

main()
