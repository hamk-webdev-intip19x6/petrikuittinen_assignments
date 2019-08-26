import sys
print("Python version:", sys.version)
print("Python path:", sys.path)
print("Platform:", sys.platform)
print("Command line arguments:")
for arg in sys.argv[1:]:
    print(arg)
print("Standard error", file=sys.stderr)
# same as print(input())
with sys.stdin as f:
    d = f.readline()
    print(d)
sys.exit(0)


