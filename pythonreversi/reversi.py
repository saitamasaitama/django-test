from PIL import Image, ImageFilter
BLACK = 1
WHITE = -1
STONE = {1:'BLACK', -1:'WHITE'}
class Board:

    def __init__(self):
    
        self.cells = []
        for i in range(8):
            self.cells.append([None for i in range(8)])


        self.cells[3][3] = WHITE
        self.cells[3][4] = BLACK
        self.cells[4][3] = BLACK
        self.cells[4][4] = WHITE

    #盤面の状態を文字列として返す
     #board_rendering
    def board_rendering(self):
        board = ""
        for i in self.cells:
            for cell in i:
                if cell == WHITE:
                    board += "○" #print("○", end=" ")
                elif cell == BLACK:
                    board +="●"#print("●", end=" ")
                else:
                    board +="*"#print("*", end=" ")
            board +="\n"#print("\n", end="")
        return board

    def put_board_image(self,user_id):
        im1 = Image.open('../testapp/static/testapp/オセロ.png')
        black_stone = Image.open('../testapp/static/testapp/white.png')
        print(f"im1:{im1}")
        print(f"black_stone:{black_stone}")
        white_stone = Image.open('../testapp/static/testapp/black.png')

        back_im = im1.copy()

        x = 0
        y = 0
        for i in self.cells:
            for cell in i:
                if cell == WHITE:
                    cell_place1 = x * 128
                    cell_place2 = y * 128
                    print(cell_place1)
                    print(cell_place2)
                    back_im.paste(white_stone,(cell_place))
                elif cell == BLACK:
                    cell_place1 = x * 128
                    cell_place2 = y * 128
                    back_im.paste(black_stone,(cell_place))
                y += 1
            x += 1
        
        
        back_im = im1.copy()
        back_im.save(f'../testapp/static/testapp/{user_id}.png', quality=95)
        #pngの名前はuser_id

  

    def put(self, x, y, stone):
        flippable = self.list_flippable_disks(x, y, stone)
        self.cells[y][x] = stone
        for x,y in flippable:
            self.cells[y][x] = stone

        return True


    def show_board(self,turn):
        board = ""
        board += str(turn) + "ターン目"
        #print("--" * 20)
        #print(str(turn) + "ターン目")
        #print("  ", end="")   
        for i in range(8):
           # print(i, end="")
            board += str(i)
            #print(" ", end="")
       # print("\n", end="")
        board += "\n"

        j = 0
        for i in self.cells:
            board+= str(j)
            #print(j, end="")
            #print(" ", end="")
            j += 1
            for cell in i:
                if cell == WHITE:
                    board += "○" #print("○", end=" ")
                elif cell == BLACK:
                    board +="●"#print("●", end=" ")
                else:
                    board +="*"#print("*", end=" ")
            board +="\n"#print("\n", end="")
        
        return board


    
    def list_possible_cells(self, stone):#viewの中で呼ぶ
        possible = []
        for x in range(8):
            for y in range(8):
                if self.cells[y][x] is not None:
                    continue
                if self.list_flippable_disks(x, y, stone) == []:
                    continue
                else:
                    possible.append((x, y))
        return possible

    
    def list_flippable_disks(self, x, y, stone):
        PREV = -1
        NEXT = 1
        DIRECTION = [PREV, 0, NEXT]
        flippable = []

        for dx in DIRECTION:
            for dy in DIRECTION:
                if dx == 0 and dy == 0:
                    continue

                tmp = []
                depth = 0
                while(True):
                    depth += 1

                    
                    rx = x + (dx * depth)
                    ry = y + (dy * depth)

                    
                    if 0 <= rx < 8 and 0 <= ry < 8:

                        request = self.cells[ry][rx]

                        
                        if request is None:
                            break

                        if request == stone:  
                            if tmp != []:     
                                flippable.extend(tmp) 
                            else:             
                                break

                        
                        else:
                            tmp.append((rx, ry))  
                    else:
                        break
        return flippable
    


class Othello:
    board:Board = None
    
    def play(self):#一番最初の盤面を出す
        self.board = Board()
        

othello_instance = Othello()
reversi_instance = Board()
test = Board()
test.put_board_image("uuuuu")