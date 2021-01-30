from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import datetime,time
import secrets

done_status = False
author_logo_gap = 150

def draw_multiple_line_text(image, imgName, text, author, fontName, fontSize, font, text_color, res, num, textwrapWidth, initial_height):

    if not done_status:
        global author_logo_gap
        all_chars = set(list(text))
        my_chars_list = ['[', ']', '`', '~', '{', '}', '@', '#', '$', '%', '^', '&', '_', '|', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e',
                        'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ':', ';', ',', "'", '"', '(', '!', '?', ')', '+', '-', '*', '/', '=', ' ', '\n']
        for achar in all_chars:
            if achar not in my_chars_list:
                text = text.replace(achar, '')
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size
        line_width, line_height = font.getsize("UK")

        lines = textwrap.wrap(text, width=textwrapWidth)
        W, H = image.size
        # y_text = (H-line_height*(len(lines)+6))//2
        y_text = initial_height
        # print(lines, y_text, textwrapWidth)
        max_line_width = 0
        for line in lines:
            line_width, line_height = font.getsize(line)
            w, h = draw.textsize(line, font=font)
            draw.text(((W - w) / 2, y_text),
                    line, font=font, fill=text_color)
            y_text += line_height
            max_line_width = max(max_line_width,line_width)
            if y_text+line_height > 600:
                # print("This text won't lie in this page",fontSize, textwrapWidth, initial_height)
                # image.show()
                # time.sleep(5)
                if initial_height > 100:
                    if author_logo_gap >=130:
                        print("Pushing text downward")
                        print()
                        author_logo_gap-=1
                        print("Pushing text upward")
                        print()
                        write(text, author, imgName, text_color, fontName, fontSize, res, num, textwrapWidth, initial_height-10)
                    elif author_logo_gap > 150:
                        write(text, author, imgName, text_color, fontName, fontSize, res, num, textwrapWidth, initial_height-10)
                else:
                    print("Reducing font size")
                    print()
                    wrap_width = textwrapWidth
                    if W-max_line_width >= 200:
                        print("Increasing text warp width")
                        print()
                        wrap_width+=3
                    write(text, author, imgName, text_color, fontName, fontSize-1, res, num, wrap_width, initial_height)
                break
        
        # placing logo begin
        line = "EduNil.com"
        font = ImageFont.truetype("fonts/efont.otf", fontSize)
        line_width, line_height = font.getsize(line)
        w, h = draw.textsize(line, font=font)
        # print(H-160,"edunil")
        draw.text(((W - w) / 2, H-160),
                line, font=font, fill=text_color)
        # placing logo end

        # placing author begin
        font = ImageFont.truetype("fonts/author.otf", fontSize)
        line = author
        line_width, line_height = font.getsize(line)
        # print(y_text+line_height,"author")
        w, h = draw.textsize(line, font=font)
        draw.text(((W - w) / 2, y_text+line_height),
                line, font=font, fill=text_color)
        # placing author end

        
        if (H-160)-(y_text+line_height)>=author_logo_gap:
            print("saving image")
            print()
            save_img(num, image, res)
        else:
            # print("less gap",fontSize, textwrapWidth, initial_height)

            # image.show()
            # time.sleep(5)
            if initial_height >100:
                if author_logo_gap >=130:
                    print("Pushing text downward")
                    print()
                    author_logo_gap-=1
                    print("Pushing text upward")
                    print()
                    write(text, author, imgName, text_color, fontName, fontSize, res, num, textwrapWidth, initial_height-10)
                elif author_logo_gap > 150:
                    write(text, author, imgName, text_color, fontName, fontSize, res, num, textwrapWidth, initial_height-10)
            else:
                print("Reducing font size")
                print()
                wrap_width = textwrapWidth
                if W-max_line_width >= 200:
                    wrap_width+=3
                write(text, author, imgName, text_color, fontName, fontSize-1, res, num, wrap_width, initial_height)
    else:
        # print(done_status)
        pass


total_pages = 0


def save_img(num, image, res):
    global total_pages
    global done_status
    done_status = True
    total_pages = max(total_pages, num)
    # image.show()
    digest = ''.join(''.join(''.join(''.join(
        str(datetime.datetime.utcnow()).split()).split('.')).split('-')).split(':'))
    digest += str(secrets.token_hex(3))
    image.save("images/qoute"+str(digest)+".jpg", optimize=True, quality=res)


def write(txt, author, imgName, color, fontName, fontSize, res, num, textwrapWidth, initial_height):
    # image = Image.new('RGB', (600, 800), color = (197,189,186))
    image = Image.open(imgName)
    im_resized = image.resize((1422, 800), Image.ANTIALIAS)
    im_resized.save("background/compressed_bg/page0.png")
    image = Image.open("background/compressed_bg/page0.png")
    font = ImageFont.truetype(fontName, fontSize)

    text_color = color
    num = draw_multiple_line_text(
        image, imgName, txt, author, fontName, fontSize, font, text_color, res, num, textwrapWidth, initial_height)

    # draw_multiple_line_text(image, text2, font, text_color, 400)


def begin_writing_text(txt, author, imgName, color, fontName, fontSize, res):
    '''
    Testing draw_multiple_line_text
    '''
    global done_status
    done_status = False

    textwrapWidth, initial_height = 50,320

    write(txt, author, imgName, color, fontName, fontSize, res, 0, textwrapWidth, initial_height)
    # print(total_pages)
    # img1 = Image.open(imgName)
    # im_list = [Image.open('page{}.png'.format(i)) for i in range(1,total_pages+1)]
    # img1.save('./handwritten.pdf', "PDF", resolution=200.0, save_all=True, append_images=im_list)

    # for i in range(total_pages+1):
    #     os.remove('page{}.png'.format(i))
    # os.remove('./handwritten.pdf')
    # image_width

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
