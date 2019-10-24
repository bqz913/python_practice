class class_test():
    def __init__(self, a, b):       # __init__という名前にするとコンストラクタになる。(コンストラクタ・・・クラスが生成された瞬間に呼び出されるdef文)
        self.val1 = a               # self.は変数をインスタンス変数にするために必要
        self.val2 = b
        self.val3 = 0

    def method1(self):
        print(self.val1 + self.val2 + self.val3)

    def method2(self):
        print(self.val1 - self.val2)

if __name__ == "__main__":
    class_test(3,5).method1()       # class_testのmethod1を実行
    class_test(5,6).method2()       # method2を実行

    ins = class_test(1,2)           # インスタンス作成(self.val1とself.val2が生成される)
    ins.method1()                   # method1を実行(14行目と同じことを行っている)

    ins2 = class_test(1, 2)         # インスタンス作成
    ins2.val3 = 10                  # val3の値を変更する
    ins2.method1()                  # val3の値が10になってることが確認される