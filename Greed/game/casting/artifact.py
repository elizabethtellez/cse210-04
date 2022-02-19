from game.casting.actor import Actor
from game.shared.point import Point


class Artifact (Actor): 
    def __init__(self):
        super().__init__()
        self._message = ""
        self._velocity = Point(0, 0)
        self._position = Point(0, 0)
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity

    def falling(self):
        x = self._position.get_x()
        y = self._position.get_y() + 1
        self._position = Point(x, y)
       

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position

