class Descriptor:
    def __init__(self,name=None,**args) -> None:
        self.name = name
        for key,value in args.items():
            setattr(self,key,value)
        
    def __set__(self,instance,value):
        isinstance.__dict__[self.name] = value 

class Typed(Descriptor):
    excepted_type = type(None)
    
