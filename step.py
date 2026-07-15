import os
import glob

def parse_airfoil_points(file_path):
    points = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    for line in lines:
        parts = line.split()
        if len(parts) == 2:
            try:
                x = float(parts[0])
                y = float(parts[1])
                points.append((x, y, 0.0))
            except ValueError:
                continue
    return points

def write_step_file(points, output_path, airfoil_name):
    if not points:
        print(f"Skipping {airfoil_name}: No valid coordinates found.")
        return

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("ISO-10303-21;\nHEADER;\n")
        f.write(f"FILE_DESCRIPTION(('Airfoil Profile for {airfoil_name}'),'2;1');\n")
        f.write(f"FILE_NAME('{airfoil_name}.stp','2026-07-15',('Batch Converter'),('Auto'),'','','');\n")
        f.write("FILE_SCHEMA(('AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }'));\nENDSEC;\nDATA;\n")
        
        f.write("#1 = DIRECTION('', (0.0, 0.0, 1.0));\n")
        f.write("#2 = CARTESIAN_POINT('', (0.0, 0.0, 0.0));\n")
        
        point_ids = []
        current_id = 10
        for p in points:
            f.write(f"#{current_id} = CARTESIAN_POINT('', ({p[0]}, {p[1]}, {p[2]}));\n")
            point_ids.append(f"#{current_id}")
            current_id += 1
            
        if point_ids:
            point_ids.append(point_ids[0])
            
        point_list_str = ", ".join(point_ids)
        polyline_id = current_id
        f.write(f"#{polyline_id} = POLYLINE('{airfoil_name}_Curve', ({point_list_str}));\n")
        
        f.write("ENDSEC;\nEND-ISO-10303-21;\n")
    print(f"Successfully converted: {airfoil_name} -> {os.path.basename(output_path)}")

def batch_convert_airfoils(source_directory, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        
    dat_files = glob.glob(os.path.join(source_directory, "*.dat")) + \
                glob.glob(os.path.join(source_directory, "*.DAT"))
                
    if not dat_files:
        print(f"No .dat or .DAT files located in '{source_directory}'.")
        return

    print(f"Found {len(dat_files)} airfoil files to convert...\n")
    
    for file_path in dat_files:
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        sanitized_name = base_name.replace(" ", "_") 
        output_step_path = os.path.join(target_directory, f"{sanitized_name}.stp")
        
        coords = parse_airfoil_points(file_path)
        write_step_file(coords, output_step_path, sanitized_name)

# Execution setup
input_folder = "./airfoils_dat"
output_folder = "./airfoils_step"

if __name__ == "__main__":
    batch_convert_airfoils(input_folder, output_folder)