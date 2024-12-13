"""
@author: zamanm16
"""

import os
import sys
import shutil
from concurrent.futures import ProcessPoolExecutor
from filter_one_scene import process_scene

def convert_kitti(core_number):

    #shutil.unpack_archive('2019_02_27.zip', '')

    
    scenes_list = os.listdir('C:/Users/rutvi/OneDrive/Desktop/Deep_Learning/Demo Project/Dataset/cadcd1/2019_02_27')
    scenes_list.remove('calib')
    #scenes_list.remove('results.txt')

    root_scene_list = []

    for scene in scenes_list:
        root = 'autonomoose_'+scene
        root_scene_list.append(root)

        os.mkdir(root)
        os.mkdir(os.path.join(root, 'calibmoose'))
        os.mkdir(os.path.join(root, 'devmoose'))
        os.mkdir(os.path.join(root, 'processedmoose'))
        shutil.copy(os.path.join('2019_02_27', scene)+'/3d_ann.json', os.path.join(root, '3d_annotations.json'))
        calib_files = [item for item in os.listdir('2019_02_27/calib') if item.endswith('yaml')]
        for calib in calib_files:
            shutil.copy(os.path.join('2019_02_27/calib', calib), os.path.join(f'{root}/calibmoose', calib))
        image_folders = [item for item in os.listdir(os.path.join('2019_02_27', scene)+'/labeled') if item.startswith('image')]+['lidar_points']
        for folder in image_folders:
            source = os.path.join('2019_02_27', scene) + '/labeled/'+folder
            destination = os.path.join(root, 'processedmoose') +'/{}'.format(folder)
            shutil.copytree(source, destination)

    # Do the conversion in parallel
    #for item in root_scene_list:
        #process_scene(item)
    with ProcessPoolExecutor(core_number) as ex:
        ex.map(process_scene, root_scene_list)

if __name__=='__main__':
    core_number = int(sys.argv[1])
    convert_kitti(core_number)