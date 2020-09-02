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


