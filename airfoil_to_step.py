import sys
import os

# NOTE: If you are running this outside of the FreeCAD Python console, 
# you must append your FreeCAD binary path to sys.path.
# Example for Windows: sys.path.append('C:\\Program Files\\FreeCAD 0.21\\bin')
# Example for Linux: sys.path.append('/usr/lib/freecad/lib')

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD module not found.")
    print("Please add the FreeCAD 'bin' or 'lib' folder to your sys.path.")
    sys.exit(1)

def convert_dat_to_step(dat_filepath, step_filepath):
    points = []
    
    if not os.path.exists(dat_filepath):
        print(f"Error: Could not find {dat_filepath}")
        return

    try:
        # 1. Parse the .dat file
        with open(dat_filepath, 'r') as f:
            for line in f:
                # Skip comments or empty lines
                if not line.strip() or line.startswith('#'):
                    continue
                
                # Split line by spaces/tabs
                coords = line.strip().split()
                
                if len(coords) >= 2:
                    x = float(coords[0])
                    y = float(coords[1])
                    # If 2D (only X and Y), set Z to 0.0
                    z = float(coords[2]) if len(coords) >= 3 else 0.0
                    
                    points.append(FreeCAD.Vector(x, y, z))
        
        if len(points) < 2:
            print("Error: Not enough points to create a geometry. Need at least 2.")
            return

        # Optional: If this is a closed profile (like an airfoil), 
        # uncomment the next two lines to close the loop.
        # if points[0] != points[-1]:
        #     points.append(points[0])

        # 2. Create the geometry (A wire/polygon connecting the points)
        # If you want a smooth curve instead of straight segments, 
        # change makePolygon to Part.BSplineCurve(points).toShape()
        shape = Part.makePolygon(points)
        
        # 3. Export to STEP
        Part.export([shape], step_filepath)
        print(f"Success! Converted '{dat_filepath}' to '{step_filepath}'.")

    except Exception as e:
        print(f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    # Example usage
    INPUT_FILE = "profile.dat"
    OUTPUT_FILE = "output.step"
    
    convert_dat_to_step(INPUT_FILE, OUTPUT_FILE)