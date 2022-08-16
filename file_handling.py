with open('testfile.txt', 'a') as file:
    file.write("\nI am happy \ntoday!")
    file.writelines(["\nFeels good to be Okay","\nI freaking love programming"])

import random
f = open("petnames.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))