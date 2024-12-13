import os


folderPath = r'C:\Users\rutvi\OneDrive\Desktop\Deep_Learning\Demo Project\Dataset\cadcd1\autonomoose_0022\processedmoose\image_00\data'
#folderPath = r'C:\Users\rutvi\OneDrive\Desktop\Deep_Learning\Demo Project\Dataset\cadcd1\autonomoose_0022\processedmoose\filtered_annotation_00'
 
fileSequence = 9000

for filename in os.listdir(folderPath):

    
    os.rename(folderPath + '\\' + filename, folderPath + '\\' + '000000' + str(fileSequence) + '.png')
    #os.rename(folderPath + '\\' + filename, folderPath + '\\' + '000000' + str(fileSequence) + '.txt')

    fileSequence +=1