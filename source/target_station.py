""" 
target station facility system module
Part of SSC
Author: S Lilley
"""
import facility_system
class target_station(facility_system):
    """ """
    def __init__(self):
        self.instrument_list = []
        self.moderator_list = []
        self.num_instruments = None
        self.target_type = None
        self.num_moderators = None
        self.epb_length = None
