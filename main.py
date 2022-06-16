import platform

#Computer network name
print("Computer network name: " + str(platform.node()))

#Machine type
print("Machine Type: " + str(platform.machine()))

#Processor type
print("Processor Type: " + str(platform.processor()))

#Platform type
print("Platform Type: " + str(platform.platform()))

#Operating system
print("Operating system: " + str(platform.system()))

#Operating system release
print("Operating system release: " + str(platform.release()))

#Operating system version
print("Operating system version: " + str(platform.version()))