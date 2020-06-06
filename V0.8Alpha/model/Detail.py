#######################################################
#
# detail.py
# Python implementation of the Class detail
# Generated by Enterprise Architect
# Created on: 11-Feb-2020 11:08:07 AM
# Original author: Corvo
#
#######################################################


class Detail:
    """An optional element used to hold CoT sub-schema. empty element
    """
    def __init__(self, CoTType):
        CoTTypes = {
                        'initialConnection': self.initialConnection()
                    }
        for x in CoTTypes.keys():
            if CoTType == x:
                CoTTypes[x]
            else:
                pass
    
    def ping(self,info):
        pass
    
    def initialConnection(self):
        from .takv import takv
        from .contact import contact
        from .uid import uid
        from .Precisionlocation import Precisionlocation
        from .group import group
        from .status import status
        from .track import track
        from .marti import marti
        self.m_takv = takv()
        self.m_contact = contact()
        self.m_uid = uid()
        self.m_precisionlocation = Precisionlocation()
        self.m_group = group()
        self.m_status = status()
        self.m_track = track()
        self.m_marti = marti()