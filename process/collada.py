import collada


def loadColladaFile(route):
    """ Loading the file """
    mesh = collada.Collada(route)
    
    return mesh

def applyTransformations(mesh, trans):
    """"""