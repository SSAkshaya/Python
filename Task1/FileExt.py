filename = input("Input the Filename: ")
f_extns = filename.split(".")
if f_extns[-1]=="py":
	print("The extension of the file is: 'python'")
elif f_extns[-1]=="java":
	 print("The extension of the file is: 'Java'")
elif f_extns[-1]=="cpp":
      print("The extension of the file is: 'C++'")
