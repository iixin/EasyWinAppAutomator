# 基于 Appium 的 Windows 自动化工具框架

## 简介
这是一个基于Appium的Windows应用程序自动化基础框架，主要用于与Windows桌面应用进行交互。它允许用户通过提供应用程序名称来定位和控制运行中的应用程序，并执行自定义任务。

你可以在此基础上自定义你的任务，快速完成开发。

## 功能特性
1. 根据程序名称查找正在前台运行（图标显示在系统任务栏）的应用程序，根据应用程序名称找到对应的窗口句柄，方便使用。

2. 格式化获取所有元素的XPath，以便快速定位元素。

## 快速开始
1. 安装依赖
    ```bash
    # 安装Appium
    npm i -g appium
    # 安装 Windows 平台 Appium 驱动程序
    appium driver install windows
    # 安装 Appium Python 客户端
    pip install Appium-Python-Client
    ```
2. 编写你的自动化任务

    *Example*
   ```Python
    def my_task(driver : webdriver.webdriver.WebDriver):
        # TODO: add your task
        node_收藏 = driver.find_element(By.XPATH, "/*[1]/*[2]/*[1]/*[1]/*[4]")
        node_收藏.click()
    main("微信", my_task)
   ```
3. 打开你要执行自动化的程序（确保其图标显示在系统任务栏，以便能被本程序找到）
4. 运行本程序

## Xpath快速查看工具

你可以运行 get_all_xpath 任务以快速查看元素的Xpath

*Example*
```bash
 /*[1]/*[1]  窗格
 /*[1]/*[2]  窗格
  /*[1]/*[2]/*[1]  窗格
   /*[1]/*[2]/*[1]/*[1] 导航 工具栏
    /*[1]/*[2]/*[1]/*[1]/*[1] 昵称 按钮
    /*[1]/*[2]/*[1]/*[1]/*[2] 1条新消息 按钮
    /*[1]/*[2]/*[1]/*[1]/*[3] 通讯录 按钮
    /*[1]/*[2]/*[1]/*[1]/*[4] 收藏 按钮
    /*[1]/*[2]/*[1]/*[1]/*[5] 聊天文件 按钮
    /*[1]/*[2]/*[1]/*[1]/*[6] 朋友圈 按钮
    /*[1]/*[2]/*[1]/*[1]/*[7]  窗格
     /*[1]/*[2]/*[1]/*[1]/*[7]/*[1]  窗格
      /*[1]/*[2]/*[1]/*[1]/*[7]/*[1]/*[1]  窗格
       /*[1]/*[2]/*[1]/*[1]/*[7]/*[1]/*[1]/*[1] 视频号 按钮
      /*[1]/*[2]/*[1]/*[1]/*[7]/*[1]/*[2]  窗格
       /*[1]/*[2]/*[1]/*[1]/*[7]/*[1]/*[2]/*[1] 看一看 按钮
       ...
```


