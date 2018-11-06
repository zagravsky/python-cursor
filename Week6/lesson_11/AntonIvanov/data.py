import datetime
today = datetime.date(2018, 10, 23)
rows = [
    {
        "item": "Огурец",
        "quantity": 6,
        "unit": "шт.",
        "price": 9
    },
    {
        "item": "Груша",
        "quantity": 2,
        "unit": "кг",
        "price": 21
    },
    {
        "item": "Яблоко",
        "quantity": 3,
        "unit": "кг",
        "price": 17
    },
    {
        "item": "Соковыжималка",
        "quantity": 1,
        "unit": "шт.",
        "price": 1024
    },
    {
        "item": "Яйцо",
        "quantity": 10,
        "unit": "шт.",
        "price": 7
    },
    {
        "item": "Молоко",
        "quantity": 5,
        "unit": "л",
        "price": 32
    }
]
articles = [
    {
        "title_heading": "TITLE HEADING",
        "title_description": "Title description",
        "text": """Sunt in culpa qui officia deserunt mollit anim id 
                est laborum consectetur adipiscing elit, sed do eiusmod
                tempor incididunt ut labore et dolore magna aliqua. Ut enim 
                ad minim veniam, quis nostrud exercitation ullamco."""
    },
    {
        "title_heading": "TITLE HEADING1",
        "title_description": "Title description1",
        "text": """Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Perferendis quasi ducimus architecto sed sint consequatur beatae ea harum. 
                Atque, ducimus nesciunt libero quam impedit tempora id quis at expedita eius."""
    }
]

links = [
    {
        "href": "render-book.html",
        "caption": "Book",
        "name": "book"
    },
    {
        "href": "render-articles.html",
        "caption": "Articles",
        "name": "articles"
    },
    {
        "href": "render-login.html",
        "caption": "Login",
        "name": "login"
    },
    {
        "href": "render-task3.html",
        "caption": "Task3",
        "name": "task3"
    }
]
