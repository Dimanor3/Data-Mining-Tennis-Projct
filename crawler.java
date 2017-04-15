package webCrawler;

import java.util.*;

public class crawler {
	private static final int MAX_PAGES_TO_SEARCH = 3;
	private Set<String> pagesVisited = new HashSet<String>();
	private List<String> pagesToVisit = new LinkedList<String>();
	
	  public void search(String url, String searchWord)
	  {
	      while(this.pagesVisited.size() < MAX_PAGES_TO_SEARCH)
	      {
	          String currentUrl;
	          crawlerSearcher leg = new crawlerSearcher();
	          if(this.pagesToVisit.isEmpty())
	          {
	              currentUrl = url;
	              this.pagesVisited.add(url);
	          }
	          else
	          {
	              currentUrl = this.nextUrl();
	          }
	          leg.crawl(currentUrl); // Lots of stuff happening here. Look at the crawl method in
	                                 // crawlerSearcher
	          boolean success = leg.searchForWord(searchWord);
	          if(success)
	          {
	              System.out.println(String.format("**Success** Word %s found at %s", searchWord, currentUrl));
	              break;
	          }
	          this.pagesToVisit.addAll(leg.getLinks());
	      }
	      System.out.println("\n**Done** Visited " + this.pagesVisited.size() + " web page(s)");
	  }


	  /**
	   * Returns the next URL to visit (in the order that they were found). We also do a check to make
	   * sure this method doesn't return a URL that has already been visited.
	   * 
	   * @return
	   */
	  private String nextUrl()
	  {
	      String nextUrl;
	      do
	      {
	          nextUrl = this.pagesToVisit.remove(0);
	      } while(this.pagesVisited.contains(nextUrl));
	      this.pagesVisited.add(nextUrl);
	      return nextUrl;
	  }
}
