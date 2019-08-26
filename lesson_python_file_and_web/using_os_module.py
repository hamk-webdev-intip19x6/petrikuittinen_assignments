import os
print("current working directory", os.getcwd())
os.chdir('/tmp') # Change current working directory
# run system commands, which can be risky!
os.system('mkdir example123')
print(os.system('ls -la'))
print("passwd size", os.lstat('/etc/passwd').st_size)
os.system('rmdir example123')
print("HOME", os.environ["HOME"])
print("PATH", os.environ["PATH"])
f = open("test.txt", "w")
f.write("One\n") # starts write to internal buffer
os.fsync(f.fileno()) # force changes to disk
f.close()
os.unlink("/tmp/test.txt") # remove file
