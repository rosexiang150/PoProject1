from appium import webdriver
import time


class TestSetting:
    # 全局变量，当前类里面的所有的方法都可以使用
    value = True

    def setup(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 解决输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    def test_more(self):
        list_1 = self.driver.find_elements_by_id('com.android.settings:id/title')
        print(id(list_1))
        list_1[1].click()

        list_2 = self.driver.find_elements_by_id('android:id/title')
        print(id(list_2))
        # eles[2].click()
        for i in list_2:
            s = i.__getattribute__("text")
            if s == '移动网络':
                i.click()

        list_3 = self.driver.find_elements_by_id('android:id/title')
        print(id(list_3))
        list_3[1].click()

        list_4 = self.driver.find_elements_by_id('android:id/text1')
        # 局部变量，只有在当前方法里面才可以使用，方法结束，局部变量消失
        target = True
        for i in list_4:
            s = i.__getattribute__('text')

            if s == '3G':
                target = False
            print(s)

        assert target == True
