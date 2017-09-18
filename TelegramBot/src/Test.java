import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

public class Test {

    public void parseHtml() {

        Document doc;
        String title="";
        String day = "";

        String subj="";
        String teacher="";
        String auditory="";
        Elements days;
        Elements teachers;
        Elements auditories;
        String [] week=null;
        String allDay="";


        //надо брать все элементы из <tbody> пока они есть...
        // split через массив строк из ВСЕЙ недели не катит....

        try {
            doc = Jsoup.connect("https://www.rozklad.onaft.edu.ua/guest_n.php?view=g&id=195").get();
            days = doc.getElementsByAttributeValue("class","entry-title");





            day= days.tagName("h1").first().text();


             title= doc.title();


        } catch (IOException e) {
            e.getMessage();
        }
        System.out.println("A title is : " + title);
        System.out.println("A current day is : " + allDay);

    }

    public static void main(String[] args) {
        Test test = new Test();
        test.parseHtml();
    }
}
