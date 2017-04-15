package webCrawler;

public class crawlerTest {
    public static void main(String[] args)
    {
        crawler spider = new crawler();
        spider.search("http://www.itftennis.com/juniors/players/player-search.aspx", "More");
    }
}
