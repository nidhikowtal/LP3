class NQueens:
    def __init__(self):
        self.size=int(input("Enter size: "))
        self.board = [[False]*self.size for i in range(self.size)]
        self.count=0

    def printBoard(self):
        for row in self.board:
            for ele in row:
                if(ele==True):
                    print('Q', end=" ")
                else:
                    print('X', end=" ")
            print()
        print()

    def isSafe(self,row,col):

        for i in self.board:
            if(i[col]==True):
                return False

        i=row
        j=col

        while(i<self.size and j<self.size):
            if(self.board[i][j]==True):
                return False
            i=i+1
            j=j+1
        i=row
        j=col
        while(i>=0 and j>=0):
            if (self.board[i][j] == True):
                return False
            i = i - 1
            j = j - 1

        i=row
        j=col
        while(i<self.size and j>=0):
            if (self.board[i][j] == True):
                return False
            i = i + 1
            j = j - 1

        i=row
        j=col
        while(i>=0 and j<self.size):
            if (self.board[i][j] == True):
                return False
            i = i - 1
            j = j + 1

        return True


    def set_first_queen(self):
        row=int(input("Enter row: "))
        col=int(input("Enter col: "))

        self.board[row-1][col-1]=True
        self.printBoard()

    def solve(self, row):
        if(row==self.size):
            self.count=self.count+1
            self.printBoard()
            return

        if any(self.board[row]) is True:
            self.solve(row+1)
            return

        for col in range(self.size):
            if(self.isSafe(row,col)==True):
                self.board[row][col]=True
                self.solve(row+1)

                self.board[row][col]=False



    def printMsg(self):
        if(self.count>0):
            print("Soln")
        else:
            print("No soln")


obj=NQueens()
obj.set_first_queen()
obj.solve(0)
obj.printMsg()