public class ExceptionalFun {

    public static int methodThatCrashes() throws RuntimeException {
        int x = (int) (Math.random() * 100);
        if (x == 0)
            throw new RuntimeException("Crash and burn!");
        else return x;
    }

    public static void main(String[] args) {
        try {
            int z = methodThatCrashes();
            System.out.println(z);
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }
}
