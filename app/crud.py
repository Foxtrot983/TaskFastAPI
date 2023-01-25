from sqlalchemy.orm import Session

import models, schemas


def get_data(db: Session):
    return db.query(models.Data).all()


def create_data(db: Session, data: schemas.Data):
    data = models.Data(data=data)
    db.add(data)
    db.commit()
    return data