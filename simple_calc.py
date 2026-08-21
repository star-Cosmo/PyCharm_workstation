"""
简单计算器
支持基本的数学运算

使用方法：
1. 运行脚本
2. 输入数学表达式（如: 2 + 3）
3. 支持的运算符: + - * /
4. 输入 'quit' 退出
"""


def calculator(expression):
    """计算数学表达式"""
    try:
        # 安全检查：只允许数字和基本运算符
        allowed_chars = set("0123456789+-*/(). ")
        if not all(c in allowed_chars for c in expression):
            return "错误：表达式包含不允许的字符"
        
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "错误：除数不能为零"
    except Exception as e:
        return f"计算错误: {e}"


def main():
    print("=" * 50)
    print("简单计算器")
    print("=" * 50)
    print("支持的运算符: + - * /")
    print("输入 'quit' 退出")
    print("=" * 50)
    
    while True:
        try:
            expression = input("\n请输入表达式: ").strip()
            
            if expression.lower() in ('quit', 'exit', 'q'):
                print("再见！")
                break
            
            if not expression:
                continue
            
            result = calculator(expression)
            print(f"结果: {result}")
            
        except KeyboardInterrupt:
            print("\n再见！")
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
