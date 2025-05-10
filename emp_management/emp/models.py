from django.db import models

# Create your models here.

# create 3 table like dept,emp,skill 


skill= [
    ('T','Technical'),
    ('NT','Non-Technical'),
]

s_level = [
    ('B','Beginner'),
    ('I','Intermediate'),
    ('E','Expert'),
]

class Skill(models.Model):
    s_name=models.CharField(max_length=255,blank=True,default='',choices=skill)
    description=models.TextField(blank=True,default='')
    skill_level = models.CharField(max_length=100,choices=s_level)

d_location = [
    ('P','Pune'),
    ('M','Mumbai'),
    ('H','Hydrabad'),
    ('CSN','charapati Sambhaji Nager'),
]

class Dept(models.Model):
    name=models.CharField(max_length=255,blank=True,default='')
    location=models.CharField(max_length=500,choices=d_location)

choice=[
    ('M','Male'),
    ('F','Female'),
    ('O','Others'),
]

class Emp(models.Model):
    name=models.CharField(max_length=255,blank=True,default='')
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=10,choices=choice,blank=True,null=True)
    description=models.TextField(blank=True,default='')
    sal=models.DecimalField(max_digits=15,decimal_places=2,default='0')
    joining_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    department=models.ForeignKey(Dept,on_delete=models.CASCADE)
    skills=models.ManyToManyField(Skill)



# mysql formate 

# CREATE TABLE skill (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     s_name VARCHAR(255) DEFAULT '' CHECK (s_name IN ('T', 'NT')),
#     description LONGTEXT DEFAULT '',
#     skill_level VARCHAR(100) NOT NULL CHECK (skill_level IN ('B', 'I', 'E'))
# );


# CREATE TABLE dept (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) DEFAULT '',
#     location VARCHAR(500) NOT NULL CHECK (location IN ('P', 'M', 'H', 'CSN'))
# );


# CREATE TABLE emp (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) DEFAULT '',
#     email VARCHAR(254) NOT NULL UNIQUE,
#     gender VARCHAR(10) DEFAULT NULL CHECK (gender IN ('M', 'F', 'O')),
#     description LONGTEXT DEFAULT '',
#     sal DECIMAL(15, 2) DEFAULT 0,
#     joining_date DATETIME DEFAULT CURRENT_TIMESTAMP,
#     department_id INT NOT NULL,
#     FOREIGN KEY (department_id) REFERENCES dept(id)
# );


# CREATE TABLE emp_skills (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     emp_id INT NOT NULL,
#     skill_id INT NOT NULL,
#     FOREIGN KEY (emp_id) REFERENCES emp(id),
#     FOREIGN KEY (skill_id) REFERENCES skill(id),
#     UNIQUE(emp_id, skill_id)  -- No duplicate skill per employee
# );

