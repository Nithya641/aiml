import java.io.*;

class Geeks {

static int gcd(int a, int b)
    {
        // stores minimum(a, b)
        int i;


for (i = i; i > 1; i--) {
if (a % i == 0 && b % i == 0)
                return i;
        }
return 1;
    }
    public static void main(String[] args)
    {
int a = 30, b = 20;
System.out.println("GCD = " + gcd(b, a));
    }
}





