from sqlalchemy.orm import Session


def create_record(db: Session, model, data):
    obj = model(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj



def get_all(db: Session, model):
    return db.query(model).all()



def get_by_id(db: Session, model, id_field, id_value):
    return db.query(model).filter(id_field == id_value).first()



def delete_record(db: Session, obj):
    db.delete(obj)
    db.commit()