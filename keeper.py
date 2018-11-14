# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:05:27 2018

@author: studdockj
"""


class FileKeeper():
    import pickle, os
    
    def __init__(self, item=False, title=False, path=False):
        self.repo = r'G:\3. VA\0. Systems\1. Reporting\Scripts\Pickles\\'
        self.input = item
        self.title = title
        self.path = path
        self.list = self.browse()

            
    def save(self, obj, filename, default_path=True):
        #Save pickle to default folder
        import pickle
        
        if filename[-2:] != '.P':
            filename += '.P'
            
        f = self.repo + filename
        
        if default_path:
            msg = 'Saved as {}'.format(f)
        else:
            msg = 'Saved to {}'.format(f)
            f = ''
            
        pickle.dump(obj, open(f, 'wb'))
        
        return msg
    
    def load(self, name):
        #Extract pickle from default folder by name or index number
        import pickle, os
        if type(name) == int:
            name = sorted(list(os.listdir(self.repo)))[name]
        
        try:
            if name.find('.') == -1:
                name += '.P'
            f = self.repo + name
            return pickle.load(open(f, 'rb'))
        except:
            print('Pickle not found.')

    def browse(self, *args):
        import os
        #Print a list of saved pickles in the default 
        [print(e, i) for e, i in enumerate(sorted(list(os.listdir(self.repo))))]
        
    def delete(self, nameornum):
        import os
        def confirm(fname):
            if fname in os.listdir(self.repo):
                deleteable = self.repo + fname
                q = input('Confirm delete for "{}" (Y/N):    '.format(deleteable))
                
                if q[0].upper() == 'Y':
                    os.remove(deleteable)
                    if fname in os.listdir(self.repo):
                        print('\nDelete Failed!')
                    else:
                        print('\nDelete Confirmed.')
                        print('\nNew List: \n')
                        self.browse()
                elif q[0].upper() == 'N':
                    print('\nDelete Cancelled.')
                    pass
                else:
                    confirm(fname)
        if type(nameornum) == int:
            file = sorted(list(os.listdir(self.repo)))[nameornum]
            confirm(file)
            
        else:
            confirm(nameornum)
                   
files = FileKeeper()
    