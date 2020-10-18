import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy

m = numpy.array(object=[100, 100, 100])
m = m.astype(numpy.int32)
m_gpu = cuda.mem_alloc(m.nbytes)
cuda.memcpy_htod(m_gpu, m)

mod = SourceModule("""
  __global__ int getC(int m, int e, int n){
    return (m**e) % n
    }
  """)

# Write C code that gets C based off parameters passed in. easy!

func = mod.get_function("getC")
func(m_gpu, block=(100,100,100))