#include <iostream>

 void bitwisePractise(){
   int n;
   n=1;
   std::cout << "(n << 1|1) = " << (n << 1|1) << std::endl; //bitwise or =  so 1  bit shifted 1 is 2 (10),
   std::cout << "(2|1) = " << (2|1) << std::endl; // 01 or 10 = 11 = 3
   std::cout << "(n << (1|1)) = " << (n << (1|1)) << std::endl;
   std::cout << "(1|1) = " << (1|1) << std::endl;
   std::cout << "((n << 1)|1) = " << ((n << 1)|1) << std::endl; //bitwise or =  so 1  bit shifted 1 is 2 (10),
   std::cout <<  "(2*n+1) = " << (2*n+1) << std::endl;
   //std::cout << "(n << 1+1) = " << (n << 1+1) << std::endl; // -- produces warning asks for n << (1+1)
   std::cout << "(n << (1+1)) = " << (n << (1+1)) << std::endl;
   std::cout << "((n << 1) +1) = " << ((n << 1) +1) << std::endl;
   int x = 3;
   n = n | x; // equivalent to
   n |= x;
   std::cout << "n = " << n << std::endl;
   std::cout << "(1 << n) - 1 = " << (1 << n) - 1 << std::endl;
}

int main() {
    std::cout << "Hello, world!" << std::endl;
    bitwisePractise();
    return 0;
}

//interesting that n << 1|1 == (n << 1)|1  but n << 1+1 == n << (1+1). Bidmass for c++ functions?

//bitwise
