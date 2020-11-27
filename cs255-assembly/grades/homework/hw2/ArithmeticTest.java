package hw2;

import org.junit.jupiter.api.Assertions;

import java.util.ArrayList;
import java.util.Collections;

public class ArithmeticTest {

    public static void main(String[] args) {
        testOperations();
        testParsing();
        testConversions();
    }

    private static void testOperations() {
        String five = String.join("", Collections.nCopies(29, "0")) + "101";
        String seventeen = String.join("", Collections.nCopies(27, "0")) + "10001";
        String four = String.join("", Collections.nCopies(24, "0")) + "00000100";
        String three = String.join("", Collections.nCopies(24, "0")) + "00000011";
        String one = String.join("", Collections.nCopies(24, "0")) + "00000001";
        String fifteen = String.join("", Collections.nCopies(28, "0")) + "1111";
        String negThree = String.join("", Collections.nCopies(30, "1")) + "01";
        String two = String.join("", Collections.nCopies(30, "0")) + "10";

        ArrayList<String> divideResult = new ArrayList<>();
        divideResult.add(String.join("", Collections.nCopies(30, "0")) + "11");
        divideResult.add(String.join("", Collections.nCopies(30, "0")) + "10");

        Assertions.assertEquals(four, Arithmetic.add(three, one));
        Assertions.assertEquals(fifteen, Arithmetic.multiply(three, five));
        Assertions.assertEquals(negThree, Arithmetic.subtract(two, five));
        Assertions.assertEquals(divideResult, Arithmetic.divide(seventeen, five));
    }

    private static void testParsing() {
        Assertions.assertEquals(252552, Arithmetic.parseInt("252552"));
        Assertions.assertEquals(-35676, Arithmetic.parseInt("-35676"));
    }

    private static void testConversions() {
        Assertions.assertEquals(String.join("", Collections.nCopies(30, "0"))
                + "11", Arithmetic.toBinary("3"));
        Assertions.assertEquals(String.join("", Collections.nCopies(30, "1"))
                        + "00",
                Arithmetic.getTwosComplement(String.join("", Collections.nCopies(29, "0")) + "100"));

        String hexString1 = "00 00 00 21";  //33
        int dec1 = 33;  //33
        String binString1 = String.join("", Collections.nCopies(26, "0")) + "100001";
        Assertions.assertEquals(hexString1, Arithmetic.toHex(binString1));
        Assertions.assertEquals(dec1, Arithmetic.toDecimal(binString1));
    }
}