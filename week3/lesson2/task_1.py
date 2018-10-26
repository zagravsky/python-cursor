import os
import pprint

proj = r'/home/bob/Documents/HW_5'
united_list = []
def direct(proj):
    for root,dirs,files in os.walk(proj):
        if root not in united_list:
            count = root.count('/')
            if files:
                for i in files:
                    print('---------' * (count), i)
            if dirs:
                for j in dirs:
                    print('---------' * (count), j)
                    absPath = os.path.join(root, j)
                        # recursively calling the direct function on each directory
                    direct(absPath)
                        # adding the paths to the list that got traversed
                    united_list.append(absPath)

direct(proj)