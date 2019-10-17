## 项目简介

1，麻花宠物APP是一个专为养宠爱好者开发的宠物交流平台，集线上优质宠物用品引导铲屎官科学养宠，快乐养宠！功能包含记录提醒提醒功能、宠物搞笑视频查看评论分享
功能、宠物表情包下载分享功能、宠物商城等，当前更新至1.3.1版本。APP正在持续不断的更新中，但有些功能后续开发不会变动或者变动较小，如：启动APP、注册、登录、日常打卡、提醒吧、健康管理、意见反馈、日历记录等功能，所以将这一部分功能考虑写成自动化脚本用于后续版本更新的回归性测试。

2，这是一个针对麻花宠物APPv1.3.1 Android版本的的UI自动化项目，基于python3.6+appium（v1.7.2）。由于该app功能的特殊性以及当前调试环境未配置好uiautomator2而无法定位toast元素，导致目前还未找到合适有效的方法对用例进行断言；已经写入自动化项目的部分功能以后可能会有更改，以及后续更新的功能的加入，使得代码维护周期将随APP版本的更新而变长；未找到已编写完成的app UI自动化项目进行参照，毫无经验的测试小哥哥只能按照自己的理解编写用例及代码，测试用例的编写以及代码的编写可能有很多需要优化改进的地方；基于以上3点原因，项目的维护周期应该是直至项目结束，假使测试小哥哥不会从公司离职。

## 环境配置

1，python3.6，解释器环境

2，appium v1.7.2，UI自动化测试框架

3，selenium，自动化测试工具

4，logging，日志模块

5，os模块，获取路径、调用shell脚本

6，HTMLTestRunner，生成html格式报告模板

7，time，时间戳，生成的报告名称是：time_report.html

8，测试机：小米note顶配版，Android 5.1.1

## 实现功能

1，对麻花宠物APPv1.3.1Android版本的：启动APP、未登录、注册、登录（验证码、账号密码、微信）、日常打卡（新增、打卡、删除）、提醒吧（新增、打卡、删除）、健康管理（新增、修改、删除）、宠物（切换、新增、删除）、日历记录、打卡积分、意见反馈等功能的自动化

2，自动生成测试报告功能

## 目录结构说明

1，APP 存放app文件

2，Base 放基础方法模块。BaseAdb.py模块获取设备名、设备UDID、设备系统版本号；BaseApk.py模块获取APP中app的路径、appPackage、启动类appActivity；BaseUpdateYmal.py模块将获取的app信息写入Config 中的yaml文件；BaseInstallApp.py模块判断设备是否安装需要测试的app，否则安装应用；BaseAppiumServer.py模块启动appium服务；BaseDriver.py模块启动app方法；BaseLog.py为日志模块；BaseOperate.py模块滑动操作；BaseMethod.py模块判断页面是否存在某元素；BaseTools.py模块获取当前类名、当前函数名等；BaseView.py模块为元素基类BaseScreenShot.py模块截图；BaseReport.py模块生成报告

3，Config 中的desired_caps.yaml文件中存放启动app信息

4，Log 中存放日志

5，Report 中存放测试报告

6，Screenshot 中存放截图

7，Testcase 中存放用例操作步骤代码模块

8，用例.xlsx 中为编写的测试用例
