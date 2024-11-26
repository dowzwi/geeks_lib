from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class books (models.Model):
    GENRE_CHOICE = (
        ('Манга','Манга'),
        ('Комедия','Комедия'),
        ('Сказка','Сказка')
    )
    image = models.ImageField(upload_to = 'books/', verbose_name= 'Загрузите обложку книги')
    title = models.CharField(max_length =100, verbose_name='Укажите название книги')
    price = models.FloatField(verbose_name='Укажите цену')
    release_date = models.DateField(verbose_name='Укажите дату написания')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, default='Комедия', verbose_name='Укажите жанр книги')
    author = models.CharField(max_length=100, verbose_name='Укажите имя автора')
    audio = models.URLField(verbose_name='Вставьте ссылку на аудио книгу с YouTube')
    email = models.EmailField(verbose_name='Укажите почту автора')
    available_copies = models.PositiveIntegerField(default=0, verbose_name="Количество доступных экземпляров", null=True)

    def average_rating(self):
        reviews = self.review_books.all()
        if reviews:
            return sum(review.mark for review in reviews) / reviews.count()
        return None

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title}-{self.price}$'

class ReviewBook(models.Model):
    review_books = models.ForeignKey(books, on_delete=models.CASCADE,
                                     related_name='review_books')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(verbose_name='Оставьте отзыв книге!')
    mark = models.PositiveIntegerField(verbose_name='Укажите оценку от 1 до 5',
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.review_books}-{self.created_at}'
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
