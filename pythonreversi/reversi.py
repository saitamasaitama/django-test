import copy
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


    
    def list_possible_cells(self, stone):
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
    message=""
    def mode_option(self,mode):
        self.player1 = User(BLACK, "あなた")
        self.player2 = Program(WHITE, "Mini-method")
        message= "あなたは黒です"
    
        return message
        
    
    def play(self):
        board = Board()
        turn = 1
        pass_turn = 0

        while(True):
            board.show_board(turn)
            black_count = 0
            white_count = 0
            for x in range(8):
                for y in range(8):
                    if board.cells[y][x] == BLACK:
                        black_count+=1
                    elif board.cells[y][x] == WHITE:
                        white_count+=1

            if (black_count + white_count == 64
                or pass_turn == 2
                or black_count == 0
                or white_count == 0):
                print("--" * 10+ "finished!!" + "--" * 10)
                if black_count > white_count:
                    print("WINNER BLACK!!")
                if white_count > black_count:
                    print("WINNER WHITE!!")
                else:
                    print("Draw")

                print("results: " + "B:" + str(black_count) + ", W: " + str(white_count))

                break

            elif turn % 2 == 1:
                stone = BLACK
                possible = board.list_possible_cells(stone)
                if possible == []:
                    pass
                else:
                    divide = self.player1.main(possible)
                    index = [0]
                    return_board = divide[1]
                    return  return_board

            
            elif turn % 2 == 0:
                stone = WHITE
                possible = board.list_possible_cells(stone)
                if possible == []:
                    pass
                else:
                    divide = self.player2.main(possible)
                    index = [0]
                    return  return_board

            if possible == []:
                print("pass")
                pass_turn +=1
                pass

            else:
                board.put(*possible[index],stone)
                self.player1.copy_board(possible,index,stone)
                self.player2.copy_board(possible,index,stone)
                pass_turn = 0
            
            turn +=1
    

class BasePlayer:
    def __init__(self,stone,name):
        self.stone = stone
        self.name = name
        self.board = Board()
        self.copy_cells =[]


    def copy_board(self,possible,index,stone):
        self.board.put(*possible[index],stone)
        self.copy_cells = copy.deepcopy(self.board.cells)
    
    def reset_board(self):
        self.board.cells = copy.deepcopy(self.copy_cells)



class User(BasePlayer):

    def main(self, possible):
        
        '''print("player: "+ self.name + "(" + STONE[self.stone] + ")")
        print("puto to: ",end ="")'''
        board_return = ("あなた"+ self.name + "(" + STONE[self.stone] + ")"+"puto to: ")
        for i in range(len(possible)-1):
            print(str(i) + ":" + str(possible[i]), end=", ")
        print(str(len(possible) -  1) + ":" + str(possible[len(possible)-1]))
        confirm_list = []
        index = 0
        while(True):
            index = int(input("choose:"))

            for i in range (len(possible)):
                confirm_list.append(i)
            if index not in confirm_list:
                print("そこには置けません")
            else:
                break


        print("You put:" + str(possible[index]))
        return index ,board_return
    
class Program(BasePlayer):

    def main(self,possible):
        '''print("player: "+ self.name + "(" + STONE[self.stone] + ")")
        print("puto to: ",end ="")'''
        for i in range(len(possible)-1):
            print(str(i) + ":" + str(possible[i]), end=", ")
        print(str(len(possible) -  1) + ":" + str(possible[len(possible)-1]))
        index = 0
        


        print("You put:" + str(possible[index]))
        return index 

if instance == None:
    instance=Othello()