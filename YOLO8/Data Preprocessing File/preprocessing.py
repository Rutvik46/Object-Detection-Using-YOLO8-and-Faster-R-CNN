"""
@author: zamanm16
"""

import sys
sys.path.append('C:/Users/rutvi/OneDrive/Desktop/Deep_Learning/cadcd')
from convert_to_kitti import convert_kitti
from arrange_dataset_tf2 import arrange_data

if __name__=='__main__':
    core_number = 2
    convert_kitti(core_number)
    arrange_data()