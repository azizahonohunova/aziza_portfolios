from flask import Flask, render_template

app = Flask(__name__)

# Данные для портфолио
portfolio = {
    "name": "Азиза",
    "bio": "Меня зовут Азиза, мне 25 лет, и я живу в Москве. Я обладаю высшим образованием в области прикладной математики, которое получила в Худжанском Государственном Университете. Я увлечена программированием и постоянно совершенствую свои навыки в различных языках программирования.",
    "skills": ["Python", "Visual Basic/QBasic", "C, C++, C#", "JavaScript", "MySQL", "HTML/CSS", "Go"],
    "projects": 
        "К сожалению, у меня нет официального опыта работы, так как после университета я вышла замуж и посвятила себя семейной жизни. Однако, я готова и стремлюсь начать свою профессиональную карьеру и применить свои знания и навыки на практике.",
    "education": [
        {"institution": "Худжанский Государственный Университет", "degree": "Прикладная математика", "years": "2016-2021"}
    ],
    "experience": [
        {}
    ],
    "contacts": {
        "Email" : "azizahonohunova@gmail.com",
        "GitHub" : "https://github.com/azizahonohunova"
    },
    "myPic": "./images/my_pic.jpg"
}

@app.route('/')
def index():
    return render_template('index.html', portfolio=portfolio)

@app.route('/projects')
def projects():
    return render_template('projects.html', portfolio=portfolio)

@app.route('/contact')
def contact():
    return render_template('contact.html', portfolio=portfolio)

if __name__ == '__main__':
    app.run(debug=True)
