import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class day1_es2 {
    public static void main(String args[]){
        try {
            BufferedReader file = new BufferedReader(new FileReader("numberDay1.txt"));
            String number = "";
            int numberI = 0;
            int A = 0, B = 0, C = 0, D = 0;
            int count = 0, i = 0;
            int increase = 0;
            int a[] = new int[6];
            /*System.out.println(number);
            System.out.println(numberI);*/
            int oldNumber = numberI, counter = 0;

            while(number != null){
                //Creation of the array with 6 number
                while(count < 6){
                    number = file.readLine();
                    if(number != null) {
                        numberI = Integer.parseInt(number);
                        a[count] = numberI;
                    }
                    count++;
                }
                count = 0;

                //Print the array for a check
                for(int k = 0; k < 6; k++){
                    System.out.print(a[k] + " ");
                }
                System.out.println();

                //first sequence
                for(i = 0; i < 3; i++){
                    A = A + a[i];
                }
                if(A > D && D != 0)
                    increase++;
                D = 0;
                System.out.println("A  " + A);

                //second sequence
                for(i = 1; i < 4; i++){
                    B = B + a[i];
                }
                if(B > A)
                    increase++;
                System.out.println("B  " + B);

                //third sequence
                for(i = 2; i < 5; i++){
                    C = C + a[i];
                }
                if(C > B)
                    increase ++;
                System.out.println("C  " + C);

                //fourth sequence
                for(i = 3; i < 6; i++){
                    D = D + a[i];
                }
                if(D > C)
                    increase++;
                System.out.println("D  " + D);


                A = 0;
                B = 0;
                C = 0;

                //Creation of the next array with the last 2 value as the first 2 value
                a[0] = a[4];
                a[1] = a[5];
                count = 2;
                System.out.println("");

            }

            file.close();
            System.out.println("Increase: " + increase);

        } catch (IOException e) {
            System.out.println(e);
        }

    }
}
