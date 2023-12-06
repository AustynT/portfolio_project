from server import db


class BaseModel(db.Model):
    """
    Base model for database models.

    This class provides common methods for creating, retrieving, updating, and deleting database records.

    Attributes:
        __abstract__ (bool): Indicates that this class is an abstract base model.
    """

    __abstract__ = True

    @classmethod
    def create(cls, **kwargs) -> 'BaseModel':
        """
        Create a new instance of the model and save it to the database.

        Args:
            **kwargs: Keyword arguments representing the model's attributes.

        Returns:
            instance (BaseModel): The newly created instance.

        """
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    @classmethod
    def get(cls, model_id) -> 'BaseModel':
        """
        Retrieve a model instance from the database.

        Args:
            model_id: The ID of the model instance to retrieve.

        Returns:
            instance (BaseModel): The retrieved model instance.

        """
        instance = cls.query.get(model_id)
        return instance

    def update(self, **kwargs) -> None:
        """
        Update the attributes of the model instance and save the changes to the database.

        Args:
            **kwargs: Keyword arguments representing the attributes to update.

        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self) -> None:
        """
        Delete the model instance from the database.

        """
        db.session.delete(self)
        db.session.commit()
