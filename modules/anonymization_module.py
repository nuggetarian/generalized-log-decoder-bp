import os

directory = f'exported'
class AnonymizeForward:

    def anonymize(self):
        r = []
        for root, dirs, files in os.walk(directory):
            for name in files:
                r.append(os.path.join(root, name))
        return r
    
