import numpy as np
from midvoxio.voxio import vox_to_arr
import os
import tkinter as tk
from tkinter import filedialog

# Function to open a file dialog and select the VOX file
def select_vox_file():
    root = tk.Tk()
    root.withdraw()  
    vox_file_path = filedialog.askopenfilename(title="Select VOX File", filetypes=[("VOX Files", "*.vox")])
    return vox_file_path

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Folder")
    return folder_path

def indexAdded(abc):
    modList = []
    for i, element in enumerate(abc, start=1):
        modList.append((*element,i))
    return modList
    
def addIndex(lst):
    # for index, xx in enumerate(lst):
    #     lst[index] = (xx, index+1)
    #    #print (lst[index])
    
    newL = []
    for i in range(len(lst)):
        newL.append((lst[i],i+1))
        #print(newL[i])

    return newL

def neighborCheck(lst):
    #takes full list as input, extracts coordinates.
    #counts pieces with touching faces
    #CUrrently appends sum of coordinates as a new element, but that will bereplaced by the neighbor count
    coords = []
    neighborList = []
    first = 0
    last = len(lst)-1


    for i in range(len(lst)):
        coords.append(lst[i][1])

    for i in range(len(coords)):
        #print (coords[i])

        #logic for first and last:
        neighbors = 0
        print (coords[i])
        for xx in coords:
            print (xx)

            if i == first:
                print ("first")

            elif i == last:
                print ("last")

            else:
                print ("other")            

            if coords[i] == xx:
                print ("yes")
            else:
                print ("no")



        print ("___________________________________________________________")
        neighbors = i
        #print (coords[i])
        newT = (coords[i], neighbors,)
        neighborList.append(newT)

        #reference: newT = (coords[i], (coords[i][0] + coords[i][1] + coords[i][2]),)

    # for xx in coords:
    #     #xum = xx[0]+xx[1]+xx[2]
    #     #new_T = (xx, xum,)
        
    #     #sorting logic here
    #     #print (xx[0])


    #     #adding to the new list to get form ((x,y,z),#neighbors)
    #     newT = (xx, (xx[0] + xx[1] + xx[2]),)
    #     neighborList.append(newT)
    

    
    return neighborList


def countColours(bcd):
    count_dict = {}
    for item in bcd:
        first = item[0]
        if first in count_dict:
            count_dict[first] +=1
        else:
            count_dict[first] = 1
    
    return count_dict

def sortByColour(xyz):

    x = len(xyz)
    for i in range(x):
        for j in range(0, x-i-1):
            if xyz[j][0] > xyz [j+1][0]:
                xyz[j], xyz[j+1] = xyz[j+1], xyz[j]


    xyz1 = indexAdded(xyz)


    return xyz1

# extract vox coordinates and 
def extract_voxel_coordinates_and_colors(vox_file_path, output_dir):
    # Load the VOX file
    vox_array = vox_to_arr(vox_file_path)

    # Extract the coordinates and colors of occupied voxels
    occupied_voxels = []
    for x in range(vox_array.shape[0]):
        for y in range(vox_array.shape[1]):
            for z in range(vox_array.shape[2]):
                if vox_array[x, y, z, 3] != 0:  # Check if the voxel is occupied (non-transparent)
                    color = (vox_array[x, y, z, 0], vox_array[x, y, z, 1], vox_array[x, y, z, 2])
                    # convert color to rgb
                    color = tuple(int(c * 255) if c <= 1 else int(c) for c in color)
                    occupied_voxels.append((x, y, z, color))

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # generate output
    input_file_name = os.path.basename(vox_file_path)
    output_file_name = f"{os.path.splitext(input_file_name)[0]}_cnc.txt" #coordinate and colour
    output_file_path = os.path.join(output_dir, output_file_name)

    # coordinates = []
    # for xx in occupied_voxels:
    #     coordinates.append((xx[0],xx[1],xx[2]))
    
    #coordinates = addIndex(coordinates)


    sorted_voxels = sortByColour(occupied_voxels)

    finallist = []   
    for voxel in sorted_voxels:
        finallist.append((voxel[3],(voxel[0],voxel[1],voxel[2])))
    
    finallist1 = sortByColour(finallist)

    lengthhh = len(finallist1) - 1

    counted=countColours(finallist1)
    with open(output_file_path, 'w') as f:
        for voxel in finallist1:
            if voxel != "done elem":
                #f.write(f"Coordinate: {voxel[1]}, Color(rgb): {voxel[0]}, Index: {voxel[2]}\n")
                f.write(f"Coordinate: {voxel[1]}, Color(rgb): {voxel[0]}\n")

    
        f.write(f"\nTotal *insert product name here* used: {finallist1[lengthhh][2]}\n")
        for key, value in counted.items():
            f.write(f"{key}: {value}\n")

        


    #print(f"Coordinates and colors have been saved to {output_file_path}")
    return finallist1

# Main function
def main():

    #vox_file_path = select_vox_file() 
    #output_dir = select_folder()
    vox_file_path = "C:\\Users\\mkapur\\Desktop\\MagicaVoxel-0.99.7.1-win64\\MagicaVoxel-0.99.7.1-win64\\vox\\Projects\\tester1.vox"
    output_dir = "C:\\Users\\mkapur\\Desktop\\MagicaVoxel-0.99.7.1-win64\\MagicaVoxel-0.99.7.1-win64\\vox\\Projects\\Coordinates"
    #print (finallist)
   

    colorcoords= extract_voxel_coordinates_and_colors(vox_file_path, output_dir)
    #ooords = sortByColour(coords)
    #print (coords)
    yes = neighborCheck(colorcoords)
    print (yes)
    #print (coords[1])
    
    #print ("sorted by colour")

    # for yy in colorcoords:
    #     print(yy)
    
    # for zz in coords:
    #     print (zz)

if __name__ == "__main__":
    main()