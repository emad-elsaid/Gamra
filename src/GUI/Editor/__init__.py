import os
__all__ = os.listdir(os.path.normpath(__package__.replace('.','/')))
__all__ = [ i.split('.')[0] for i in __all__ if i.endswith('.py') and i!='__init__.py' and i!='Generic.py']