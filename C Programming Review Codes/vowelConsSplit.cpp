// Online C compiler to run C program online
#include <stdio.h>

void concat(){
char str1[20] = "Hello ";
char str2[] = "World!";

// Concatenate str2 to str1 (result is stored in str1)
//strcat(str1, str2);

// Print str1
printf("\n%s", str1);    
}

int main() {
    // Write C code here
    /*
    closed path calculations
    0, 4, 6, 9 = 1
    8 = 2
    
    */
    int num = 8450469;
    char numChar[20];
    int closedPath = 0;
    sprintf(numChar, "%d", num);
    
    for (int i=0; numChar[i] != '\0'; i++){
        char x = numChar[i];
        if (x == '0' || x == '4' || x == '6'|| x == '9' ){
            closedPath +=1;
        }
        if (x=='8'){
            closedPath +=2;
        }
    }
    printf("Closed path: %d", closedPath);
    
    concat();
    return 0;
}


