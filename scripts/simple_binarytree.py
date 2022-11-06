###
# https://fuji-pocketbook.net/data-structure/ にあるサンプルコードにコメントをつけた自分の勉強の備忘録
###

#1つの葉を1つのオブジェクトとして実装
from collections import deque
from inspect import stack
from turtle import right


class Node:
    def __init__(self, data) -> None:
        self.data = data #Nodeに格納されているdata
        self.left = None #このオブジェクトの左下の葉のオブジェクト
        self.right = None #このオブジェクトの右下の葉のオブジェクト

#幅優先探索


#深さ優先探索
def dfsearch(root):
    stack = deque([root]) #dequeクラスを使って、データをスタックとして持つ
    data = []
    while stack:
        node = stack.pop() #stackの右から1つずつ要素抜き出す
        data.append(node.data)

        #左下にノードがある場合
        if node.left:
            stack.append(node.left)
        
        #右下にノードがある場合
        if node.right:
            stack.append(node.right)

    for idx, datam in enumerate(data):
        print(f"{idx}-th data = {datam}")


if __name__ == "__main__":
    root = Node(0) #root nodeをインスタンス化
    root.left = Node(1) #root nodeの一段下の左側の葉のNodeを、root nodeのself.leftに格納
    root.right = Node(2) #root nodeの一段下の右側の葉のNodeを、root nodeのself.rightに格納
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    dfsearch(root)