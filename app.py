from hand import begin_writing_text
import random
with open("text/quotes.txt", 'r') as qoute:
    lines = qoute.readlines()
    for line in lines:
        bg_img = ""
        with open("text/random_bg.txt") as bg_file:
            i_names = bg_file.readlines()
            img_names = []
            for name in i_names:
                if name.strip():
                    img_names.append(name)
            i_names.clear()
            # print(img_names)
            bg_img = img_names[random.randint(0,len(img_names)-1)].strip()
        print(bg_img,"bg")
        if line.strip():
            args = {
                "text": line.split(" ~ ")[0],
                "author": line.split(" ~ ")[1],
                "image": "background/"+bg_img.split(" ~ ")[0],
                "color": bg_img.split(" ~ ")[1],
                "font": "fonts/LeagueSpartan-Bold.otf",
                "fontSize":50,
                "res": 60
            }

            begin_writing_text(args.get("text"), args.get("author"), args.get("image"), tuple(
                map(int, args.get("color").split())), args.get("font"), args.get("fontSize"), args.get("res"))
