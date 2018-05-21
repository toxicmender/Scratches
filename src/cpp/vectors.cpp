#include <iostream>
#include <vector>

int main(){
    std::vector <int> vic;
    std::vector::iterator it;
    int n;
    for(int i = 0; n != 42; ++i){
        std::cin >> n;
        vic.insert(n);
    }
    for (it = vic.begin(); it < vic.end(); it++){
        std::cout << ' ' << *it;
    }

    std::cout << std::endl;

    for (it: vic){
        std::cout << ' ' << *it;
    }
    return(0);
}
