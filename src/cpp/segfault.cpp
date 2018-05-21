#include <iostream>

long long fibonacci(int n){
	if(n > 1){
		return(fibonacci(n-1) + fibonacci(n-2));
/*	}else if(n < 0){
		return(((long long)pow(-1, n+1)) * fibonacci(n));
*/	}else
		return(n);
}

int sequence(int n){
	int i, seed0 = 0, seed1 = 1;
	for (i = 0; i <= n/2; ++i){
		std::cout << seed0 <<'\t' << seed1 << '\t';
		seed0+=seed1;
		seed1+=seed0;
	}
	return(0);
}

int nsequence(int n){
	for(int i = 0; i <= n; ++i){
		std::cout << fibonacci(i) << '\t';
	}
	return(0);
}

int main(){
	int x;
	std::cout << "Enter #: ";
	std::cin >> x;
	std::cout << fibonacci(x) << std::endl;
//	std::cout << sequence(x) << "\b\b\b" <<std::endl;
	std::cout << nsequence(x) << "\b\b";
	return(0);
}
