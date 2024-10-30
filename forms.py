from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    """Форма авторизации"""
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    """Форма регистрации"""
    user_name = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email адрес', validators=[DataRequired(), Email()])
    password_hash = PasswordField('Пароль', validators=[DataRequired()])
    confirm = PasswordField('Повторите пароль', validators=[DataRequired()])
    accept_tos = BooleanField('Я принимаю лицензионное соглашение',
                              validators=[DataRequired()])
    submit = SubmitField('Создать учетную запись')


class AddBookForm(FlaskForm):
    """Форма добавления фильма"""
    name = StringField('Название Фильма', validators=[DataRequired()])
    author = StringField('Режиссер', validators=[DataRequired()])
    year = IntegerField('Год', validators=[DataRequired()])
    pages = IntegerField('Длительность', validators=[DataRequired()])
    pictures = FileField('Обложка', validators=[DataRequired()])
    bio = StringField(u'Описание', widget=TextArea(), validators=[DataRequired()])
    stock = IntegerField('Прокат', validators=[DataRequired()])
    price = IntegerField('Цена (руб)', validators=[DataRequired()])
    submit = SubmitField('Добавить фильм')


class AddCommentForm(FlaskForm):
    """Форма комментария фильма"""
    name = StringField('Название рецензии', validators=[DataRequired()])
    date = StringField('Дата (дд-мм-гг)', validators=[DataRequired()])
    text = StringField(u'Рецензия', widget=TextArea(),
                       validators=[DataRequired()])
    submit = SubmitField('Добавить рецензию')


class AddAuthorForm(FlaskForm):
    """Форма автора"""
    name = StringField('Имя режиссера', validators=[DataRequired()])
    picture = FileField('Фотография', validators=[DataRequired()])
    bio = StringField('Биография', widget=TextArea(),
                      validators=[DataRequired()])
    submit = SubmitField('Добавить режиссера')


class SearchForm(FlaskForm):
    """Форма поиска"""
    search = StringField('Название фильма, ИФ режиссера',
                         widget=TextArea(),
                         validators=[DataRequired(),
                                     Length(min=4, max=250)])
    submit = SubmitField('Поиск')
