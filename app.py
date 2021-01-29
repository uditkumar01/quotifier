from hand import begin_writing_text
with open("text/quotes.txt", 'r') as qoute:
    lines = qoute.readlines()
    for line in lines:

        if line:
            args = {
                "text": line.split(" ~ ")[0],
                "author": line.split(" ~ ")[1],
                "image": "background/bg2.jpg",
                "color": "255 255 255",
                "font": "fonts/LeagueSpartan-Bold.otf",
                "fontSize":50,
                "res": 60
            }

            begin_writing_text(args.get("text"), args.get("author"), args.get("image"), tuple(
                map(int, args.get("color").split())), args.get("font"), args.get("fontSize"), args.get("res"))
