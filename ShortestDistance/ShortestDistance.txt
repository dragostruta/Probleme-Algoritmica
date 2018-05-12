#include <assert.h>
class Solution {
public:
    vector<int> shortestToChar(string S, char C) {

	//Initializations
        int x[1000], nr_x = 0, min = 0;
        char s[1000];
        vector<int> myvector;

	//Convert String to Char array
        strcpy(s,S.c_str());
        
	//Stocarea pozitiilor parametrului 'C' in vectorul X
        for (int i = 0; i < strlen(s); i++){
            if(s[i] == C)
            {
                x[nr_x] = i;
                nr_x++;
            }
        }
        
	//Compararea si salvarea diferentei dintre pozitia parametrului 'C' si pozitia celorlalte elemente
        for (int i = 0; i < strlen(s); i++){
            for(int j = 0; j < nr_x; j++){
                if(j == 0){
                    min = abs(x[j] - i);
                } else {
                    if (min > abs(x[j] - i))
                        min = abs(x[j] - i);
                }
            }
            myvector.push_back(min);
        }  

	//Returnare vectorului final
        return myvector;
    }
public:
    //comparare a doua elemente
    static bool myfunction (int i,int j) { return (i<j); }
public:
    //Functia areEqual compara doi vectori, daca sunt egali returneaza True, altfel False
    bool areEqual(vector<int> arr1, vector<int> arr2, int n, int m)
    {
        
        if (n != m)
            return false;

        sort (arr1.begin(), arr1.end(), myfunction);
        sort (arr2.begin(), arr2.end(), myfunction);

        for (int i=0; i<n; i++)
             if (arr1[i] != arr2[i])
                return false;

        return true;
    }
public:
    //Teste
    void Test() {
        int arr[] = {1,0,1,0};
        vector<int> b (arr, arr + sizeof(arr) / sizeof(arr[0]) );
        
        vector<int> a;
        a = shortestToChar("mama",'a');
        assert(areEqual(a,b,a.size(),b.size()) == true);
        
        vector<int> bv (arr, arr + sizeof(arr) / sizeof(arr[0]) );
        
        vector<int> av;
        av = shortestToChar("",'a');
        assert(areEqual(av,bv,av.size(),bv.size()) == false);
        
        int arr2[] = {0,1,0,1,2,3,4,5,6,7,8};
        vector<int> b2 (arr2, arr2 + sizeof(arr2) / sizeof(arr2[0]) );
        
        vector<int> a2;
        a2 = shortestToChar("academyplus",'a');
        assert(areEqual(a2,b2,a2.size(),b2.size()) == true);
        
        int arr3[] = {0};
        vector<int> b3 (arr3, arr3 + sizeof(arr3) / sizeof(arr3[0]) );
        
        vector<int> a3;
        a3 = shortestToChar("a",'a');
        assert(areEqual(a3,b3,a3.size(),b3.size()) == true);
        
        int arr4[] = {0,0,0,0,0,0};
        vector<int> b4 (arr4, arr4 + sizeof(arr4) / sizeof(arr4[0]) );
        
        vector<int> a4;
        a4 = shortestToChar("aaaaaa",'a');
        assert(areEqual(a4,b4,a4.size(),b4.size()) == true);
        
        int arr5[] = {0};
        vector<int> b5 (arr5, arr5 + sizeof(arr5) / sizeof(arr5[0]) );
        
        vector<int> a5;
        a5 = shortestToChar("abcaaaa",'a');
        assert(areEqual(a5,b5,a5.size(),b5.size()) == false);
        
    }
    
};