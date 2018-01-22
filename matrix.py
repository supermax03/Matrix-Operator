#################################################
#Author: Maximiliano Bordon
################################################

class Matrix:
    import operator
    _operations={'add':operator.add,'minus':operator.sub}
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
    def revert(self):
        import sys
        result = []
        try:
            for i_index in range(self.cols):
                row = []
                for j_index in range(self.rows):
                    row.append(self.getdata()[j_index][i_index])
                result.append(row)
        except:
            print(sys.exc_info())
        finally:
            return result

    def getOrder(self):
        return (self.rows, self.cols)

    def getdata(self):
        return self.matrix

    def hassameorder(self, othermatrix=None):
        if not othermatrix or not isinstance(othermatrix, Matrix):
            return False
        else:
            o1 = self.getOrder()
            o2 = othermatrix.getOrder()
            return (o1 == o2)

    def isidentitymatrix(self):
        if not self.issquarematrix():
            return False
        else:
            identity = True
            for id in range(self.rows):
                if (self.getdata()[id][id] != 1):
                    identity = False
                    break
            return identity

    def iszeromatrix(self):
        iszero = True
        for row_index in range(self.rows):
            for col_index in range(self.cols):
                if self.getdata()[row_index][col_index] != 0:
                    iszero = False
                    break
        return iszero

    def issquarematrix(self):
        rows, cols = self.getOrder()
        return (rows == cols)
    def applyfunction(self,othermatrix,operation):
        result=[[]]
        if self.hassameorder(othermatrix):
            _function=Matrix._operations[operation]
            if (_function):
                result=[]
                m1 = self.getdata()
                m2 = othermatrix.getdata()
                for row_index in range(self.rows):
                    row = []
                    for col_index in range(self.cols):
                        partial = _function(m1[row_index][col_index],m2[row_index][col_index])
                        row.append(partial)
                    result.append(row)
        return Matrix(result)
    def add(self, othermatrix):
                  return self.applyfunction(othermatrix,'add')
    def minus(self,othermatrix):
                  return self.applyfunction(othermatrix,'minus')

if __name__=='__main__':
     m=Matrix([[1,2,3],[4,5,6]])
     m1=Matrix([[1,3,2],[6,7,8]]

          )
     print(m1.revert())
     print((m.add(m1)).getdata())
     print((m.minus(m1)).getdata())

