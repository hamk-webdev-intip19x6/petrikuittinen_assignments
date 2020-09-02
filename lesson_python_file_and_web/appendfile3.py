with open("test.txt", "r+") as f:
    d = f.read()
    f.seek(0, 0)  # seek to start of file
    f.write("new line to start\n")
    f.write(d)  # write old contents of file
