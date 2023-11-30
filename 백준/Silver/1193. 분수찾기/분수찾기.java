import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = 0;
        int cnt = 0;
        int t = 100;
        for(int i=1; i<=1000000; i++) {
            if(t<=0) {
                t = t + cnt - 1;
                cnt -= 1;
                break;
            }
            t = n - k;
            k = k + i;
            cnt += 1;
        }
        int a = cnt - t + 1;
        int b = cnt + 1 - a;
        if(cnt%2 != 0)
            System.out.printf("%d/%d",a,b);
        else
            System.out.printf("%d/%d",b,a);
    }
}