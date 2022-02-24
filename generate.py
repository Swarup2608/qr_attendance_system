from MyQR import myqr
import os
import base64

# IMPORT AND READ FILE
f = open('students.txt','r')
lines = f.read().split("\n")
print(lines)

for i in range(len(lines)):
    data = lines[i].encode()
    name = base64.b64encode(data)

    version,level,qr_name = myqr.run(
        str(name),
        level = 'H',
        version=1,
        picture = "bg.png",
        colorized=True,
        brightness=1.0,
        save_name=str(lines[i]+'.bmp'),
        save_dir=os.getcwd()
    )