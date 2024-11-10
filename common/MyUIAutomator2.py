import uiautomator2 as u2

d = u2.connect('192.168.101.16')
info = d(text='平板管家').info
print(info)