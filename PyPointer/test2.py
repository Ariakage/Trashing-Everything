from .ptr import Value, Pointer

num: Value = Value(12)
num_ptr: Pointer = Pointer(num)
print(f"num addr.{num_ptr.address} val.{num_ptr.value.value}")
num_ptr.value.value = 34
print(f"num addr.{num_ptr.address} val.{num_ptr.value.value}")
print(f"{num.value}    |    {12}")