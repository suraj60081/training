import java.util.Scanner;
public class SquareAndMultiple {

private static void check(int a, int b)
{
	if(b/a==0 && b%a==0) System.out.println(b+ " is square of "+ a+" \n"+b+" is multiple of "+a );
    else if(b/a==a) System.out.println(b+" is square of "+a);
	else if(b%a==0) System.out.println(b+" is multiple of "+a);
	else System.out.println("no condition matched");
}
public static void main(String[] args)
{
int num1, num2;
Scanner sc = new Scanner(System.in);
num1 = sc.nextInt();
num2 = sc.nextInt();

check(num1,num2);

}
}
