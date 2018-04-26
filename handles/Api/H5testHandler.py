

from core.CoreHandler import CoreHandler

import h5py

class H5testHandler(CoreHandler):
    def get(self): 
        f = h5py.File("./mytestfile.hdf5","w")
        f.create_dataset("mydataset", (100,), dtype="i")
        self.write("over")
