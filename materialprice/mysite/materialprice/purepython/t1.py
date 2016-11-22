file_object = open('data.txt')
print ("action#123")
try:
    lines = file_object.readlines( )
    for line in lines:
        for item in line.split:
            # print("xxx "+ item)
finally:
  file_object.close( )
