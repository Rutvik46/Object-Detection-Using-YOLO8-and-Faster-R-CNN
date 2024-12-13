"""
@author: zamanm16
"""

import os
import shutil

def arrange_data():
    os.mkdir('cadcd_dataset')
    os.mkdir('cadcd_dataset/images')
    annotation_destination = 'cadcd_dataset/dataset_annotations.txt'
    names_ = 'cadcd_dataset/dataset_names.txt'
    yolo_annotation_lines = []
    dirs = [item for item in os.listdir() if item.startswith('autonomoose_')]
    dirs.sort()
    datapoint_counter = 0
    classes = {}
    for folder in dirs:
        data_folder = os.path.join(folder, 'processedmoose')
        image_folders = [os.path.join(data_folder, item) for item in os.listdir(data_folder) if item.startswith('image')]
        image_folders.sort()
        annotation_folders = [os.path.join(data_folder, 'filtered_annotation_{}'.format(item[-2:])) for item in image_folders]
        for image_folder, annotation_folder in zip(image_folders, annotation_folders):
            images = os.listdir(os.path.join(image_folder, 'data'))
            images.sort()
            annotations = os.listdir(annotation_folder)
            annotations.sort()
            names = [format(i, '05d') for i in range(datapoint_counter, datapoint_counter+len(images))]
            datapoint_counter += len(names)
            for idx in range(len(names)):
                image_source = os.path.join(os.path.join(image_folder, 'data'), images[idx])
                image_destination = './cadcd_dataset/images/{}.png'.format(names[idx])
                annotation_file = open(os.path.join(annotation_folder, annotations[idx]), 'r')
                annotation_lines = annotation_file.readlines()
                the_line = image_destination
                for line in annotation_lines:
                    the_data = line.split(' ')
                    class_name = the_data[0]
                    xmin = int(float(the_data[4]))
                    xmax = int(float(the_data[6]))
                    ymin = int(float(the_data[5]))
                    ymax = int(float(the_data[7]))
                    if xmin==xmax or ymin==ymax:
                        continue
                    if not class_name in classes.keys():
                        classes[class_name] = len(classes.keys())
                    the_line += ' {},{},{},{},{}'.format(xmin, ymin, xmax, ymax, classes[class_name])
                the_line += '\n'
                yolo_annotation_lines.append(the_line)
                shutil.copy(image_source, image_destination)
    yolo_format_file = open(annotation_destination, 'w')
    yolo_format_file.writelines(yolo_annotation_lines)
    names_data = ''
    for name in classes.keys():
        names_data += '{}\n'.format(name)

    class_names_file = open(names_, 'w')
    class_names_file.writelines(names_data)

if __name__ == '__main__':
    arrange_data()
