import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.telegram.telegrambots.ApiContextInitializer;
import org.telegram.telegrambots.TelegramBotsApi;
import org.telegram.telegrambots.api.methods.send.SendMessage;
import org.telegram.telegrambots.api.objects.Message;
import org.telegram.telegrambots.api.objects.Update;
import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.exceptions.TelegramApiException;

import org.w3c.dom.NodeList;


import java.io.IOException;


public class TelegramBot extends TelegramLongPollingBot {


    public TelegramBot parseHtml(){

        Document doc;
        String title="";
        try{
            doc = Jsoup.connect("https://www.rozklad.onaft.edu.ua/guest_n.php?view=g&id=195").get();
            doc.body().getAllElements().eachText();
        }catch (IOException e){
            e.getMessage();
        }
        return null;
    }

    @Override
    public void onUpdateReceived(Update update) {
        Message message = update.getMessage();
        if (message != null && message.hasText()){
            if(message.getText().equals("/help")){
                sendMsg (message,"Введите setGroup номер_группы для выбора своей группы");

            }
            else{
                sendMsg(message,"я тестовый робот");
            }
        }

    }

    private void sendMsg(Message message, String s) {
        SendMessage sendMessage = new SendMessage();
//        sendMessage.enableMarkdown(true); //цитирование сообщения
        sendMessage.setChatId(message.getChatId().toString());
//        sendMessage.setReplyToMessageId(message.getMessageId());//цитирование сообщения
        sendMessage.setText(s);
        try {
            sendMessage(sendMessage);
        }catch (TelegramApiException e){
            e.printStackTrace();
        }
    }

    @Override
    public String getBotUsername() {
        return "Onaftshedule_bot";
    }

    @Override
    public String getBotToken() {
        return "420111054:AAHpmTBkA6UlxvLAhh6pn82QNhl3Dw4IEGs";
    }
}
