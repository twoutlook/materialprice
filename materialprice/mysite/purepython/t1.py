file_object = open('data.txt')
print ("t1...")
name = set ()
q = set ()


try:
    lines = file_object.readlines( )
    for line in lines:
        items = line.split()
        name.add(items[0])
        q.add(items[1]+"Q"+items[2])

    print(name)
    print(q)

        # for item in line.split():
        #     print(item)
finally:
  file_object.close( )

try:
    for line in lines:
        items = line.split()
        print (items)

        
finally:
    pass
