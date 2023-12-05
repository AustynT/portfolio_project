from server import db


class TypeModel(db.Model):
    """
    Represents a type in the system.

    Attributes:
        type_id (int): The unique identifier for the type.
        type_name (str): The name of the type.
        projects (list): The projects associated with this type.
        hobbies (list): The hobbies associated with this type.
    """
    __tablename__ = 'types'
    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), nullable=False, unique=True)

    # Relationships
    projects = db.relationship('Project', backref='type')
    hobbies = db.relationship('Hobby', backref='type')

    @staticmethod
    def create_type(type_name):
        """
        Create a new type.

        Args:
            type_name (str): The name of the type.

        Returns:
            Type: The newly created type object.
        """
        new_type = Type(type_name=type_name)
        db.session.add(new_type)
        db.session.commit()
        return new_type

    @staticmethod
    def get_type_by_id(type_id):
        """
        Get a type by its ID.

        Args:
            type_id (int): The ID of the type.

        Returns:
            Type: The type object.
        """
        return Type.query.get(type_id)

    def update_type_name(self, new_name):
        """
        Update the name of the type.

        Args:
            new_name (str): The new name of the type.
        """
        self.type_name = new_name
        db.session.commit()

    def delete_type(self):
        """
        Delete the type from the database.
        """
        db.session.delete(self)
        db.session.commit()
