from app import db
from app.models import User, Post, Comments

def add_dummy_data():
    # Dummy data
    users = [
        User(id=1, username='sebagabones', email='seb@thinkmad.com', password_hash='scrypt:32768:8:1$KeaQt5QHjdKHUjK0$55b686c82de9b076b7aaf001e50d78b5afe3b984cd68f0b69ed88f2b0635cf8018fbf2d35661da2db496a10e5ded22329cb32030a25b0639d3abba1551a39a38', ThinkPads=8, pronouns='They/Them')
    ]

    db.session.add_all(users)

    db.session.commit()


if __name__ == "__main__":
    add_dummy_data()