import win32gui
import pymouse
import pykeyboard
import time

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'Heroes of the Storm' in win32gui.GetWindowText(hwnd):           
            win32gui.MoveWindow(hwnd, 0, 0, 1200, 760, True)
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y


def main():    
    # resize the window to standard 1200 * 760
    win32gui.EnumWindows(enumHandler, None)
    m = pymouse.PyMouse()
    k = pykeyboard.PyKeyboard()
    while (True):
        change_option(m)
        mouse_menu(m)
        end_game_control(m)
        side = check_side()
        ingame_control(m,k,side)
        time.sleep(2)
    
    
   
def change_option(m):
    m.click(1100,730)
    m.click(1100,575)
    m.click(200,240)
    m.click(950,150)
    m.click(480,680)

def mouse_menu(m):
     m.click(50,100)
     m.click(65,510)
     m.click(100,580)
     m.click(600,700)

def check_side():
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, 490,60)
    i_colour = int(long_colour)
    t = (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)
    win32gui.ReleaseDC(i_desktop_window_id, i_desktop_window_dc)
    if t[1] > 200:
        return "left"
    else:
        return "right"

def ingame_control(m,k,side):
    m.click(600,350)
    k.press_key(k.control_key)
    k.press_key('1')
    k.release_key(k.control_key)
    k.release_key('1')
    if side == "left":  
        k.press_key(k.control_key)
        k.release_key(k.control_key)
        k.tap_key(k.space_key) 
        time.sleep(0.2)
        m.move(1000,400)
        m.click(1000,400)
        k.press_key('a')
        m.click(1000,400)
        k.release_key('a')
    else:
        k.press_key(k.control_key)
        k.release_key(k.control_key)
        k.tap_key(k.space_key) 
        time.sleep(0.2)
        m.move(100,400)
        m.click(100,400)
        k.press_key('a')
        m.click(100,400)
        k.release_key('a')



def is_alive():
    print 1

def is_end_game():
    print 1

def end_game_control(m):
    m.click(125,700)
    m.click(125,730)

main()