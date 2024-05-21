from DrissionPage import ChromiumOptions, ChromiumPage

co = ChromiumOptions().use_system_user_path()
print("page1要控制的浏览器地址", co.address)
print("page1浏览器默认可执行文件的路径", co.browser_path)
print("page1用户数据文件夹路径", co.user_data_path)
print("page1用户配置文件夹名称", co.user, "\n")
page = ChromiumPage(co)

page.get('http://g1879.gitee.io/DrissionPageDocs', retry=3, interval=2, timeout=15)
print(f">>>>>>>>>>>>>>>>>>>>>>>>\n当前对象控制的页面地址和端口: {page.address}\n浏览器进程id: {page.process_id}\n标签页id: {page.tab_id}")
print(">>>>>>>>>>>>>>>>>>>>>>>>\n当前概述html", page.ele('x://*[@id="️-概述"]').html)
print(">>>>>>>>>>>>>>>>>>>>>>>>\n当前版本信息text", page.ele('x://p[contains(text(),"最新版本")]').text)
print(">>>>>>>>>>>>>>>>>>>>>>>>\ngit链接属性值", page.ele('x://p[contains(text(),"项目地址")]/a').attr('href'))

# page.quit()  退出浏览器