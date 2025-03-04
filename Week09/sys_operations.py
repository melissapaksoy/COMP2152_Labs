import platform
import socket
import os

print("Current machine type")
print(platform.machine()) # Apple M1, M2, M3, M4, Raspberry Pi : arm64; for intel/AMD: x86
print ("-------------------------------\n")

print("Current Processor Type:")
print(platform.architecture())
print ("-------------------------------\n")

print("Set timeout of socket in seconds")
print(socket.setdefaulttimeout(50))
print ("-------------------------------\n")


print("Get timeout of socket in seconds")
print(socket.getdefaulttimeout())
print ("-------------------------------\n")

print("Operating System type")
print(os.name)
print ("-------------------------------\n")

print("Operating System name")
print(platform.system())
print ("-------------------------------\n")

print("Currect Process ID")
print(os.getpid())
print ("-------------------------------\n")

file_name = "fdpractice.txt"
#Printt the PID of the process before forking
print(f"[Before Fork] Process ID: {os.getpid()}")

# Open the file using os.open(low-level file handling)
file_handle =os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process ID {os.getpid()} opened file_handle: {file_handle}]")

#Convert the file handle into a file object for writing
file_object_TextIO = os.fdopen(file_handle, "w+")

#Write text to the file
file_object_TextIO.write("Lab Tue 10 to 12")
file_object_TextIO.flush() #Ensure content is written immediately

print(f"[Before Fork] Process ID: {os.getpid()}")

######
pid = os.fork()

if pid == 0:
    #Child process
    print(f"[Child Process] PID: {os.getpid()}, Parent Process ID: {os.getppid()}")
else:
    #Parent process
    print(f"[Parent Process] PID: {os.getpid()}, Child Process ID: {pid}")

