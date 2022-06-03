from meshtool.filters.panda_filters.pandacore import setupPandaApp
import base64
from PIL import Image
import collada

from panda3d.core import PNMImage, StringStream


def saveScreenshot(p3dapp, filename):

    p3dapp.taskMgr.step()
    p3dapp.taskMgr.step()
    pnmss = PNMImage()
    p3dapp.win.getScreenshot(pnmss)
    resulting_ss = StringStream()
    pnmss.write(resulting_ss, "screenshot.png")
    screenshot_buffer = resulting_ss.getData()
    base = (base64.b64encode(screenshot_buffer)).decode('utf-8')
    f = open("b64.txt", "w")
    f.write(base)
    f.close()

    with open("foo.png","wb") as f:
        f.write(base64.b64decode(base))



def transformations(mesh, pipeline):
    """ Define the pipeline to flow """
    for camera in mesh.cameras:
        print(camera.znear, camera.zfar)
    if(len(pipeline) > 0):
        """Process"""
        if('--image' in pipeline):
            """ Process to take an SS """
            p3dApp = setupPandaApp(mesh)
            print(p3dApp)
            saveScreenshot(p3dApp, pipeline['--image'])
            return mesh
    else:
        """"""
        return 'There\'s no process to achieve'