import numpy as np
from midvoxio.voxio import vox_to_arr
import os
import tkinter as tk
from tkinter import filedialog

# Function to extract coordinates and colors from a VOX file and save them to a specified location
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
                    # Ensure the color values are within the range 0-255 and convert to integers
                    color = tuple(int(c * 255) if c <= 1 else int(c) for c in color)
                    occupied_voxels.append((x, y, z, color))

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate the output file name based on the input file name
    input_file_name = os.path.basename(vox_file_path)
    output_file_name = f"{os.path.splitext(input_file_name)[0]}_cnc.txt" #coordinate and colour
    output_file_path = os.path.join(output_dir, output_file_name)

    # Save the coordinates and colors to a text file
    with open(output_file_path, 'w') as f:
        finallist = []
        for voxel in occupied_voxels:
            f.write(f"Coordinate: ({voxel[0]}, {voxel[1]}, {voxel[2]}), Color: {voxel[3]}\n")
            #print(voxel[0],voxel[1],voxel[2])
            finallist.append((voxel[3],(voxel[0],voxel[1],voxel[2])))
   
    #print (finallist)
    return finallist
    #print(f"Coordinates and colors have been saved to {output_file_path}")

# Function to open a file dialog and select the VOX file
def select_vox_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    vox_file_path = filedialog.askopenfilename(title="Select VOX File", filetypes=[("VOX Files", "*.vox")])
    return vox_file_path

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select Folder")
    return folder_path

def algorithm(xyz):
    start = xyz[0][0] #[X][0] - colour, [X][1] - coordinates
    #print (start)
    NewL = []
    print (xyz[0][0])
    print (xyz[1][0])

    if (xyz[0][0] == xyz[1][0]):
        print("true")

    



# Main function
def main():
    # User input for VOX file path and output directory
    #vox_file_path = select_vox_file()
    vox_file_path = "C:\\Users\\mkapur\\Desktop\\MagicaVoxel-0.99.7.1-win64\\MagicaVoxel-0.99.7.1-win64\\vox\\Projects\\car1.vox"
    output_dir = "C:\\Users\\mkapur\\Desktop\\MagicaVoxel-0.99.7.1-win64\\MagicaVoxel-0.99.7.1-win64\\vox\\Projects\\Coordinates"
    #print (finallist)
    #output_dir = select_folder()

    # Extract voxel coordinates and colors and save them to the specified location
    coords = extract_voxel_coordinates_and_colors(vox_file_path, output_dir)
    algorithm(coords)
    #print("Format: (Colour - RGB, Coordinate)")
    #print (coords[0])


if __name__ == "__main__":
    main()
