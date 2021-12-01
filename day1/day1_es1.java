import java.io.*;

public class day1_es1 {
    public static void main(String args[]){
        try {
            BufferedReader file = new BufferedReader(new FileReader("numberDay1.txt"));
            String number = file.readLine();
            int numberI = Integer.parseInt(number);
            //System.out.println(number);
            //System.out.println(numberI);
            int oldNumber = numberI, counter = 0;

            while(number != null){
                number = file.readLine();
                if(number != null)
                    numberI = Integer.parseInt(number);
                //System.out.println(numberI);
                if(numberI > oldNumber)
                    counter ++;
                oldNumber = numberI;
            }
            file.close();
            System.out.println("counter: " + counter);

        } catch (IOException e) {
            System.out.println(e);
        }


    }
}
