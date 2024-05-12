import copy
import opsc
import oobb
import oobb_base

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "precision_screwdriver_test"

        #kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        kwargs["modes"] = ["3dpr", "laser", "true"]
        #kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 5
        kwargs["height"] = 5
        kwargs["thickness"] = 35

    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "test" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        part["kwargs"] = p3
        part["name"] = "bit_blank"
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        part["kwargs"] = p3
        part["name"] = "bit_holder_test"
        parts.append(part)

        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        part["kwargs"] = p3
        part["name"] = "precision_screwdriver_test"
        parts.append(part)
        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")

def get_precision_screwdriver_test(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", True)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    height_driver = 60

    #hex holder bottom
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"polyg"  
    p3["sides"] = 6
    p3["radius"] = 6
    p3["height"] = height_driver        
    p3["rot"] = [0,90,0]
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
    p3["radius"] = 8
    pos1 = copy.deepcopy(pos)
    pos1[0] += hex_offset
    p3["pos"] = pos1
    p3["rot"] = [0,90,0]
    p3["zz"] = "bottom"
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)



    #add coinnecting screws
    if True:
        shift_screw = 35
        offset_screw  = 15
        
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        depth_screw = 12
        p3["depth"] = depth_screw
        p3["radius_name"] = "m3"
        p3["include_nut"] = True    
        pos1 = copy.deepcopy(pos)        
        pos1[0] += shift_screw
        pos1[2] += depth_screw/2
        p3["pos"] = pos1
        p3["m"] = "#"
        p3["clearance"] = ["top", "bottom"]
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        pos1 = copy.deepcopy(p3["pos"])
        pos1[0] += offset_screw
        pos1[2] += -depth_screw
        p3["pos"] = pos1
        p3["m"] = "#"
        p3["rot"] = [0,180,0]
        oobb_base.append_full(thing,**p3)

    
    #get holder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1

    p3["rot"] = [0,90,0]
    p3["m"] = "#"    
    p3["clearance"] = 0.5
    return_value_2 = get_holder_blank(thing, **p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[1] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


def get_bit_holder_test(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", True)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"    
    dep = 10
    width = 35
    height = 25
    depth = dep
    size = [width, height, depth]
    p3["size"] = size
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[0] += width/2 - 2
    pos1[2] += -dep/2
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add coinnecting screws
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["depth"] = dep
    p3["radius_name"] = "m3"
    p3["include_nut"] = True    
    pos1 = copy.deepcopy(pos)
    shift_screw = 15/2
    pos1[0] += width/2 - 2
    pos1[1] += shift_screw
    pos1[2] += dep/2
    p3["pos"] = pos1
    p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    p3 = copy.deepcopy(p3)
    pos1 = copy.deepcopy(p3["pos"])
    #pos1[1] += shift_screw
    pos1[2] += -dep
    pos1[1] += -shift_screw * 2
    p3["pos"] = pos1
    p3["m"] = "#"
    p3["rot"] = [0,180,0]
    oobb_base.append_full(thing,**p3)

    
    #get holder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1

    p3["rot"] = [0,90,0]
    p3["m"] = "#"    
    p3["clearance"] = 0.5
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
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        #thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


def get_bit_blank(thing, **kwargs):

    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)
    

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    #oobb_base.append_full(thing,**p3)
    
    
    #get holder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    pos1 = copy.deepcopy(pos)
    #pos1[2] += 20
    p3["pos"] = pos1
    #p3["rot"] = [10,90,45]
    #p3["m"] = "#"
    p3["include_bit"] = False
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
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    
###### utilities

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

def get_holder_blank(thing, **kwargs):
    clearance = kwargs.get("clearance", 0)
    include_bit = kwargs.get("include_bit", True)

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
        height_total = 28
        p3["height"] = height_total + clearance
        p3["depth"] = 4
        pos1 = copy.deepcopy(pos)
        pos1[0] += clearance /2
        p3["pos"] = pos1
        #p3["m"] = "#"    
        return_value.append(oobb_base.oobb_easy(**p3))

    #donut cutouts
    if True:
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
        p3["r1"]= 5/2 + clearance/2
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
        
        p3["radius"] = 5 / 2 + clearance / 2
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


def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    func = globals()[f"get_{name}"]
    func(thing, **kwargs)

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)