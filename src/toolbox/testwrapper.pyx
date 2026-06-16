cdef extern from "hello.hpp":
    void hello_cpp()

def hello():
    return hello_cpp()
