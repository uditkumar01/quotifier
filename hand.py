from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import datetime
import secrets



def draw_multiple_line_text(image, imgName, text, author, fontName, font, text_color, text_start_height, res,num):

    all_chars = set(list(text))
    my_chars_list = ['[',']','`','~','{','}','@','#','$','%','^','&','_','|','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ':', ';', ',', "'", '"', '(', '!', '?', ')', '+', '-', '*', '/', '=', ' ', '\n']
    for achar in all_chars:
        if achar not in my_chars_list:
            text = text.replace(achar,'')
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    line_width, line_height = font.getsize("UK")
    
    lines = textwrap.wrap(text, width=50)
    W,H = image.size
    y_text = (H-line_height*(len(lines)+6))//2
    print(lines,y_text)
    
    
    
    for line in lines:
        line_width, line_height = font.getsize(line)
        w, h = draw.textsize(line, font=font)
        draw.text(((W - w) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height
        if y_text+line_height > 600:
            save_img(num,image, res)
            num += 1

            # image.save('img/pil_text'+str(num)+'.png')
            write(' '.join(lines[lines.index(line)+1:]) , author, imgName, text_color, fontName, res,num)
            # write(' '.join(lines[lines.index(line):]),num+1)
            break
    
    # placing author begin
    font = ImageFont.truetype("fonts/author.otf", 50)
    line = author
    line_width, line_height = font.getsize(line)
    w, h = draw.textsize(line, font=font)
    draw.text(((W - w) / 2, y_text+line_height),
                  line, font=font, fill=text_color)
    # placing author end
            
    # placing logo begin
    line = "EduNil.com"
    font = ImageFont.truetype("fonts/efont.otf", 50)
    line_width, line_height = font.getsize(line)
    w, h = draw.textsize(line, font=font)
    draw.text(((W - w) / 2, H-160), 
                  line, font=font, fill=text_color)
    # placing logo end
    save_img(num,image, res)

total_pages = 0
def save_img(num,image, res):
    global total_pages
    total_pages = max(total_pages,num)
    # image.show()
    digest = ''.join(str(datetime.datetime.utcnow()).split())
    digest += str(secrets.token_hex(3))
    image.save("images/qoute"+str(digest)+".jpg", optimize = True,quality = res)

def write(txt, author, imgName, color, fontName, res, num):
    # image = Image.new('RGB', (600, 800), color = (197,189,186))
    image = Image.open(imgName)
    im_resized = image.resize((1422,800), Image.ANTIALIAS)
    im_resized.save("background/compressed_bg/page0.png")
    image = Image.open("background/compressed_bg/page0.png")
    fontsize = 50  # starting font size
    font = ImageFont.truetype(fontName, fontsize)

    text_color = color
    text_start_height = 0
    num = draw_multiple_line_text(image, imgName, txt, author, fontName, font, text_color, text_start_height, res, num)

    
    # draw_multiple_line_text(image, text2, font, text_color, 400)
    

def begin_writing_text(txt, author, imgName, color, fontName, res):
    '''
    Testing draw_multiple_line_text
    '''
    
    write(txt, author, imgName, color, fontName , res, 0)
    # print(total_pages)
    # img1 = Image.open(imgName)
    # im_list = [Image.open('page{}.png'.format(i)) for i in range(1,total_pages+1)]
    # img1.save('./handwritten.pdf', "PDF", resolution=200.0, save_all=True, append_images=im_list)

    # for i in range(total_pages+1):
    #     os.remove('page{}.png'.format(i))
    # os.remove('./handwritten.pdf')
    #image_width

# def begin_writing():
#     '''
#     Testing draw_multiple_line_text
#     '''
#     with open('text/assignment1.txt','rb') as f:
#         txt = f.read().decode('latin-1')
#     write(txt,0)
#     print(total_pages)
#     img1 = Image.open('page0.png')
#     im_list = [Image.open('page{}.png'.format(i)) for i in range(1,total_pages+1)]
#     img1.save('./handwritten.pdf', "PDF", resolution=200.0, save_all=True, append_images=im_list)

#     for i in range(total_pages+1):
#         os.remove('page{}.png'.format(i))
#     # os.remove('./handwritten.pdf')
#     #image_width

    
