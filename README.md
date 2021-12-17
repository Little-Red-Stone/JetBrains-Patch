本脚本根据[Jetbrains系列产品最新激活方式](https://www.xuzihao.com/posts/6aacb63a/)中的原理制作完成，~~之前说过，我的shell是废的~~，所以这个还是用Python写的
## 使用
### 下载
首先从[GitHub](https://github.com/ja-netfilter/ja-netfilter/releases)下载ja-netfilter，放到用户文件夹，如: `/Users/???/` 中

然后，从[123云盘](https://www.123pan.com/s/motA-zO6Rv)下载 `mymap.jar` 放入 `ja-netfilter` 文件夹中的 `plugins` 文件夹，比如
```
/Users/???/ja-netfilter/plugins/
```

然后将源码下载、解压到 `ja-netfilter` 文件夹，在终端运行
```
cd ja-netfilter && python3 main.py
```

### 解释
解释一下脚本的内容
#### 当出现以下两行时
```
What name do you want to use?
Name=
```
在 `name` 中输入你想在IDE中显示的许可证激活名称

#### 当出现以下四行时
```
What time limit do you want?
Year=
Month=
Day=
```
在 `Year` 、 `Month` 、 `Day` 中分别输入你想在IDE中显示的，许可证激活到期的年份、月份、日期

### 尽情享受吧！
