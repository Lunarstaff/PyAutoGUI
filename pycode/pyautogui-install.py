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

>>> help(pag.typewrite)
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

"""