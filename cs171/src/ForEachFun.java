import java.util.ArrayList;
import java.util.Iterator;

public class ForEachFun {

    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("one");
        list.add("two");
        list.add("three");

        for (String s : list) {
            System.out.println(s);
        }

        System.out.println("============");

        // What happens behind the scenes
        // Our stack has to implement the iterable interface
        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            String s = iterator.next();
            System.out.println(s);
        }
    }
}
