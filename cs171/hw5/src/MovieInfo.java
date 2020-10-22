class MovieInfo{
    public String shortName;   //short or simplified name, e.g., Tom Hanks.
    public String fullName;    //full name, e.g., Hanks, Thomas III.
    public int ID;             //integer ID.

    public MovieInfo(int id, String shortName, String fullName) {
       this.ID = id;
       this.shortName = shortName;
       this.fullName = fullName;
    }
}