import glob, os
import random


# put your own path here
dataset_path = '/home/son/obdetect/OIDv4_ToolKit/Images4'

# Percentage of images to be used for the validation set
percentage_test = 5

# Populate the folders
p = percentage_test/100
i = 0
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))		#title = ten file, ext = ten duoi file (.jpg, .txt, ...)
    if random.random() <=p :
        os.system(f"cp {dataset_path}/{title}.jpg data5/images/valid")
        os.system(f"mv data5/images/valid/{title}.jpg data5/images/valid/img{i}.jpg")
        os.system(f"cp {dataset_path}/{title}.txt data5/labels/valid")
        os.system(f"mv data5/labels/valid/{title}.txt data5/labels/valid/img{i}.txt")
    else:
        os.system(f"cp {dataset_path}/{title}.jpg data5/images/train")
        os.system(f"mv data5/images/train/{title}.jpg data5/images/train/img{i}.jpg")
        os.system(f"cp {dataset_path}/{title}.txt data5/labels/train")
        os.system(f"mv data5/labels/train/{title}.txt data5/labels/train/img{i}.txt")
    i = i+1
