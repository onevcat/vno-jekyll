//test.c
#include <studio.h>
int main(void)
{
  float c;
  double d;

  c = 3.14;
  d = 3.14159263;

  printf("圆周率是：%.2f\n", c);
  printf("圆周率是：%11.9\n", d);

  return 0;
}
