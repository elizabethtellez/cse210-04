import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import time
class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.
    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._last_time_grown = time.time()

    def execute(self, cast, script):
        """Executes the handle collisions action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_snake_collision (cast)
            self._handle_game_over(cast)
            self._handle_time_passage(cast)

    def _handle_time_passage(self, cast):
        snake = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")

        now = time.time()
        if now - self._last_time_grown >= 5:
            snake.grow_tail(2)
            snake2.grow_tail(2)
            self._last_time_grown = now

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snake1")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True


    def _handle_snake_collision (self,cast):
       
       snake1 = cast.get_first_actor("snake1")
       segments1 = snake1.get_segments()[1:]
       head1 = snake1.get_segments()[0]
    
       snake2 = cast.get_first_actor("snake2")
       segments2 = snake2.get_segments()[1:]
       head2 = snake2.get_segments()[0]
    
       for segment2 in segments2:
            if head1.get_position().equals(segment2.get_position()):      
                self._is_game_over = True

       for segment1 in segments1:
            if head2.get_position().equals(segment1.get_position()):      
                self._is_game_over = True
     

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake1 = cast.get_first_actor("snake1")
            segments1 = snake1.get_segments()

            snake2 = cast.get_first_actor("snake2")
            segments2 = snake2.get_segments()

            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment1 in segments1:
                segment1.set_color(constants.WHITE)

            for segment2 in segments2: 
                segment2.set_color(constants.WHITE)
        