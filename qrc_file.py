import os

f = open("files.qrc", "w+")

f.write("<RCC>")
f.write('\n\t<qresource>')

for file_name in os.listdir("icons/dark"):
    f.write("\n\t\t<file>icons/dark/" + file_name + "</file>")

for file_name in os.listdir("icons/light"):
    f.write("\n\t\t<file>icons/light/" + file_name + "</file>")

for file_name in os.listdir("icons/images"):
    f.write("\n\t\t<file>icons/images/" + file_name + "</file>")

f.write('\n\t</qresource>')
f.write('\n</RCC>')

f.close()


