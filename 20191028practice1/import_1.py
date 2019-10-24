import def_1                                # def_1.pyを実行
print(def_1.def_test(1,2,4))                # def_1.pyのdef_test()を実行

from def_1 import *                         # このように記述するとファイル名.と書く必要がなくなる
print(def_test(1,2,3))                      # def_1.pyのdef_test()を実行

import def_2                                # if __name__ == "__main__" にしないとprint文が実行されちゃう
print(def_2.def_test(2,3,3))                # def_2.pyのdef_test()を実行

import class_1                              # class_1.pyを実行
cls = class_1.class_test(1,2)               # clsにclass_1.py内のclass_test()を入れる(インスタンスを作成する)
cls.method1()                               # class_1.class_test(1,2).method1()と記述してもOK
cls.method2()
print(cls.val1)                             # clsに入ってるインスタンス変数も参照できる
print(cls.val2)

cls_2 = class_1.class_test(3,2)             # もう一個cls_2というインスタンスを作ってみる
print(cls_2.val2)

import package1                             # package1内の__init__.pyを実行

import package1.module1                     # package1内のmodule.pyを実行
print(package1.module1.module1(1,2,3))      # package1の中のmodule1.pyのmodule()を実行

from package1 import module1                # package1内のmodule1.pyを実行
print(module1.module1(1,2,3))               # module1.py内のmodule1を実行

from package1 import module2                # package1内のmodule2.pyを実行
print(module2.module2(1,1,1).plus())        # module2.pyのmodule2クラスのplus()メゾットを実行
print(module2.module2(1,1,1).minus())       # module2.pyのmodule2クラスのminus()メゾットを実行