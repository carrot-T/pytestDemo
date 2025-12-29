import uiautomator2 as u2

from common.logger import logger

d = u2.connect()
pkg = "com.cherry.pdc.recordvoice"
lan_select = "com.cherry.pdc.recordvoice:id/spinner_text"
lan = ["Chinese","English","Russian","Spanish","Arabic","Persian","Brazilian Portuguese","European Portuguese","Thai","Indonesian","German","French","Italian","Turkish","Hebrew","Dutch","Swedish","Polish","Kazakh","Malay","Norwegian Bokmål","Danish"]
button_record = "com.cherry.pdc.recordvoice:id/button_record"
button_next = "com.cherry.pdc.recordvoice:id/button_next"
button_cancel_upload = "com.cherry.pdc.recordvoice:id/button_cancel_upload"
up = (600, 2500, 600, 300)
down = (600, 300, 600, 2500)


def rc():
    d.app_stop(pkg)
    d.sleep(1)
    d.app_start(pkg)
    d.sleep(1)

    for l in lan:
        if l == d(resourceId=lan_select).info['text']:
            if d(text="确认").exists:
                d(text="确认").click()
        else:
            d(resourceId=lan_select).click()
            if d(text=l).exists:
                d(text=l).click()
            else:
                d.swipe(*down)
                if d(text=l).exists:
                    d(text=l).click()
                else:
                    d.swipe(*up)
                    d(text=l).click()
            if d(text="确认").exists:
                d(text="确认").click()

        d.sleep(1)
        for i in range(1000):
            d(resourceId=button_record).click()
            d.sleep(2)
            d(resourceId=button_record).click()
            d(resourceId=button_next).click()
            d.sleep(1)
            toast = d.toast.get_message()
            if toast == "上传失败":
                logger.info("语言：" + l + "，第 " + str(i+1) + " 条语料 - " + toast)
                d(resourceId=button_cancel_upload).click()
            logger.info("语言：" + l + "，第 " + str(i+1) + " 条语料 - " + toast)
            d.sleep(1)


def rc1(l="Chinese"):
    d.app_stop(pkg)
    d.sleep(1)
    d.app_start(pkg)
    d.sleep(1)

    if l == d(resourceId=lan_select).info['text']:
        if d(text="确认").exists:
            d(text="确认").click()
    else:
        d(resourceId=lan_select).click()
        if d(text=l).exists:
            d(text=l).click()
        else:
            d.swipe(*down)
            if d(text=l).exists:
                d(text=l).click()
            else:
                d.swipe(*up)
                d(text=l).click()
        if d(text="确认").exists:
            d(text="确认").click()

    d.sleep(1)
    for i in range(1000):
        d(resourceId=button_record).click()
        d.sleep(2)
        d(resourceId=button_record).click()
        d(resourceId=button_next).click()
        d.sleep(1)
        toast = d.toast.get_message()
        if toast == "上传失败":
            logger.info("语言：" + l + "，第 " + str(i + 1) + " 条语料 - " + toast)
            d(resourceId=button_cancel_upload).click()
        logger.info("语言：" + l + "，第 " + str(i + 1) + " 条语料 - " + toast)
        d.sleep(1)

if __name__ == '__main__':
    # rc()
    rc1("English")
    # d(resourceId=luzhi).click()
    # d.sleep(2)
    # d(resourceId=luzhi).click()
    # d(resourceId=xiayige).click()
    # d.sleep(1)
    # info = d.app_current()  # 获取当前包名
    # print(str(info))
    # d.shell('pm grant com.cherry.pdc.recordvoice android.permission.INJECT_EVENTS')


