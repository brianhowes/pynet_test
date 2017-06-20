
#!/usr/bin/env python

f = open("new_file.txt","w")
f.write('I love to ride!!!')
f.close()

with open("new_file.txt","a") as f:
    f.write("Always!!!/n")





