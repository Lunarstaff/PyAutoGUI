"""
PyAutoGUI的安装：
    -在Pycharm中项目解释器中安装
    -在系统环境解释器中安装：pip install pyautogui
    略...

导入pyautogui库：
    >>> import pyautogui as pag
    >>> dir(pag)
    ['FAILSAFE', 'FailSafeException', 'KEYBOARD_KEYS', 'KEY_NAMES',
    'MINIMUM_DURATION', 'MINIMUM_SLEEP', 'PAUSE', 'Window',
    '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
    '__name__', '__package__', '__path__', '__spec__', '__version__',
    '_autoPause', '_failSafeCheck', '_mouseMoveDrag', '_pyautogui_win',
    '_unpackXY', '_window_win', 'absolute_import', 'alert', 'center',
    'click', 'collections', 'confirm', 'displayMousePosition', 'division',
    'doubleClick', 'dragRel', 'dragTo', 'easeInBack', 'easeInBounce',
    'easeInCirc', 'easeInCubic', 'easeInElastic', 'easeInExpo',
    'easeInOutBack', 'easeInOutBounce', 'easeInOutCirc', 'easeInOutCubic',
    'easeInOutElastic', 'easeInOutExpo', 'easeInOutQuad', 'easeInOutQuart',
    'easeInOutQuint', 'easeInOutSine', 'easeInQuad', 'easeInQuart', 'easeInQuint',
    'easeInSine', 'easeOutBack', 'easeOutBounce', 'easeOutCirc', 'easeOutCubic',
    'easeOutElastic', 'easeOutExpo', 'easeOutQuad', 'easeOutQuart', 'easeOutQuint',
    'easeOutSine', 'getPointOnLine', 'getWindow', 'getWindows', 'grab', 'hotkey',
    'hscroll', 'isShiftCharacter', 'isValidKey', 'keyDown', 'keyUp', 'linear',
    'locate', 'locateAll', 'locateAllOnScreen', 'locateCenterOnScreen', 'locateOnScreen',
    'middleClick', 'mouseDown', 'mouseUp', 'moveRel', 'moveTo', 'onScreen', 'password',
    'pixel', 'pixelMatchesColor', 'platformModule', 'position', 'press', 'print_function',
    'prompt', 'pymsgbox', 'pyscreeze', 'pytweening', 'rightClick', 'screenshot', 'scroll',
    'size', 'sys', 'time', 'tripleClick', 'typewrite', 'vscroll']

    >>> screenWidth,screenHeigth = pag.size() # 获取屏幕分辨率，返回一个元组
    >>> screenWidth,screenHeigth
    (1920, 1080)

    >>> pag.moveTo(screenWidth / 2, screenHeigth / 2) # 移动光标到指定坐标位置，屏幕左上为(0, 0)，右下为(1920, 1080)

    >>> folder = pag.position() #获取当前光标位置的坐标
    >>> folder
    (214, 1057)
    >>> pag.moveTo(folder) #移动光标到指定位置
    >>> pag.click() #单击

    >>> pag.moveRel(None,20) #光标向下移动 20 像素

    >>> pag.doubleClick() #双击

    >>> help(pag.moveTo)
    Help on function moveTo in module pyautogui:

    moveTo(x=None, y=None, duration=0.0, tween=<function linear at 0x00000144B672E840>, pause=None, _pause=True)
        Moves the mouse cursor to a point on the screen.

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        Args:
          x (int, float, None, tuple, optional): The x position on the screen where the
            click happens. None by default. If tuple, this is used for x and y.
          y (int, float, None, optional): The y position on the screen where the
            click happens. None by default.
          duration (float, optional): The amount of time it takes to move the mouse
            cursor to the xy coordinates. If 0, then the mouse cursor is moved
            instantaneously. 0.0 by default.
          tween (func, optional): The tweening function used if the duration is not
            0. A linear tween is used by default. See the tweens.py file for
            details.

        Returns:
          None

    >>> pag.moveTo(500, 500, duration=2, tween=pag.easeInOutQuad)
# use tweening/easing function to move mouse over 2 seconds.
# 使用渐变功能让光标在2s内移动到指定位置

    >>> help(pag.typewrite) # 光标所在位置要是可编辑的才有效果
    Help on function typewrite in module pyautogui:

    typewrite(message, interval=0.0, pause=None, _pause=True)
        Performs a keyboard key press down, followed by a release, for each of
        the characters in message.

        The message argument can also be list of strings, in which case any valid
        keyboard name can be used.

        Since this performs a sequence of keyboard presses and does not hold down
        keys, it cannot be used to perform keyboard shortcuts. Use the hotkey()
        function for that.

        Args:
          message (str, list): If a string, then the characters to be pressed. If a
            list, then the key names of the keys to press in order. The valid names
            are listed in KEYBOARD_KEYS.
          interval (float, optional): The number of seconds in between each press.
            0.0 by default, for no pause in between presses.

        Returns:
          None

按键操作：
    >>> pag.press('capslock') # 按一下 capslock 键，具体的键值参见：KEYBOARD_KEYS

    >>> pag.KEYBOARD_KEYS
    ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
    '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept',
    'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback',
    'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh',
    'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl',
    'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down',
    'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12',
    'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22',
    'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn',
    'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana',
    'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect',
    'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0',
    'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9',
    'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause',
    'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return',
    'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright',
    'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute',
    'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

使用 pag.press('键值')，传入对应的键值。
单独的按下、弹起操作：一梓传入对应的键值，出下按键按下或弹出的操作。
pag.keyDown("键值")
pag.keyUp("键值")

    >>> pag.keyDown("shift") # 保持shift 键按下
    >>> pag.keyUp("shift") # shift 弹起


快捷键功能：hotkey()
the hotkey() can be passed several key strings which
will be pressed down in order, and then released in reverse order
可以按照传入的一系列键值顺序按下对应按键，并按相反的顺序弹起（释放）。

    >>> pag.hotkey("ctrl","shift","esc")
相当于：
    >>> pag.keyDown("ctrl")
    >>> pag.keyDown("shift")
    >>> pag.keyDown("esc")
    >>> pag.keyUp("esc")
    >>> pag.keyUp("shift")
    >>> pag.keyUp("ctrl")

Message Box Functions
消息框功能：

The alert() Function
警告提示框：
    >>> pag.alert(text='这是个alert',title='这个是alert的title',button='OK')
就会弹出一个 标题为“这个是alert的title”，提示框内容为“这是个alert”，且有一个“OK”按钮的警告提示框。
点“OK”按钮后，返回“OK”字符串。
    >>> test = pag.alert(text='这是个alert',title='这个是alert的title',button='OK')
    >>> test
    'OK'

The confirm() Function
确认提示框：

弹出一个提示框内容为“存在疑问***，请确认”，标题为“这个是confirm提示框”，且有一个OK确认按钮和一个Cancel取消按钮的提示框，
点“Cancel”按钮后，返回“Cancle”字符串
    >>> cofirm = pag.confirm(text="存在疑问***，请确认", title='这个是confirm提示框',buttons=["OK", "Cancel"])
    >>> cofirm
    'Cancel'


    >>> pro = pag.prompt(text="", title="", default='')
    >>> pro
    '这个是prompt提示框输入的内容'

弹出一个提示框内容为“这个是Prompt的text”，标题为“这个是Prompt的tltle”，一个有默认值为“这个是Prompt的Default”的文本编辑框
且有一个OK确认按钮和一个Cancel取消按钮的提示框，
点“Cancel”按钮后，返回文本编辑框中的字符串
    >>> pro = pag.prompt(text="这个是Prompt的text", title="这个是Prompt的tltle", default='这个是Prompt的Default')
    >>> pro
    '这个是Prompt的Default'

The password() Function
密码输入框：
    >>> pas = pag.password(text="", title="", default="", mask='')
    >>> pas
    '12345rt@#$'
弹出一个标题为“密码输入提示框的tlttle”，提示框内容为“密码输入提示框的text”，一个无默认值的密码输入文本框且有一个OK确认按钮和一个Cancel取消按钮的密码输入提示框
输入密码后，以“$”符号为标记，点OK确定后，返回密码输入文本框中的值，点取消后不返回值。
    >>> pas = pag.password(text="密码输入提示框的text", title="密码输入提示框的tlttle", default="", mask='$')
    >>> pas
    '123456'

Screenshot Functions
截图功能：

The screenshot() Function
    >>> tubar1 = pag.screenshot()
    >>> tubar1
    <PIL.Image.Image image mode=RGB size=1920x1080 at 0x245B81E6048>

切换工作目录：
    >>> import os
    >>> os.chdir("./FIles")
    >>> os.getcwd()
    'C:\\E-Data-File\\腾讯课堂\\Python入门\\PyAutoGUI\\FIles'
获取截图：
    >>> pubar1 = pag.screenshot("./pubar1.png")
    >>> os.listdir()
    ['password()-demo-1.png', 'password()-demo-2.png', 'prompt()-demo.png', 'screenshot()-demo-1.png', 'tubar1.png']

按给定区域获取截图：（获取当前的任务栏，区域为 1919，39）
屏幕大小为(1920, 1080)
所以，任务栏区域为：0，1079-39，1919，39
0,1040,1919,1079
    >>> tubar2 = pag.screenshot("./tubar2.png", region = (0,1040,1919,39))
# 区域设置为（x1,y1,δ1,δ2）,其中x1,y1设置为获取截图的左上点，δ1,δ2设置为截图的长和高。
    >>> tubar2
    <PIL.Image.Image image mode=RGB size=1919x1079 at 0x26478B95F28>
    >>> os.listdir()
    ['password()-demo-1.png', 'password()-demo-2.png', 'prompt()-demo.png', 'screenshot()-demo-1.png', 'tubar1.png', 'tubar2.png']

The Locate Functions

图像定位方法：
根据已有的图像对象，找到界面上对应的位置并返回定位到的区域（返回格式为：）
再根据返回的区域信息，执行鼠标及键盘操作。
下面演示，根据已有的Win图标找到Win键的位置并点击，打开Win10开始菜单。

    # 找到Win键的区域
    >>> Win_button_location = pag.locateOnScreen("./Win10-button-WinKey.png", region = (0,1040,1919,39))
    >>> Win_button_location
    (3, 1044, 43, 33)
    # 计算找到的Win键区域的中位点
    >>> Win_button_center = pag.center(Win_button_location)
    >>> Win_button_center
    (24, 1060)
    # 单击
    >>> pag.click(Win_button_center)

有可以根据已有对象的图像，找到界面上对应的位置，并直接返回中位点信息的方法：
    >>> Win_button_center = pag.locateCenterOnScreen('./Win10-button-WinKey.png')
为了快速定位，可以通过 regin参数传入区域信息设置扫描区域
    >>> Win_button_center = pag.locateCenterOnScreen('./Win10-button-WinKey.png', region = (0,1040,1919,39))
    >>> Win_button_center
    (24, 1060)

Pixel Matching
像素匹配：

To obtain the RGB color of a pixel in a screenshot, use the Image object’s getpixel() method
使用 图像对象的 getpixel() 方法获取图像上指定点的像素RGB颜色信息。
    >>> im = pag.screenshot(region = (1450,194,50,50))
    >>> im.getpixel(20,20)
    >>> im.getpixel((20,20))
    (64, 64, 64)
或者直接调用getpixel()方法，获取当前屏幕指定点的像素颜色RGB信息
>>> pag.pixel(321,1052)
(14, 170, 255) #任务栏中遨游浏览器图标蓝色

判断当前屏幕指定点的像素颜色是否与给定的颜色相同：
>>> pag.pixelMatchesColor(321,1052,(14, 170, 255))
True
>>> pag.pixelMatchesColor(321,1052,(14, 155, 255))
False

可通过设置色差偏移量来放宽比较：
>>> pag.pixelMatchesColor(321,1052,(14, 160, 255))
False
>>> pag.pixelMatchesColor(321,1052,(14, 160, 255), tolerance = 10) #允许色差偏移量为10
True
>>> pag.pixelMatchesColor(321,1052,(14, 160, 245), tolerance = 10)
True
>>> pag.pixelMatchesColor(321,1052,(14, 160, 235), tolerance = 10)
False

测试模块：
PyAutoGUI常用的方法：
• onScreen()
• size()
• position()
• moveTo()
• moveRel()
• typewrite()
• PAUSE

其他的GUI模块：
PyUserInput
PyKeyboard
PyMouse
pykey
Sikuli




Window handling features
Windows窗口处理功能：

>>> wins = pag.getWindows() # 获取当前所有Windows的窗口对象，以字典类型返回
>>> wins
{'': <ctypes.wintypes.LP_c_long object at 0x0000026400C5ADC8>,
'Python Console - PyAutoGUI': <ctypes.wintypes.LP_c_long object at 0x0000026400C5AAC8>,
'PyAutoGUI [C:\\E-Data-File\\腾讯课堂\\Python入门\\PyAutoGUI] - ...\\pycode\\pyautogui-install.py [PyAutoGUI] - PyCharm': <ctypes.wintypes.LP_c_long object at 0x0000026400C5ACC8>,
'pyautogui.pdf - Gaaiho Reader': <ctypes.wintypes.LP_c_long object at 0x0000026400C5A748>,
'计算器 \u200e- 计算器': <ctypes.wintypes.LP_c_long object at 0x0000026400C5A948>,
'设置': <ctypes.wintypes.LP_c_long object at 0x0000026400C5AC48>,
'Microsoft Edge': <ctypes.wintypes.LP_c_long object at 0x0000026400C5A8C8>,
'中国大学MOOC(慕课)_优质在线课程学习平台 - 傲游5 5.1.5.2000 - max5': <ctypes.wintypes.LP_c_long object at 0x0000026400C5A848>,
'邮件': <ctypes.wintypes.LP_c_long object at 0x0000026400C5A9C8>,
'收件箱 - 163-Lunar12 \u200e- 邮件': <ctypes.wintypes.LP_c_long object at 0x0000026400C5AA48>,
'MI Hotkey Utility': <ctypes.wintypes.LP_c_long object at 0x0000026400C5AB48>,
'金山词霸2016': <ctypes.wintypes.LP_c_long object at 0x0000026400C5A7C8>,
'Files': <ctypes.wintypes.LP_c_long object at 0x0000026400C5A648>,
'Program Manager': <ctypes.wintypes.LP_c_long object at 0x0000026400C5AD48>}


>>> win_cal = pag.getWindow(title="计算器") # 获取标题（title）为“计算器”的Windows窗口，产生一个Win对象
>>> win_cal
<pyautogui._window_win.Window object at 0x000002647943DC18>
>>> dir(win_cal) # Win对象的dir
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'_hwnd',
'close', 'get_position', 'maximize', 'minimize', 'move',
'resize', 'restore', 'set_foreground', 'set_position']

>>> win_cal.get_position() # 获取对象的位置信息（格式为：x1,y1,x2,y2）,返回窗口左上角的点和右下角点的坐标
(238, 262, 574, 802)

>>> win_cal.position() # returns (x, y) of top-left corner (文档上说的有这个方法，实际上没有。)

>>> win_cal.maximize() # 使窗口最大化，再次执行不能还原
>>> win_cal.minimize() # 使已经最大化的窗口，最小化到任务栏

>>> win_cal.move(50,200) # 移动窗口 ,绝对坐标移动：将窗口左上点移动到屏幕的（50，200）位置处。
>>> win_cal.moveRel(x=0, y=0) # moves relative to the x, y of top-left corner of the window (文档上说的有这个方法，实际上没有。)


>>> win_cal.clickRel(x=0, y=0, clicks=1, interval=0.0, button=’left’)
# click relative to the x, y of top-left corner of the window (文档上说的有这个方法，实际上没有。)


>>> win_cal.resize(500,800) # 设置窗口大小为（500X800），宽为500，高为800

>>> win_cal.close() # 关闭窗口（实际上并没有关闭，只是释放了窗口对象）





"""