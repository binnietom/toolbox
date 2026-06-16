import cython

path = "../cpp/helloworld.cpp"

cdef extern from "hello.hpp":
    void hello()

def py_hello():
    hello()


if __name__ == "__main__":
    py_hello()
    
