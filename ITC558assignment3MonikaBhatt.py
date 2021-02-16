import turtle
import easyshape
import check

def main(): 
    turtle.hideturtle() #Hiding turtle

    #default value of error
    error=0
    
    # Input the filename repetedly until a correct file name and extension is entered
    # FileNotFoundError exception is handled and user is invoked to input correct filename
    
    repeat='y'
    while (repeat=='y' or repeat=='Y'):
        try:
            file_name=input('Enter the filename: ')
            f=open(file_name, 'r')
            repeat='n'
        except FileNotFoundError:
            print('Enter a valid file name and extension')
    
    #Read all the lines in the file, and assign the value of each line to list named file_list
    #by splitting across comma
    #Sending each file_list incrementally to check for errors to the check module
    #Adding the number of errors to get an error count
    
    lines=f.readlines()
    count=len(lines)
    for index in range(0,count):
        line = lines[index]
        file_list=line.split(',')
        error=error+check.check(file_list,index)

    #Only proceed with the program if error count is 0, else print the number of errors and quit
        
    if error==0:
        for index in range(0,count):

            #Incrementally break each line into a list by splitting via comma
            #Assigning the first element of the list into the menu_input variable
            #strip() strips the extra spaces in the input and gives the raw value of the element
            
            line = lines[index]
            file_list=line.split(',')
            menu_input=file_list[0].strip()

            
            #This section runs if input = l or L
            if (menu_input=='L' or menu_input=='l'):

                #If only 3 inputs obtained for the line input, it is assumed that x1, y1 will be the
                #existing global current_x and current_y values
                
                if (len(file_list))==3:
                    x1=easyshape.current_x
                    y1=easyshape.current_y
                    x2=float(file_list[1].strip())
                    y2=float(file_list[2].strip())

                #If only 5 inputs obtained for the line input, it is assumed that x1, y1 will be the
                #first two values
                    
                elif (len(file_list))==5:
                    x1=float(file_list[1].strip())
                    y1=float(file_list[2].strip())
                    x2=float(file_list[3].strip())
                    y2=float(file_list[4].strip())

                #after values are assigned to the variables, the line function is called to draw the line
    
                easyshape.line(x1,y1,x2, y2)

                
            #This section runs if input = a or A
            elif (menu_input=='A' or menu_input=='a'): 
                radius=float(file_list[1].strip())
                angle=float(file_list[2].strip())

                #after values are assigned to the variables, the arc function is called to draw the arc

                easyshape.arc(radius, angle)


            #This section runs if input = t or T    
            elif (menu_input=='T' or menu_input=='t'): 
                content=file_list[1].strip()
                size=int(file_list[2].strip())
                x3=float(file_list[3].strip())
                y3=float(file_list[4].strip())

                #after values are assigned to the variables, the text function is called to write the text

                easyshape.text(content, size, x3, y3)

            #This section runs if input = s or S    
            elif (menu_input=='S' or menu_input=='s'):
                set_colour=file_list[1].strip()
                set_thickness=float(file_list[2].strip())
                
                #after values are assigned to the variables, the line function is called to draw the line
                
                easyshape.settings(set_colour, set_thickness)
                
    #If there are errors, user is prompted to fix the correspondng number of errors before proceeding
    
    else:
        print("Please fix the ", error, "errors before proceeding")
        
main()

