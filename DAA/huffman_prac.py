import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq=freq
        self.symbol=symbol
        self.left=left
        self.right=right
        self.huff=""

    def __lt__(self,nxt):
        return self.freq<nxt.freq

def printNodes(node, val=""):
    newVal=val+str(node.huff)
    if(node.left):
        printNodes(node.left,newVal)
    if(node.right):
        printNodes(node.right, newVal)

    if not node.left and not node.right:
        print(node.symbol," ", newVal)

chars=['a', 'b', 'c', 'd', 'e', 'f']
freq=[5,9,12,13,16,45]

pq=[]
for x in range(len(chars)):
    heapq.heappush(pq, Node(freq[x], chars[x]))

while(len(pq)>1):
    left=heapq.heappop(pq)
    right=heapq.heappop(pq)
    left.huff=0
    right.huff=1
    newNode=Node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    heapq.heappush(pq, newNode)

printNodes(pq[0])