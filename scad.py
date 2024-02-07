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
        #filter = ""
        filter = "base"

        kwargs["save_type"] = "none"
        #kwargs["save_type"] = "all"
        
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
        part["name"] = "base"
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

def get_base(thing, **kwargs):

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


    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"polyg"
    p3["sides"] = 6
    p3["radius"] = (0.25 * 25.4) / 2  * 1.1546 # 7.32 hopefully
    p3["height"] = 26
    p3["depth"] = 4
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    #p3["m"] = "#"    
    return_value.append(oobb_base.oobb_easy(**p3))

    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oring"
    dep = 0.25 * 25.4
    p3["depth"] = dep
    p3["id"] = 5.588 - dep/2
    pos1 = copy.deepcopy(pos)
    pos1[2] += 17.745
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