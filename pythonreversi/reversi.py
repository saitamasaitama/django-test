from PIL import Image, ImageFilter
from django_test.settings import BASE_DIR

BLACK = 1
WHITE = -1
STONE = {1:'BLACK', -1:'WHITE'}
class Board:
    """オセロクラスはオセロの盤面を表示"""
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
        """
        現在の盤面を文字列で返す

        Return:
            str:
                現在の盤面の文字列
        """
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
        """
        現在の盤面ををpillowで作る

        Args:
            user_id str:
                line送信者のuserid
        """
        try:
            #im1 = Image.open('../testapp/static/testapp/board.png')#パスわからないここでエラー
            im1 = Image.open(BASE_DIR + "/testapp/static/testapp/board.png")
            #black_stone = Image.open('../testapp/static/testapp/white.png')
            black_stone = Image.open(BASE_DIR + "/testapp/static/testapp/black.png")
            black_stone_r = black_stone.resize((75,75))
            print(f"im1:{im1}")
            print(f"black_stone:{black_stone}")
            #white_stone = Image.open('../testapp/static/testapp/black.png')
            white_stone = Image.open(BASE_DIR + "/testapp/static/testapp/white.png")
            print(white_stone)
            white_stone_r = white_stone.resize((75,75))
            back_im = im1.copy()
            print(back_im)

            x = 0
            for i in self.cells:
                y = 0
                print(f"i:{i}")
                for cell in i:
                    print(f"x,y:{x,y}")
                    if cell == WHITE:
                        cell_place1 = x * 105
                        cell_place2 = y * 105
                        print(cell_place1)
                        print(cell_place2)

                        back_im.paste(white_stone_r,(cell_place1,cell_place2))
                    elif cell == BLACK:
                        cell_place1 = x * 105
                        cell_place2 = y * 105
                        back_im.paste(black_stone_r,(cell_place1,cell_place2))  
                    y += 1
                x += 1
            
            print(back_im.save(BASE_DIR + f'/testapp/static/testapp/{user_id}.png', 'png'))
            back_im.save(BASE_DIR + f'/testapp/static/testapp/{user_id}.png', 'png')
        except Exception as e:
            print(e)
        #pngの名前はuser_id

  

    def put(self, x, y, stone):
        """
        石をひっくり返す

        Args:
            x int:
                ユーザから選ばれたオセロのx座標
            y int:
                ユーザから選ばれたオセロのy座標
            stone int:
                -1なら白、１なら黒
        
        Return:
            True bool:
        """
        flippable = self.list_flippable_disks(x, y, stone)
        self.cells[y][x] = stone
        for x,y in flippable:
            self.cells[y][x] = stone

        return True

    def count_stone(self):
        """
        盤面の白と黒の枚数を返す

        Return:
            tuple:
                white_countが白石の枚数でblack_countが黒石の枚数

        """
        white_count = 0
        black_count = 0
        for i in self.cells:
            for cell in i:
                if cell == WHITE:
                    white_count +=1
                elif cell == BLACK:
                    black_count += 1
        white_count = str(white_count)
        black_count = str(black_count)
        return white_count,black_count
        
    
    def list_possible_cells(self, stone):#
        """
        置ける場所を返す

        Args:
            stone int:
                -1なら白、１なら黒
        
        Return:
            list:
                置ける場所x,yのタプルをリストで返す
        """
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
        """
        ひっくり返せる石を探す

        Args:
            x int:
                ユーザから選ばれたオセロのx座標
            y int:
                ユーザから選ばれたオセロのy座標
            stone int:
                -1なら白、１なら黒
        
        Return;
            list:
                ひっくり返せるx,y座標のタプルをリストで返す
        """
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



