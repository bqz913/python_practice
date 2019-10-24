# arg1 + arg2 + arg3 の値を返す関数def_testを作成
def def_test(arg1, arg2, arg3):
    x = arg1 + arg2 + arg3
    return(x)

if __name__ == "__main__": # 実行ファイルがdef_1.pyの場合下の文が実行される
    print(def_test(1,2,4)) # 1 + 2 + 4の結果がprintされる