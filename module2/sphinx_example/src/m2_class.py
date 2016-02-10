"""
.. module:: m2_decorator
    :synopsis: This is a class example for module 2

.. moduleauthor:: RickChung
"""

class ZhongXiaoQiao:
    """
    ZhongXiaoQiao is a blueprint of bridge used to generate ZhongXiaoQiao. 
    """
    def __init__(self, width, height, depth):
        """
        Construct a new ZhongXiaoQiao object.

        Args:
            width (float): the width of the bridge
            height (float): the height of the bridge
            depth (float): the depth of the bridge

        Returns:
            None

        Constructor of ZhongXiaoQiao 

        >>> bridge = ZhongXiaoQiao(1.0, 2.0, 3.0)
        """
        self.width  = width
        self.height = height
        self.depth  = depth

    def getVolume(self):
        """
        Get the volume of this bridge.

        Returns:
            float. The volume of this bridge.

        No description.

        >>> bridge.getVolume()
        """
        return self.width*self.height*self.depth

if __name__ == '__main__':
    bridge = ZhongXiaoQiao(2, 20, 3)
    print('bridge width = '+str(bridge.width))
    print('bridge height = '+str(bridge.height))
    print('bridge depth = '+str(bridge.depth))
    print('bridge volume = '+str(bridge.getVolume()))