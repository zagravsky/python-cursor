import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.io.IOException;

public class Test {

    public String[] getMessage(String cases) throws IOException {
        Document doc;
        doc = Jsoup.connect("https://www.rozklad.onaft.edu.ua/guest_n.php?view=g&id=195").get();
        Elements lesson1;
        Elements lesson2;
        Elements lesson3;
        Elements lesson4;
        String[] schedule = new String[0];
        switch (cases) {

            case "/Понедельник":
                lesson1=doc.getElementsByAttributeValue("title", "Понеділок 1-а пара");
                lesson2=doc.getElementsByAttributeValue("title", "Понеділок 2-а пара");
                lesson3=doc.getElementsByAttributeValue("title", "Понеділок 3-а пара");
                lesson4=doc.getElementsByAttributeValue("title", "Понеділок 4-а пара");
                schedule[0]=lesson1.text();
                schedule[1]=lesson2.text();
                schedule[2]=lesson3.text();
                schedule[3]=lesson4.text();
                break;

            case "/Вторник":
                lesson1=doc.getElementsByAttributeValue("title", "Вівторок 1-а пара");
                lesson2=doc.getElementsByAttributeValue("title", "Вівторок 2-а пара");
                lesson3=doc.getElementsByAttributeValue("title", "Вівторок 3-а пара");
                lesson4=doc.getElementsByAttributeValue("title", "Вівторок 4-а пара");
                schedule[0]=lesson1.text();
                schedule[1]=lesson2.text();
                schedule[2]=lesson3.text();
                schedule[3]=lesson4.text();
                break;

            case "/Среда":
                lesson1=doc.getElementsByAttributeValue("title", "Середа 1-а пара");
                lesson2=doc.getElementsByAttributeValue("title", "Середа 2-а пара");
                lesson3=doc.getElementsByAttributeValue("title", "Середа 3-а пара");
                lesson4=doc.getElementsByAttributeValue("title", "Середа 4-а пара");
                schedule[0]=lesson1.text();
                schedule[1]=lesson2.text();
                schedule[2]=lesson3.text();
                schedule[3]=lesson4.text();
                break;

            case "/Четверг":
                lesson1=doc.getElementsByAttributeValue("title", "Четвер 1-а пара");
                lesson2=doc.getElementsByAttributeValue("title", "Четвер 2-а пара");
                lesson3=doc.getElementsByAttributeValue("title", "Четвер 3-а пара");
                lesson4=doc.getElementsByAttributeValue("title", "Четвер 4-а пара");
                schedule[0]=lesson1.text();
                schedule[1]=lesson2.text();
                schedule[2]=lesson3.text();
                schedule[3]=lesson4.text();
                break;

            case "/Пятница":
                lesson1=doc.getElementsByAttributeValue("title", "П`ятниця 1-а пара");
                lesson2=doc.getElementsByAttributeValue("title", "П`ятниця 2-а пара");
                lesson3=doc.getElementsByAttributeValue("title", "П`ятниця 3-а пара");
                lesson4=doc.getElementsByAttributeValue("title", "П`ятниця 4-а пара");
                schedule[0]=lesson1.text();
                schedule[1]=lesson2.text();
                schedule[2]=lesson3.text();
                schedule[3]=lesson4.text();
                break;

            case "/Суббота":
                lesson1=doc.getElementsByAttributeValue("title", "Понеділок 1-а пара");
                lesson2=doc.getElementsByAttributeValue("title", "Понеділок 2-а пара");
                lesson3=doc.getElementsByAttributeValue("title", "Понеділок 3-а пара");
                lesson4=doc.getElementsByAttributeValue("title", "Понеділок 4-а пара");
                schedule[0]=lesson1.text();
                schedule[1]=lesson2.text();
                schedule[2]=lesson3.text();
                schedule[3]=lesson4.text();
                break;

            default:
                System.out.println("Введите день недели, плиз...");


        }
        return schedule;
    }



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
