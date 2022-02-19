import random 
from game.shared.color import Color
from game.shared.point import Point
from game.casting.artifact import Artifact

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._counter= 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")

        artifacts = cast.get_actors("artifacts")

        velocity = self._keyboard_service.get_direction()

        robot.set_velocity(velocity)  

        for artifact in artifacts:
            artifact.set_velocity(velocity)

        # artifacts.set_velocity(velocity)    

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        
        for artifact in artifacts:
            artifact.falling()
            if robot.get_position().equals(artifact.get_position()):
                message = artifact.get_message()
                banner.set_text(message)


        if self._counter == 10:
            
            test = ['42','9744']
            text = chr(int(random.choice(test))) 
            # * artificat , □ = 0x25A1

            #message = messages[n]

            x = random.randint(1, 40 - 1)
            y = 1
            position = Point(x, y)
            position = position.scale(15)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(15)
            artifact.set_color(color)
            artifact.set_position(position)
            # artifact.set_message(message)
            cast.add_actor("artifacts", artifact)
            
            self._counter=0
        else:
            self._counter +=1
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()