"""
@author: zamanm16
"""

import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

def visualize_image(image_name, annotation_file_path, class_file_path):
    annotation_file = open(annotation_file_path, 'r')
    class_file = open(class_file_path, 'r')
    classes = {idx:name[:-1] for idx, name in enumerate(class_file.readlines())}
    the_line = None
    for line in annotation_file.readlines():
        if image_name in line:
            the_line = line
            break
    assert the_line != None
    splitted_line = the_line.split(' ')
    image_path = splitted_line[0]
    found_objects = splitted_line[1:]
    image = mpimg.imread(image_path)
    fig, ax = plt.subplots()
    ax.imshow(image)
    for obj in found_objects:
        splitted_obj = obj.split(',')
        xmin = int(splitted_obj[0])
        ymin = int(splitted_obj[1])
        xmax = int(splitted_obj[2])
        ymax = int(splitted_obj[3])
        class_type = classes[int(splitted_obj[4])]
        width = xmax-xmin
        height = ymax-ymin
        rect = patches.Rectangle((xmin, ymin), width, height, linewidth=1, edgecolor='r', facecolor=None, fill=False)
        ax.add_patch(rect)
        ax.text(xmin, ymin, class_type, fontsize=6, color='red')
    plt.show()

if __name__=='__main__':
    image_name = sys.argv[1]
    annotation_file = sys.argv[2]
    class_file = sys.argv[3]
    visualize_image(image_name, annotation_file, class_file)


