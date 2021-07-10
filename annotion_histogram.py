import xml.etree.ElementTree as ET
import os
import matplotlib.pyplot as plt

path = "G:\\CALISMALAR\\mikrobiyoloji_projesi\\datasetler\\Mikro_basic\\Mikro_basic_hard_aug_pascalvoc\\train"  #Source path of your images and xml files. This path shouldn't contain subdirectory
 
class_name=""
dict={}


for filename in os.listdir(path):
    
    if filename.endswith('.xml'):
        tree = ET.parse(path+"\\"+filename)  # for Windows filesystem
        #tree = ET.parse(path+"/"+filename)  #for UNIX/LINUX filesystem uncomment this and comment the upper line
        root = tree.getroot()
        for node in root.iter('name'): #find the xml root with annotion's name containing
            class_name=node.text
            if class_name in dict:
                dict[class_name] +=1
            else:
                dict[class_name] =1


print(dict)

plt.bar(*zip(*dict.items()), color="red", label="labels")
plt.xticks(rotation=90)

plt.tight_layout()
plt.legend()
plt.show()