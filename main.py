file_read = open("Codingal_txt.txt", "r")
print("File in read mode")
print (file_read.read())
file_read.close()

file_read = open("Codingal_txt.txt", "w")
print("File in write mode")
file_read.write("file in write mode")
file_read.write("Hi Iam a cat")
file_read.close()

file_read = open("Codingal_txt.txt", "a")
print("File in append mode")
file_read.write("\n file in append mode")
file_read.close()

