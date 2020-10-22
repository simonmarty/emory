// SUBMITTED BY: Bhargav Annigeri, Simon Marty, Alex Welsh
// Not currently in use

public class MainAddUpdate {
	private static Network network = new Network();
	
	public static void main(String[] args) {
		network.add("BBB", "Stuff", "eyyyy1", null, null);
		network.add("Simon", "Physics", "simonfun1", null, null);
		network.add("Alex", "Chem", "alexwelsh1", null, null);

		network.getUser("BBB");
	}
}
