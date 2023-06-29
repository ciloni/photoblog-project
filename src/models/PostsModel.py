from database import db, metadata_obj
import datetime

class Post(db.Model):
    __tablename__ = 'posts'
    metadata_obj
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_description = db.Column(db.String(500))
    post_media_type = db.Column(db.String(25))
    post_media_filename = db.Column(db.String(100))
    post_media_path = db.Column(db.String(255))
    post_date_created = db.Column(db.DateTime())

    def __repr__(self):
        return f'<Id "{self.id}">'

    def __init__(self, user_id, post_description, post_media_type, post_media_filename, post_media_path):
        self.user_id = user_id
        self.post_description = post_description
        self.post_media_type = post_media_type
        self.post_media_filename = post_media_filename
        self.post_media_path = post_media_path
        self.post_date_created = datetime.datetime.now()

    # código util para outras implementacoes
    # def as_dict(self):
    #    return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'post_description': self.post_description,
            'post_media_type': self.post_media_type,
            'post_media_filename': self.post_media_filename,
            'post_media_path': self.post_media_path,
            'post_date_created': self.post_date_created
        }