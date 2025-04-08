import uiautomator2 as u2
from uiautomator2.image import imread, compare_ssim

d = u2.connect()

# 重新截图方法，指定区域截图
# def screenshot(deceive, bounds=None ) -> Image.Image:
#     im = deceive.screenshot()
#     return im.crop(bounds)

# Id = 'com.hozonauto.account:id/iv_login_qr'
# ele = d(text='应用中心')
# ele = d(resourceId=Id)

# d(text='应用中心').click()
# info = ele.exists
# info = ele.info
# info = ele.bounds()
# info = ele.center()
# info = ele.click_gone(maxretry=5,interval=1)

# info = ele.screenshot().save('应用中心.jpg')
# info = ele.screenshot().save('二维码.jpg')
# info = d.screenshot("全屏.jpg")
# screenshot(d,d(text='手动激活').bounds()).save('手动激活.jpg')

# d(text='应用中心').click_exists()
# xpath1 = '//*[@resource-id="com.hozonauto.netahome:id/rv_all_app"]/android.widget.LinearLayout[5]/android.widget.FrameLayout[1]/android.widget.ImageView[1]'
# xpath2 = '//*[@resource-id="com.hozonauto.netahome:id/rv_all_app"]/android.widget.LinearLayout[6]/android.widget.FrameLayout[1]/android.widget.ImageView[1]'
# d.sleep(2)
# info = d.xpath(xpath1)
# # info = d(text='应用中心').long_click()
# ele = d(text='一键通风').center()
# ele1 = d(text='离车不下电').center()
# info = d.drag(sx=ele[0],sy=ele[1],ex=ele1[0],ey=ele1[1],duration=0.5)
# info = ele.exists
# id = 'com.hozon.settings:id/right_scrollview_pager'
# info = d(resourceId=id).swipe('up',steps=1)
# info = d.swipe(0.5,0.4,0.5,0.6)
# info = d.shell('ls -alt')
# info = d.reset_uiautomator()
# info = d.app_list()
# img1 = imread('common/二维码.jpg')
# img2 = imread('common/全屏.jpg')
# info = compare_ssim(img1,img2)
#
# print(info)

# d.press('home')
# d.screenshot('img1.png')

d.app_start("com.ss.android.article.news")












# ２.设备安装守护进程（成功后多一个ATX小黄车程序）
# 确保需要安装的手机已经连接上电脑，adb devices列出所有设备列表
# 执行命令：python -m uiautomator2 init

# 4.安装UI资源定位器
# 执行命令pip install -U weditor
# windows系统可以创建桌面快捷方式 python -m weditor --shortcut，双击生成的桌面图标启动即可
# 或者直接运行命令行启动python -m weditor，直接打开浏览器界面，输入手机IP地址　点击Dump Hierarchy同步界面 但特别不流畅，将就用用。


# 国内包
#  pip install --upgrade weditor==0.6.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
#  pip install libtscanapi -i https://pypi.tuna.tsinghua.edu.cn/simple
# adb shell /data/local/tmp/atx-agent server --stop
# adb shell /data/local/tmp/atx-agent server -d