# Task-1
# import os
# import shutil

# os.mkdir("Example")
# os.mkdir("Example/subdirect")

# imgpath = "c:\Users\PC\Desktop/chess.jpeg"
# txtpath = "c:\Users\PC\Desktop/Task.txt"

# destinationimg = "Example/subdirect/chess.jpeg"
# destinationtxt = "Example/subdirect/Task.txt"

# shutil.copyfile(imgpath, destinationimg)
# shutil.copyfile(txtpath, destinationtxt)


# for filename in os.listdir("Example/subdirect"):
#     if filename.endswith(".txt"):
#         txt_file_path = os.path.join("Example/subdirect", filename)
#         shutil.move(txt_file_path, "Example")

# os.rmdir("Example/subdirect")
# print("Əməliyyat uğurla başa çatib.")


#########################################################################################################

# Task-2

def Find(points):
    places = [f"{i + 1}-ci" if i != 2 else f"{i + 1}-cu" for i in range(len(points))]
    return [place for xal, place in sorted(zip(points, places), reverse=True)]

points = [5, 3, 4, 2, 1]
print(Find(points))