import numpy
from flask import Flask, render_template, request, send_file, jsonify
from flask_qrcode import QRcode

app = Flask(__name__)
qrcode = QRcode(app)

# if __name__ == '__main__':
app.run()


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


@app.route("/solve", methods=["GET"])
def solve():
    data = request.args.get("val", "")
    a = numpy.array([[int(j) for j in i.split(' ')] for i in data.splitlines()]) # list(map(int, data.split(' ')))#[[int(j) for j in data.split()] for i in range(n1)]
    solveSudoku(a)
    print(a)
    return jsonify(a.tolist())


def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False
