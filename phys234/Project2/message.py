import serial
import time

dev = serial.Serial('COM7')
time.sleep(3)
# Variables Used
sharedPrime =23    # p
sharedBase = 5      # g
 
aliceSecret = 6     # a
 
# Begin
print( "Publicly Shared Variables:")
print( "    Publicly Shared Prime: " , sharedPrime )
print( "    Publicly Shared Base:  " , sharedBase )
 
A = (sharedBase ** aliceSecret) % sharedPrime
dev.write(str(A).encode())
time.sleep(3)
print("    Bob Sends Over Public Chanel: ", A )
B = dev.readline()
time.sleep(3)
B = int(B.decode().rstrip())
print( "\n------------\n" )
print( "Privately Calculated Shared Secret:" )

shared_secret = (B**aliceSecret) % sharedPrime
print( "    Bob Shared Secret: ", shared_secret )