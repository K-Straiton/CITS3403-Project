from app import db
from app.models import User, Post, Comments

def add_dummy_data():	#Create dummy/test data
    # Dummy data
    users = [
        User(id=1, username='sebagabones', email='seb@thinkmad.com', password_hash='scrypt:32768:8:1$vVPhlv7T4ExbWSTL$b52adb1d150a46a32d79a2ce88073d756ca48fba8e978de6791f37e65f09691dd6c745e1caa60ca10b10ace09cbd883f72e6bedd9396398830340d48ab789b03', ThinkPads=6, pronouns='They/Them'),
        User(id=2, username='quichelorraine', email='lauren@thinkmad.com', password_hash='scrypt:32768:8:1$uwUTXovjcggazM2G$32e48b3cdb3e24deb2e7beac9195645654e06d2e6e6fcf60dc8dc603a2659bf110898fe4285e12700ee32c9dce3b40612058d8c3d7e62a4cfde9a9ca77f16615', ThinkPads=3, pronouns='She/Her'),
        User(id=3, username='kirsty', email='kirsty@thinkmad.com', password_hash='scrypt:32768:8:1$KcaGiwMOyZAfAlpB$45a185d403cbc9486971e5522f071952a033b1e5834798b56bc100c2c4f17ed10cb5765af4990ba1f107ccc76bcb31cfda1f02edcf1dc74c73660dfe0f70270d', ThinkPads=3, pronouns='They/Them'),
        User(id=4, username='sersangy', email='sersang@thinkmad.com', password_hash='scrypt:32768:8:1$4gfZkeRAEHOn76vs$8345a05fd6bb9a8f5bf2b8bfe1c86cf90bf36530f8c7499608ec0bf89f8f088666936e745ca7ddad74a815ea9f09ff095fa959f67e64d30d9c752282b1f920d2', ThinkPads=1, pronouns='She/Her')
    ]

    posts = [
        Post(id=1, title="Just bought my first thinkpad and now looking for more", body="I just bought my first thinkpad and have been having a great time with it. Now I'm looking for more but need advice on what models I should get.", user_id=4),
        Post(id=2, title="X220 keeps overheating", body="I have an X220 and currently the CPU reaches 80 degress while doing almost nothing. Does anyone have any advice?", user_id=2),
        Post(id=3, title="X13 battery life is terrible", body="My new ThinkPad X13 Gen 2 AMD is only one year old however ever since I got it, its battery has only lasted a maximum of two hours. I am not sure if it's something to do with settings or if there is something wrong with the battery itself. I have run Windows, Ubuntu, and Arch on it but the result is the same. Has anyone else had the same experience with this model?", user_id=3)
    ]

    comments = [
        Comments(id=1, post_id=3, body="You should look into getting an x270 - I have one and the battery life on it was amazing", user_id=1),
        Comments(id=2, post_id=3, body="I can attest to that - I borrowed their x270 for ages and fell in love with it's battery life", user_id=2)
    ]
    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.add_all(comments)

    db.session.commit()


if __name__ == "__main__":
    add_dummy_data()
