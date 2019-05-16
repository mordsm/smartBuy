import pandas as pd
import sys
from  .Attribute import Attribute
from  .smartUtils import *

from smartBuy.resources.ManagingData import *
class CoordinatedData:
    def __init__(self, csvPath, item,name, value):
        self.df = pd.read_csv(csvPath)
        self.item = item
        self.value = value
        self.name = name
        self.type = typ
        self.c_value = self.get_cordinated_value()
    def get_type_by_name(self):
        try:
            nameToType[self.item][self.name]
        except Exception as e:
            print (e)
            send_mail("no type exists for {} {}".format(self.item,self.name))
            sys.exit(1)


    def coordinate(self):
        for key, value in self.df.iteritems():
            grokIt(self.c_value.get_cordinated_value()
        for key, value in self.df.iteritems():
            self.c_value.get_cordinated_value()

    def __gt__(self, other):
        if (self.c_value > other.c_value):
            return True
        else:
            return False
    def __lt__(self, other):
        if (self.c_value < other.c_value):
            return True
        else:
            return False
    def get_cordinated_value(self):
        if isinstance(self.type, int):
            self.c_value = self.value
        elif isinstance(self.type, bool):
            if self.value == True:
                self.c_value = 1
            else:
                self.c_value = 0


