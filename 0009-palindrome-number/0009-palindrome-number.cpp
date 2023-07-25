class Solution {
public:
    bool isPalindrome(int x) {
        
vector<int> v;
bool found=true;
while(x>0){

v.push_back(x%10);
x=x/10;

}
int i=0;
int j=v.size()-1;

while(i<j){

if(v[i]!=v[j]){
    found=false;
    break;
}
i++;
j--;

}
if(x<0) found=false;
return found;


    }
};