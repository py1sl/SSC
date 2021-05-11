""" 
facility module
Part of SSC
Author: S Lilley
"""


class Facility:
    """ """
    def __init__(self, systems_list):
        self.systems_list = systems_list
        self.build_cost = 0.0
        self.run_cost = 0.0
        self.availabilty = 1.0
             
    
    def calc_buildcost(self):
        """ """       
        for system in self.systems_list:
            self.build_cost += system.build_cost

            
    def calc_runcost(self):
        """ """       
        for system in self.systems_list:
            self.run_cost += system.run_cost