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




"""