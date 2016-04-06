/*************************************************************************
    > File Name: test_ctypes.cpp
  > Author: tuskguo
  > Mail: tuskguo@tencent.com
  > Created Time: 2016/4/6 11:00:33
 ************************************************************************/

#include <stdio.h>

#include <iostream>
#include <string>

using namespace std;

extern "C" {

void display(string s)
{
    printf("display\n");
    //cout << "cout: " << s << endl;
    printf("s address: %x\n", &s);
    printf("s.c_str address: %x\n", s.c_str());
    printf("printf: %s\n", s.c_str());
}

void display_sz(const char *s)
{
    string str(s);
    cout << "cout: " << str << endl;
    printf("printf: %s\n", s);
    printf("printf: %s\n", str.c_str());
}

}
