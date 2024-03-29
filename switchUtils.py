import maya.cmds as mc





def find_transforms_with_prefix_and_types(prefix="Ctrl_", types=None):
    """
    Find all transform nodes in the Maya scene with a given prefix in their name and
    that are associated with specified shape types.

    Args:
    - prefix (str): The prefix to search for in the object names.
    - types (list of str): The types of shapes to include (e.g., ['nurbsCurve', 'locator']).

    Returns:
    - List of transform nodes with the specified prefix in their names and associated with specified types.
    """
    if types is None:
        types = ['nurbsCurve', 'locator']
    
    # Find all transforms in the scene
    all_transforms = mc.ls(type='transform', long=True)
    
    # Filter those transforms to find ones with children that are of the specified types
    valid_transforms = [transform for transform in all_transforms
                        if any(mc.ls(mc.listRelatives(transform, children=True, fullPath=True) or [], type=shapeType) for shapeType in types)]
    
    # Further filter to include only those with the specified prefix in their name
    valid_transforms_with_prefix = [transform for transform in valid_transforms if prefix in transform]
    
    return valid_transforms_with_prefix
    
def select_transforms_with_prefix_and_types(prefix="Ctrl_", types=None):
    """
    Selects all transforms in the Maya scene with a specified prefix in their name and
    associated with specified shape types.

    Args:
    - prefix (str): The prefix to search for in the object names.
    - types (list of str): The types of shapes to include (e.g., ['nurbsCurve', 'locator']).
    """
    # Use the function to find the transforms with the given prefix and types
    valid_transforms = find_transforms_with_prefix_and_types(prefix, types)
    
    # Select the found transforms
    if valid_transforms:
        return valid_transforms
    else:
        print("No transforms found with prefix '{}' and types {}".format(prefix, types))