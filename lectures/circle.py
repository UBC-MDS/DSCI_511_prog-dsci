class Circle:
    """A circle with a centre (x,y) and radius r."""
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def area(self):
        return np.pi * self.r**2

    def circumference(self):
        return 2.0 * np.pi * self.r

    def dist(self):
        """Compute the distance to the origin."""
        return np.abs(np.sqrt(self.x**2 + self.y**2) - self.r)
    
    def dist_between(self, other):
        """Compute the distance between this circle and another circle."""
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2) - (self.r + other.r)
    
    def translate(self, Δx, Δy):
        """Move the circle by (Δx, Δy)"""
        self.x += Δx
        self.y += Δy
        return self # This is not needed, but is sometimes convenient.
        
    def __str__(self):
        return "A Circle at (%.1f, %.1f) with radius %.1f." % (self.x, self.y, self.r)


MY_CONSTANT = 5

def my_function():
    pass
 