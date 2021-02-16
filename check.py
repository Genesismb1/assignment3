import turtle

def check(list, index):
    menu_input=list[0].strip()

    #Default value of error=0, 0 will be returned if no errors occur
    #If errors occur, the value of error will be incremented
    
    error=0

    # This section runs if stripped value of menu_input has some value, i.e. is not null
    if menu_input.strip():


        if (menu_input=='L' or menu_input=='l'):

            #Since all input (except the first) for line is supposed to be float, we check all values

            #If length of list is 3, check the last 2 values incrementally for exceptions/errors
            #by sending the list to the exception_handling module
            
            if (len(list)==3):
                for pos in range(1,3):
                    error=error+exception_handling(list,index,pos)

            #If length of list is 5, check the last 4 values incrementally for exceptions/errors
            #by sending the list to the exception_handling module

            elif len(list)==5:
                for pos in range(1,5):
                    error=error+exception_handling(list,index,pos)
                    
            #Length for menu_input l or L should be 3 or 5
            else:
                print("\nIncorrect number of inputs in line ",index+1, list)
                error=error+1

                
        elif (menu_input=='A' or menu_input=='a'):

            #Since all input (except the first) for arc is supposed to be float, we check all values

            #If length of list is 3, check the last 2 values incrementally for exceptions/errors
            #by sending the list to the exception_handling module
            
            if (len(list)==3):
                for pos in range(1,3):
                    error=error+exception_handling(list,index,pos)

            #Length for menu_input a or A should be 3

            else:
                print("\nIncorrect number of inputs in line ",index+1, list)
                error=error+1

                
        elif (menu_input=='T' or menu_input=='t'):

            #Since the last three inputs for text is supposed to be float, we check those

            #If length of list is 5, check the last 3 values incrementally for exceptions/errors
            #by sending the list to the exception_handling module
            
            if (len(list)==5):
                for pos in range(2,5):
                    error=error+exception_handling(list,index,pos)

                # Since size of text cannot be 0 or -ve, we check it for errors
                
                if(float(list[2].strip())<=0):
                    print("\nValue", list[2].strip(), "is not a valid size, it should be positive in line", index+1, " value 3", list)
                    error=error+1
                    
            #Length for menu_input t or T should be 5

            else:
                print("\Incorrect number of inputs in line ",index+1, list)
                error=error+1


        elif (menu_input=='S' or menu_input=='s'):

            #Since the last input for text is supposed to be float, we check it only

            #If length of list is 3, check the last value for exceptions/errors
            #by sending the list to the exception_handling module
            
            if (len(list)==3):
                error=error+exception_handling(list,index,2)

                #Since turtle color should be valid, we check it and an incorrect color raises an exception
                
                try:
                    turtle.color(str(list[1].strip()))
                except:
                    print("\nValue ", list[1].strip(), " is not a valid color, enter a valid color in", index+1, " value 2", list)
                    error=error+1

                #Since thickness of the pen cannot be 0 or negative, we check it and incorrect pen size raises an exception
                    
                if(float(list[2].strip())<=0):
                    print("\nValue ", list[2].strip(), " is not a valid pen thickness, it should be positive in line", index+1, " value 3", list)
                    error=error+1
                    
            #Length for menu_input s or S should be 3
            
            else:
                print("\nIncorrect number of inputs in line ",index+1, list)
                error=error+1
                
        # If menu_input is not in (l,L,s,S,a,A,t,T), then we print that the menu_input is invalid in corresponding line

        else:
            print("\nInvalid input for menu option in line", index+1, " value 1", list)
            print("\n Menu option in first value of each line should be L/l for Line, A/a for Arc, T/t for Text or S/s for settings")
            error=error+1

    #Since error is added after each step, the final vaue of error is passed back to main module
            
    return error
    
def exception_handling(list,index,pos):

            #exception handling module for float values

            #Try each value passed into this function for Value, Type or other exceptions, and return error=1 if it occurs

            try:
                    value=float(list[pos].strip())
            except ValueError:
                print('\nEnter float value in line ', index+1, ' value ',pos+1, list)
                error=1
            except TypeError:
                print('\nType error in line ', index+1, ' value ', pos+1, list)
                error=1
            except:
                    print('\nError in line ', index+1, ' value ', pos+1, list)
                    error=1
            else:
                error=0

            #If error occurs, value 1 is returned. If not, value 0 is returned
                
            return error
turtle.hideturtle()
        
