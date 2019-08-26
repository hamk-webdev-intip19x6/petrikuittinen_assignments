with open("testi.txt", "w", encoding="utf-8") as f:
    while True:
        line = input("Give me a line?")
        if not line: break
        print(line, file=f, flush=True)
        # alternative you can use f.flush()
    
    
    

