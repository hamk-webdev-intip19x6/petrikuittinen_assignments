import glob

text_files = glob.glob("*.txt")
for text_file in text_files:
    with open(text_file) as f:
        lines = f.readlines()
    print(text_file, "has", len(lines), "lines")



