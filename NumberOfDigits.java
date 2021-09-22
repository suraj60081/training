import java.util.Scanner;
public class NumberOfDigits {
	
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();
        int len=n.length();
        if (len%2==0){
            System.out.println(len+","+len*len);
        }
        else if (len%3==0)
        {
            System.out.println(len+","+len*len*len);
        }
        else if(len==1)
        {
            System.out.println("1");
        }
        else
        {
            int l1=len;
            while(!( len%2==0 || len%3 ==0))
            {
                len--;
            }
            if (len%2==0){
                System.out.println(l1+"["+len+"]"+","+len*len);
            }
            else if (len%3==0)
            {
                System.out.println(l1+"["+len+"]"+","+len*len*len);
            }
        }
	}
}


