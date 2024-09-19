from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """King character"""
    def __init__(self, first_name, is_alive=True):
        """King Characters Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "blue"
        self.hairs = "light"
    
    def set_eyes(self, eyes):
        """Set the eyes color"""
        self.eyes = eyes
    
    def set_hairs(self, hairs):
        """Set the hairs color"""
        self.hairs = hairs
    
    def get_eyes(self):
        """Get the eyes color"""
        return self.eyes
    
    def get_hairs(self):
        """Get the hairs color"""
        return self.hairs