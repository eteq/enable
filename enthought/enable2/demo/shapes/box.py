""" A moveable box shape. """


# Local imports.
from shape import Shape


class Box(Shape):
    """ A moveable box shape. """
        
    ###########################################################################
    # Protected 'Component' interface.
    ###########################################################################

    def _draw(self, gc, view_bounds=None, mode='default'):
        """ Draw the component. """
        
        gc.save_state()
                
        gc.set_fill_color(self._get_fill_color(self.event_state))

        dx, dy = self.bounds
        x, y = self.position
        gc.rect(x, y, dx, dy)
        gc.fill_path()
        
        gc.restore_state()

        return
    
#### EOF ######################################################################