
n = 5 # numero de lineas de la parte superior del patron

# parte superior del patron 
for i in range(1, n, +1):
    print('*'*i)
    
# Parte inferior del patron 

for i in range(n-1, 0, -1):
    print('*'*i)
