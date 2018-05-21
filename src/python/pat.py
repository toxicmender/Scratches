#!usr/bin/python3

#Patterns correctly displayed until input size < 10

size = int( input( "Enter size: " ) )
lst = list( range( 1, size + 1 ) )

for i in range( 1, size + 1 ):
    print( lst[:i] )

for i in range( 1, size ):
    print( lst[:-i] )

print('\n')

l = str(lst)
l = l.__len__()

ns = str()
for i in range( 0, l ):
    ns += ' '

temp = str()
for i in range( 1, size + 1 ):
    #i*3 because each element in list adds a strlen of 3, ie; 'int' ',' ' '
    temp += ns[:( l - (i*3) )] + str( lst[:i]  ) + '\n'

for i in range( 1, size ):
    temp += ns[:( (i*3) )] + str( lst[:-i]  ) + '\n'

print(temp)
