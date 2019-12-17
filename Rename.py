import os
path1 = input("Please enter the video path: ")
path2 = input("Please enter the subtitle path: ")

f1 = os.listdir(path1)
f2 = os.listdir(path2)

# Rename PDF to MKV
# for i in f1:
#     oldname = path1 + os.sep + i
#     newname = path1 + os.sep + i.replace("pdf", "mkv")
#     os.rename(oldname, newname)
#     print(oldname, "---------->", newname)


# Rename ass to match the MKV
for i in range(len(f2)):
    video_name = f1[i].replace(".mkv", "")
    oldname2 = path2 + os.sep + f2[i]
    newname2 = path2 + os.sep + video_name + ".ass"
    os.rename(oldname2, newname2)
    print(oldname2, "---------->", newname2)
