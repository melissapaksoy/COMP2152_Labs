import os
import platform
import socket
import sys

print("Current Machine Type")
print(platform.machine())
print("==================================")

print("Current Processor Type")
print(platform.architecture())
print("==================================")

print("Set socket time out to 50 seconds")
print(socket.setdefaulttimeout(50))
print("Get the current socket time out")
print(socket.getdefaulttimeout())
print("==================================")

print("Get the current operation system type")
print(os.name)
print("Get the current operation system name")
print(platform.system())
print("==================================")

print("Get the current process ID")
print(os.getpid())

file_name = ("fdpractice.txt")
print(f"\n[Before Fork] Process {os.getpid()}")

file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getpid()}] Opened file_handle: {file_handle}")

file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()

print(f"\n[Before Process {os.getpid()}] Forking now")
pid = os.fork()

if pid == 0:
    # Child process
    print(f"\n[PID {pid} has Parent process ID: {os.getppid()}]")
    os.lseek(file_handle, 0, 0)

    print(f"\n[Child Process {os.getpid()}] File content: {os.read(file_handle, 100).decode()}]")
    os.close(file_handle)
    sys.exit(0)
else:
    # Parent PID
    print(f"\n[Parent Process ID: {pid}], Child PID: {pid}")
    print("Wait for he child to complete the modification")
    os.wait()
    print("Child Process finished the modification")
    file_object_TextIO.close()

print(f"\n[Process {os.getpid()}] File closed. Exiting...  ")
sys.exit(0)
