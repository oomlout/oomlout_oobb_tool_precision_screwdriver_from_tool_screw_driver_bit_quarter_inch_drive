import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    oomp_mode = "project"
    #oomp_mode = "oobb"

    if typ == "all":
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr", "laser", "true"]
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]

        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        names = []
        names.append("precision_screwdriver")
        names.append("precision_screwdriver_test")

        for name in names:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3["width"] = 1
            p3["height"] = 1
            #p3["thickness"] = 6
            p3["extra"] = "hex_head_2_5_mm"
            part["kwargs"] = p3
            nam = name
            part["name"] = nam
            if oomp_mode == "oobb":
                p3["oomp_size"] = nam
            parts.append(part)


    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        
        sort.append("name")
        sort.append("extra")
        #sort.append("width")
        #sort.append("height")
        #sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_precision_screwdriver_test(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    radius_big = 10
    radius_little = 4
    height_driver = 30
    depth_taper = 12
    #hex holder bottom
    
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"    
    p3["depth"] = depth_taper
    p3["shape"] = f"oobb_cylinder"  
    p3["r2"] = radius_big
    p3["r1"] = radius_little
    p3["zz"] = "bottom"
    p3["rot"] = [0,0,0]
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add cylinder top
    hex_offset = 10
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    dep = height_driver - hex_offset
    p3["depth"] = dep
    p3["radius"] = radius_big
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth_taper
    p3["pos"] = pos1
    p3["rot"] = [0,0,0]
    p3["zz"] = "bottom"
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)



    

    
    #get holder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    #p3["type"] = "p"
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1

    p3["rot"] = [0,0,0]
    p3["m"] = "#"    
    p3["clearance"] = 0.2
    p3["clearance_top"] = True
    return_value_2 = get_holder_blank(thing, **p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [0,0,180]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # left
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_precision_screwdriver(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #technical
    lift_bit = 10
    radius_little = 3.5/2
    radius_bit_main = 3.5/2

    #main
    radius_big = 10/2
    
    height_driver = 40
    #taper
    depth_taper = 5    
    #hex
    hex_side_ratio = 1.1547
    radius_bottom_hex = 10/2 * hex_side_ratio
    depth_bottom_hex = 6
    
    #bottom taper piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"    
        p3["depth"] = depth_taper
        p3["shape"] = f"oobb_cylinder"  
        p3["r2"] = radius_big
        p3["r1"] = radius_little
        p3["zz"] = "bottom"
        p3["rot"] = [0,0,0]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
    
    #main_cylinder
    if True:    
    #if False:    
        hex_offset = 10
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_driver - hex_offset
        p3["depth"] = dep
        p3["radius"] = radius_big
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_taper
        p3["pos"] = pos1
        p3["rot"] = [0,0,0]
        p3["zz"] = "bottom"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    
    #hex_bottom
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = depth_bottom_hex
        p3["radius"] = radius_bottom_hex
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_taper
        p3["pos"] = pos1        
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

    #get holder
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        #p3["type"] = "p"
        pos1 = copy.deepcopy(pos)
        pos1[2] += lift_bit
        p3["pos"] = pos1

        p3["rot"] = [0,0,0]
        p3["m"] = "#"    
        p3["clearance"] = 0.2
        p3["clearance_top"] = True
        p3["radius_bit_main"] = radius_bit_main
        return_value_2 = get_holder_blank(thing, **p3)

    #add lock nut
    if True:
        nut_wall_thickness = 2
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_nut"
        p3["depth"] = radius_big - nut_wall_thickness
        p3["radius_name"] = "m3"
        #p3["hole"] = True    
        pos1 = copy.deepcopy(pos)        
        pos1[0] += 0
        pos1[1] += 0
        pos1[2] += lift_bit + 12
        poss = []
        repeats = 6        
        shift_down = 0
        for i in range(repeats):            
            pos11 = copy.deepcopy(pos1)
            shift_down = -i * 2.75
            pos11[2] += shift_down
            poss.append(pos11)
        p3["pos"] = poss
        rot = [90,360/12,0]
        p3["rot"] = rot
        p3["m"] = "#"        
        oobb_base.append_full(thing,**p3)
        #add cylinder clearance
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_hole"
        dep = 12
        p3["depth"] = dep
        p3["radius_name"] = "m3"
        p3["include_nut"] = True
        p3["clearance"] = ["top", "bottom"]
        pos12 = copy.deepcopy(pos1)
        pos12[2] += shift_down
        p3["pos"] = pos12
        rot = [90,0,0]
        p3["rot"] = rot
        p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [0,0,180]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # left
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_precision_screwdriver_1(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    radius_big = 12/2
    radius_little = 4
    height_driver = 50
    depth_taper = 20
    lift_bit = 10
    #hex holder bottom
    
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"    
    p3["depth"] = depth_taper
    p3["shape"] = f"oobb_cylinder"  
    p3["r2"] = radius_big
    p3["r1"] = radius_little
    p3["zz"] = "bottom"
    p3["rot"] = [0,0,0]
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add cylinder top
    hex_offset = 10
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    dep = height_driver - hex_offset
    p3["depth"] = dep
    p3["radius"] = radius_big
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth_taper
    p3["pos"] = pos1
    p3["rot"] = [0,0,0]
    p3["zz"] = "bottom"
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)



    

    
    #get holder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    #p3["type"] = "p"
    pos1 = copy.deepcopy(pos)
    pos1[2] += lift_bit
    p3["pos"] = pos1

    p3["rot"] = [0,0,0]
    p3["m"] = "#"    
    p3["clearance"] = 0.2
    p3["clearance_top"] = True
    return_value_2 = get_holder_blank(thing, **p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [0,0,180]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # left
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


def get_holder_blank(thing, **kwargs):
    clearance = kwargs.get("clearance", 0)
    include_bit = kwargs.get("include_bit", True)
    clearance_top = kwargs.get("clearance_top", False)
    radius_bit_main = kwargs.get("radius_bit_main", 3.5/2)
    pos = kwargs.get("pos", [0, 0, 0])

    # setting up for rotation object
    typ = kwargs.get("type", "p")
    kwargs["type"] = "positive" #needs to be positive for the difference to work
    rot_original = get_rot(**kwargs)   
    kwargs.pop("rot", None)
    kwargs.pop("rot_x", None)
    kwargs.pop("rot_y", None)
    kwargs.pop("rot_z", None)

    # storing pos and popping it out to add it in rotation element     
    pos_original = copy.deepcopy(copy.deepcopy(kwargs.get("pos", [0, 0, 0])))
    pos_original_original = copy.deepcopy(pos_original)
    kwargs.pop("pos", None)
    

    
    return_value = []

    #hex shank
    if True:
        #hex bit is 0.25 inch6.35 mm
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["radius"] = (0.25 * 25.4) / 2  * 1.1546 + clearance# 7.32 hopefully 
        height_total = 28 + clearance 
        height_total_local = height_total       
        if clearance_top:
            height_total_local += 200
        else:
            height_total_local = height_total
        p3["height"] = height_total_local
        #p3["depth"] = 4
        pos1 = copy.deepcopy(pos)
        pos1[0] += clearance /2
        p3["pos"] = pos1
        #p3["m"] = "#"    
        return_value.append(oobb_base.oobb_easy(**p3))

    #donut cutouts
    if False:
        #1/16       1/16 inch bit is    1.5875 mm or    0.0625 inch
        #2/16       1/8 inch bit is     3.175 mm or     0.125 inch
        #3/16       3/16 inch bit is    4.7625 mm or    0.1875 inch
        #4/16       1/4 inch bit is     6.35 mm or      0.25 inch
        #5/16       5/16 inch bit is    7.9375 mm or    0.3125 inch
        #6/16       3/8 inch bit is     9.525 mm or     0.375 inch
        #7/16       7/16 inch bit is    11.1125 mm or   0.4375 inch
        #8/16       1/2 inch bit is     12.7 mm or      0.5 inch

        #middle one
        #the donut cutout
        if True:
            #smallest bit is 0.1875 3/16"            
            smallest_bit = 0.1875 * 25.4 - clearance
            # too small     bead_diameter = 0.25 * 25.4
            bead_diameter = (5/16) * 25.4 - clearance
            # too big       bead_diameter = (3/8) * 25.4
            diameter = smallest_bit
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oring"
            p3["depth"] = bead_diameter
            p3["id"] = diameter / 2
            pos1 = copy.deepcopy(pos)
            # top piece too short pos1[2] += height_total - (3/8) * 25.4
            # top piece even shorter pos1[2] += height_total - (5/16) * 25.4
            # top piece too longpos1[2] += height_total - (7/16) * 25.4
            pos1[2] += 17
            #pos1[2] += height_total
            p3["pos"] = pos1
            #p3["m"] = "#"
            return_value.append(oobb_base.oobb_easy(**p3))
    #joining screws
    if False:
        shift_screw = 17
        offset_screw  = 5 
        depth_screw = 12

        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        
        p3["depth"] = depth_screw
        p3["radius_name"] = "m3"
        p3["include_nut"] = True    
        pos1 = copy.deepcopy(pos)        
        pos1[0] += offset_screw
        pos1[1] += -depth_screw/2
        pos1[2] += shift_screw
        p3["pos"] = pos1
        rot = [90,360/12,0]
        p3["rot"] = rot
        p3["m"] = "#"
        p3["clearance"] = ["top", "bottom"]
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        pos1 = copy.deepcopy(p3["pos"])        
        pos1[0] += -offset_screw * 2
        pos1[1] += depth_screw 
        p3["pos"] = pos1
        p3["m"] = "#"
        rot1 = copy.deepcopy(rot)
        rot1[2] += 180 

        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)
        # bottom one at 0,0,0
        # cone not a donut
        #p3 = copy.deepcopy(p3)
        #pos1 = copy.deepcopy(pos)
        #p3["pos"] = pos1
        #p3["m"] = "#"
        #return_value.append(oobb_base.oobb_easy(**p3))

    #cutout at bottom
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"tube_new"
        p3["height"] = 2
        p3["r2"]= 7.35/2 + clearance/2
        #p3["r1"]= 3.5/2
        p3["r1"]= radius_bit_main + clearance/2
        p3["wall_thickness"] = 8
        pos1 = copy.deepcopy(pos)        
        p3["pos"] = pos1
        #p3["m"] = "#"
        return_value.append(oobb_base.oobb_easy(**p3))

    if include_bit:
        #add bit
        p3 = copy.deepcopy(kwargs)
        #p3["type"] = "n"
        p3["shape"] = f"oobb_cylinder"
        dep = 100
        p3["depth"] = dep
        
        p3["radius"] = radius_bit_main + clearance / 2
        pos1 = copy.deepcopy(pos)         
        pos1[2] += -dep/2 + height_total
        p3["pos"] = pos1
        #p3["m"] = "#"
        return_value.append(oobb_base.oobb_easy(**p3))


    # packaging as a rotation object
    return_value_2 = {}
    return_value_2["type"]  = "rotation"
    return_value_2["typetype"]  = typ
    return_value_2["pos"] = pos_original
    return_value_2["rot"] = rot_original
    return_value_2["objects"] = return_value
    return_value_2 = [return_value_2]


    thing["components"].append(return_value_2)

def get_rot(**kwargs):
    rot = kwargs.get("rot", "")
    if rot == "":
        rot_x = kwargs.get('rot_x',0)
        rot_y = kwargs.get('rot_y',0)
        rot_z = kwargs.get('rot_z',0)
        rot = [rot_x, rot_y, rot_z]        
        kwargs["rot"] = rot
        kwargs.pop('rot_x', None)
        kwargs.pop('rot_y', None)
        kwargs.pop('rot_z', None)
        kwargs.pop("rot", None)

    return rot

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)