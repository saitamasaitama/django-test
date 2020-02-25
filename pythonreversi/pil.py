'''from PIL import Image, ImageFilter

im1 = Image.open('../testapp/static/testapp/オセロ.png')



def put_board_image():
    black_stone = Image.open('../testapp/static/testapp/white.png')
    white_stone = Image.open('../testapp/static/testapp/black.png')

    back_im = im1.copy()
    for i in self.cells:
        for cell in i:
            if cell == WHITE:
                cell_place = (cell-1) *128
                back_im.paste(white_stone,(cell_place))
            elif cell == BLACK:
                cell_place = (cell-1) *128
                back_im.paste(black_stone,(cell_place))
            else:
                board +="*"#print("*", end=" ")
        board +="\n"#print("\n", end="")
    return board
    
    
    back_im = im1.copy()
    
    
    image_number = str(x)+str(y)
    
    back_im.save(f'../testapp/static/testapp/{image_number}.png', quality=95)
    #pngの名前はuser_id
'''å
