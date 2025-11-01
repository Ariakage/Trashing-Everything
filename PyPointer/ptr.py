import ctypes

class Value:
    def __init__(self, val: object) -> None:
        self._val = val
    
    @property
    def value(self) -> object:
        return self._val
    
    @value.setter
    def value(self, new_val: object) -> None:
        self._val = new_val

class Pointer:
    def __init__(self, obj: Value) -> None:
        self._addr = self._ptr(obj)
    
    def _ptr(self, obj: Value) -> int:
        return id(obj)
    
    def _deref(self, addr: int) -> Value:
        return ctypes.cast(addr, ctypes.py_object).value
    
    @property
    def value(self) -> Value:
        return self._deref(self._addr)
    
    @value.setter
    def value(self, new_obj: Value) -> None:
        self._addr = self._ptr(new_obj)
    
    @property
    def address(self) -> int:
        return self._addr
    
    @address.setter
    def address(self, new_addr: int) -> None:
        self._addr = new_addr