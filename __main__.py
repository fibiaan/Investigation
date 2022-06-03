from cmath import exp
import os, getopt, sys
from process.collada import *
import pipeline

def main(argv):
    transformations = dict()
    try:
        opts, args = getopt.getopt(argv, "hc:", ["image=", "base64="])
    except getopt.GetoptError:
        print('python ./ -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python ./ -c <inputColladaFile> --image <outputPNG> --base64 <outputBase64>')
            sys.exit()
        elif opt in ("-c", "--colladaFile"):
            inputfile = arg
        else:
            transformations[opt] = arg
        

    ext = inputfile.split('.')
    exists = os.path.exists(inputfile)
    if(ext[-1] == 'dae' and exists):
        mesh = loadColladaFile(inputfile)
        print('type of ', type(mesh))

        # print('camera infomation')
        # for camera in mesh.cameras:
        #     print(type(camera), dir(camera))
        #     print(camera.zfar, camera.znear)
        #     camera.zfar = 10
        #     camera.znear = 100

        for geo in mesh.geometries:
            print(geo)
            
        mesh.save()
        expected = pipeline.transformations(mesh, transformations)
        # expected = ''
        if(isinstance(expected, str)):
            print(expected)
        else:
            """"""
    else:
        print('Invalid -c argument')


if __name__ == "__main__":
    main(sys.argv[1:])
