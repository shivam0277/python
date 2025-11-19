#File Handling
#r=Read
#w=Write
#a=Append
#x=Create

#Read - error if it doesn't exist
#f = open("Notes.txt", "r") 
#or
f= open("Notes.txt")
print(f.read())
#print(f.read(4)) 
#print(f.readline())  reads only one line
#print(f.readlines()) reads all lines and returns a list of lines


#for line in f:
    # print(line)

f.close()# close the file to free up system resources and avoid data corruption

try:
    f = open("Notes.txt", "r")
    content = f.read()
    print(content)
except:
    print("An error occurred while trying to read the file.")
finally:
    f.close() 

#append - if the file doesn't exist, it will be created
f = open("Notes.txt", "a")
f.write("\nThis is an appended line.")
f.close()

f = open("Notes.txt", "r")
print(f.read())
f.close()

#write - overwrites existing file or creates a new one
f = open("Notes.txt", "w")
f.write("This is a new line, overwriting the old content.")
f.close()

f = open("Notes.txt", "r")
print(f.read())
f.close()

