import gc
import os
import time
import win32api, win32con, win32gui
import sys
import win32com.client

terms = 0
class DesktopWindow(object):
    def __init__(self, *args, **kwargs):
        self.window_id = win32gui.GetDesktopWindow()
        self.window_dc = win32gui.GetWindowDC(self.window_id)
        pass
    def get_pixel_color(self, i_x, i_y):
        long_colour = win32gui.GetPixel(self.window_dc, i_x, i_y)
        i_colour = int(long_colour)
        return (i_colour & 0xff, (i_colour >> 8) & 0xff,
                (i_colour >> 16) & 0xff)
    def set_pixel_color(self, i_x, i_y, i_color):
        x,y = win32gui.ScreenToClient(self.window_id,(i_x,i_y))
        win32gui.SetPixel(self.window_dc, x, y, i_color)
    def release(self):
        win32gui.releaseDC(self.window_id,self.window_dc)    
x_ini = 244
x_fim = 646
y_ini = 570
y_fim = 592
x_tam = x_fim - x_ini
y_tam = y_fim - y_ini
n_parts = 8
now = time.time()
is_on = True
while time.time() - now <= 60.0:
    if(is_on):
        try:
            dtop = DesktopWindow()
            for i in range(1,41):
                for j in range(y_ini,y_fim+1):
                    color = 0x00ff00
                    if(i % 5 == 0):
                        color = 0xffffff
                    dtop.set_pixel_color(x_ini + (x_tam/40)*i,j,color)
            for i in range(1,n_parts+1):
                for j in range(0,10):
                    color = 0x00ffff
                    dtop.set_pixel_color((800/n_parts) * i, j, color)
            dtop.release()
        except:
            pass
        time.sleep(0.005)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    