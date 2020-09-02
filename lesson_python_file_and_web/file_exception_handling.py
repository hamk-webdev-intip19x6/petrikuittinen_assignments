import sys
try:
    with open('myfile.txt') as f:
        s = f.readline()
        i = int(s.strip())
        print(i)
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# open file mode = "r/w/a/rb/wb/ab/r+/rb+/w+/wb+/a+/ab+"
f = open("filepath", "mode")
# do your file processing d = f.read() f.write(d)
f.close() # closing file starts to flush the results
with open("testi.txt", "mode") as f:
    # process file
    # file is closed automatically outside with
