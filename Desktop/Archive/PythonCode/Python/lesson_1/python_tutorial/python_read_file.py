import os
f = open("demofile.txt", "r")
if __name__ == '__main__':
    print(f.read())
if __name__ == '__main__':
    f = open("demofile.txt", "r")
    print(f.read(5))
if __name__ == '__main__':
    f = open("demofile.txt", "r")
    print(f.readline())
    # f.close()
    print(f.readline())
    print(f.readline())
if __name__ == '__main__':
    f = open("demofile.txt", "r")
    for x in f:
        print(x)

# 2. Python File Write
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
if __name__ == '__main__':
    f = open("demofile1.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    f = open("demofile1.txt", "r")
    print(f.read())
if __name__ == '__main__':
    f = open("demofile3.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()
    f = open("demofile3.txt", "r")
    print(f.read())

# 3. Create a New File
if __name__ == '__main__':
    f = open("myfile.txt", "w")
    f.write("a new empty file is created!")
    f.close()
    f = open("myfile.txt", "r")
    print(f.read())

# 4. Delete file
# use os.remove() method
if __name__ == '__main__':
    os.remove("myfile.txt")
if __name__ == '__main__':
    if os.path.exists("myfile.txt"):
        os.remove("myfile.txt")
    else:
        print("The file does not exist")
# 4.1 To delete an entire folder, use the os.rmdir() method: You can only remove empty folders.
if __name__ == '__main__':
    os.rmdir("abc")