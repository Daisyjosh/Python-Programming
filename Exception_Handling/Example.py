try:
    x = int(input("Enter x: "))
    ans = 10/x

except ZeroDivisionError: # ZeroDevisionError (Builtin Error Message) if the input is zero as a divisor.
    print("Divide by 0 is not allowed")

except ValueError: # ValueError (Builtin Error Message) when invalid type of input is entered.
    print(f"Invalid Error")

else: # If it passes the exceptions then else block is excuted.
    print(f"ans = {ans}")

finally: # Irrespective of the error thrown finally block is excuted.
    print("End of program")
    
