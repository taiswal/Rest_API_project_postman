from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    cat_name=models.CharField(max_length=255)


class Book(models.Model):
    book_name=models.CharField(max_length=255)
    book_description=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)


# '''

# CREATE TABLE Author (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL
# );

# CREATE TABLE Category (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     cat_name VARCHAR(255) NOT NULL
# );

# CREATE TABLE Book (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     book_name VARCHAR(255) NOT NULL,
#     book_description TEXT NOT NULL,
#     author_id INT NOT NULL,
#     FOREIGN KEY (author_id) REFERENCES Author(id) ON DELETE CASCADE
# );

# CREATE TABLE Book_Category (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     book_id INT NOT NULL,
#     category_id INT NOT NULL,
#     FOREIGN KEY (book_id) REFERENCES Book(id) ON DELETE CASCADE,
#     FOREIGN KEY (category_id) REFERENCES Category(id) ON DELETE CASCADE,
#     UNIQUE (book_id, category_id)  -- Prevents duplicate entries
# );


# '''