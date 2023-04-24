# import required module
import os
# assign directory
directory = f'exported'
 
# iterate over files in
# that directory
class AnonymizeForward:

    def anonymize(self):
        r = []
        for root, dirs, files in os.walk(directory):
            for name in files:
                r.append(os.path.join(root, name))
        return r
    
