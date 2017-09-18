import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.io.IOException;

public class Test {

//    public String[] getMessage(String cases) throws IOException {
//        Document doc;
//        doc = Jsoup.connect("https://www.rozklad.onaft.edu.ua/guest_n.php?view=g&id=195").get();
//        Elements lessons;
//        String[] schedule = new String[0];
//        switch (cases) {
//            case "/Понедельник":
//                lessons=doc.getElementsByAttributeValue("title", "Понеділок 1-а пара");
//                schedule[0]=lessons.text();
//                break;
//            case "/Вторник":
//                lessons=doc.getElementsByAttributeValue("title", "Вівторок 1-а пара");
//                schedule = lessons.text();
//                break;
//            case "/Среда":
//                lessons=doc.getElementsByAttributeValue("title", "Середа 1-а пара");
//                schedule = lessons.text();
//                break;
//            case "/Четверг":
//                lessons=doc.getElementsByAttributeValue("title", "Четвер 1-а пара");
//                schedule = lessons.text();
//                break;
//            case "/Пятница":
//                lessons=doc.getElementsByAttributeValue("title", "П'ятниця 1-а пара");
//                schedule = lessons.text();
//                break;
//            case "/Суббота":
//                lessons=doc.getElementsByAttributeValue("title", "Субота 1-а пара");
//                schedule += lessons.text();
//                break;
//            default:
//                System.out.println("Введите день недели, плиз...");
//
//
//        }
//        return schedule;
//    }



    public void parseHtml() {

        Document doc;
        Elements days= new Elements();
        Elements subjects= new Elements();
        Elements titles = new Elements();


        //надо брать все элементы из <tbody> пока они есть...
        // split через массив строк из ВСЕЙ недели не катит....

        try {
            doc = Jsoup.connect("https://www.rozklad.onaft.edu.ua/guest_n.php?view=g&id=195").get();
            days = doc.getElementsByAttributeValue("class","lesson");
//            subjects = doc.getElementsByAttributeValue("class" , "predm");
//            titles = doc.getElementsByAttributeValue("title", "Понеділок 1-а пара");

        } catch (IOException e) {
            e.getMessage();
        }

        System.out.println("Lessons : " + days.text());
        System.out.println("Subjects : " + titles.text());

    }

    public static void main(String[] args) {
        Test test = new Test();
        test.parseHtml();
    }
}
