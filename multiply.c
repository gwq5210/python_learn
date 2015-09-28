/*************************************************************************
	> File Name: multiply.c
	> Author: gwq
	> Mail: gwq5210@qq.com 
	> Created Time: 2015年09月29日 星期二 00时56分37秒
 ************************************************************************/

/*
 * gcc -c -fPIC multiply.c
 * gcc -shared multiply.o -o multiply.so
 * 或者
 * gcc multiply.c -fPIC -shared -o multiply.so 
 */
int multiply(int a, int b)
{
	return a * b;
}
