import platform

print("Current machine type")
print(platform.machine()) # Apple M1, M2, M3, M4, Raspberry Pi : arm64; for intel/AMD: x86
print ("-------------------------------\n")

print("Current Processor Type:")
print(platform.architecture())
print ("-------------------------------\n")