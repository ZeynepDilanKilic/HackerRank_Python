thickness = int(input())
h = 'H'

def upArrow(thickness):
    for i in range(thickness):
        print((h*i).rjust(thickness-1)+h+(h*i).ljust(thickness-1))
    

def downArrow(thickness):
    for i in range(thickness):
        print(((h*(thickness-i-1)).rjust(thickness)+h+(h*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
 
    
def center(thickness):
    for i in range(thickness+1):
        print((h*thickness).center(thickness*2)+(h*thickness).center(thickness*6))
    for i in range((thickness+1)//2):
        print((h*thickness*5).center(thickness*6))
    for i in range(thickness+1):
        print((h*thickness).center(thickness*2)+(h*thickness).center(thickness*6))
        
    
upArrow(thickness)
center(thickness)
downArrow(thickness)

