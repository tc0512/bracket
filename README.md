# bracket
python制作的转译型简单编程语言

## 1 安装
```bash
pip install bracket
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
    [IF] [i==100000]
        [BREAK]

# GUI
[USE] [TKGUI]
[VAR] [root] [TKGUI.Tk()]
root.title("Hello bracket")
root.geometry("300x200")
[VAR] [label] [TKGUI.Label(root, text="Hello, World!")]
label.pack()
root.mainloop()
```
