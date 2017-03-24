def findColumns(queen, columns):
    while columns[queen] != 0:
        queen += 1
    columns[queen] += 1
    return columns

def solveLine(line):
    n = int(line)
    rows = [0] * n
    columns = [0] * n
    for queen in range(0,n): #places queens in each row
        rows[queen] += 1 #increments when a queen is placed in that row
        if columns[queen] == 0:
            columns = findColumns(queen, columns)
               
# for i in columns, for h in rows, draw X if h = 1, else draw _
    
def main():
    with open('nqueens.txt') as file:
        for line in file:
            solveLine(line)
