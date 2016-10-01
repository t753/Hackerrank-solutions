/*
Step 1 : Find the index of the smallest character call it idx1;

Step 2 : Find the index of the second smallest character call it idx2;

Step 3 : Find the index of the smallest freq. character call it midx;

Step 4 :
Place one copy of the character with smallest frequency at first place.

Step 5 :

If the character of smallest freq. also occurs earliest with
freq. >= 2 then place two copies of this character at beginning and then
place rest of characters as it is until you hit midx character,
once midx character is hit make interleaving of midx and next non-zero freq.
characters one by one, thus maintaining the lexicographical smallest property
and utilizing all characters.
Corner Case : When there is only one character, then idx2==-1
and job is done.

Else
If the character of least freq. is not the one which occurs earliest
then place all the copies of other characters one by one after first.

*/
# include<iostream>
# include<climits>
using namespace std;

int main(){
int *lst = new int[26]();
int g = 0,idx1=-1,idx2=-1,mval = INT_MAX,midx;
for(int i=0;i<26;++i){
    cin>>lst[i],g+=lst[i];
    // find the second character after first one
    if(idx1 != -1 && idx2 == -1 && lst[i])idx2 = i;
    // find the first character with non-zero freq.
    if(idx1 == -1 && lst[i])idx1 = i;
    // find character with min. freq.
    if(lst[i] && lst[i]<mval)mval=lst[i],midx=i;
}

char *str = new char[g+1];
int k=0;
// Put minimum freq. character at first place
--lst[midx];
str[k++]=midx+97;
// if the min. freq. character is the earliest occurring character
// and it is not the only character and it occurs more than once
if(idx1 == midx && idx2!=-1 && lst[idx1]){
    // make second character of string same as first one
    str[k++]=midx+97,--lst[midx];

    // make interleaving of characters
    int m=idx2; // the character that occurs just after first character
    while(lst[midx]>0){
        while(m<26 && !lst[m])++m;
        if(m>25)break;

        // till the time interleaving can be done do that
        while(lst[midx]-- && lst[m]--)
            str[k++]=m+97,str[k++]=midx+97;
    }
    // if you came out because of the other character's emptiness
   // while(lst[midx]--)str[k++]=midx+97;
    for(int i=m;i<26;++i)
        while(lst[i]--)
        str[k++]=i+97;
}
else    // the earliest occurring character is not the one with least freq.
for(int i=0;i<26;++i)
    while(lst[i]--)
    str[k++]=i+97;

str[k] = 0;
cout<<str;
return 0;
}

