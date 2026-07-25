# bracket
python制作的转译型简单编程语言

## 1 安装
```bash
pip install bracket-lang
```

## 2 Hello world
```bracket
[INFO] ["Hello world!"]
```

## 3 基本语法
```bracket
# 打印
[INFO] ["这是一段文本"]
[INFO] ["Loading...", end=" "]
[INFO] ["complete"]

# 变量
[VAR] [integer] [2]
[VAR] [floating_point] [3.0]
[VAR] [string] ["abc"]
[VAR] [lst] [[1, 2, 3, 4, 5]]
[VAR] [t] [(1, 2, 3)]
[VAR] [dict] [{1: 1, 2: 4, 3: 9}]
[INFO] [integer, floating_point, string, lst, t, dict]

# 输入
[VAR] [short] [INPUT] [单行文本] [False]
[VAR] [long] [INPUT] [多行文本] [True]
[INFO] ["您这两次分别输入了: "]
[INFO] [short]
[INFO] [long]

# 分支语句
[VAR] [a] [6]
[IF] [a>0]
    [INFO] ["正数"]
[ELSEIF] [a==0]
    [INFO] ["零"]
[ELSE]
    [INFO] ["负数"]

# 循环
[VAR] [total] [0]
[FOR] [i] [1, 101, 1]
    [VAR] [total] [total+i]
[INFO] ["1~100的和:", total]
[VAR] [i] [0]
[WHILE] [i<10]
    [INFO] [i]
    [VAR] [i] [i+1]
[LOOP]
    [INFO] [i]
    [IF] [i==100]
        [BREAK]
    [VAR] [i] [i+1]

# GUI
[USE] [TKGUI]
[VAR] [root] [TKGUI.Tk()]
root.title("Hello bracket")
root.geometry("300x200")
[VAR] [label] [TKGUI.Label(root, text="Hello, World!")]
label.pack()
root.mainloop()
```
输出: 
```text
这是一段文本
Loading... complete
2 3.0 abc [1, 2, 3, 4, 5] (1, 2, 3) {1: 1, 2: 4, 3: 9}
单行文本: 1
多行文本: 2
3
您这两次分别输入了
1
2
3
正数
5050
1
2
3
...
100
```
![窗口显示: ](./TKGUI_helloHello.jpg)

## 4 命令行工具参数
| 参数 | 用法 |
| ------ | ------ |
| `--help` `-h` | 帮助 |
| `build` | 转译 |
| `run` | 转译运行 |

## 6 注意事项
1. `INFO`的参数与python的`print`基本相同
2. `[VAR] [lst] [[1, 2, 3, 4, 5]]`是真正的列表, `[VAR] [t] [1, 2, 3, 4, 5]`是元组
3. `FOR`必须要写三个参数
4. `[LOOP]`是无限循环, 与`[WHILE] [True]`等效
5. 变量名不能与bracket关键字和python关键字重名
6. bracket语言不兼容python的列表推导式, 三元表达式等
7. bracket内置轻量编辑器bkted
