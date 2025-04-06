class Base:
    def __init__(self):
        print("Base.__init__")
        
    def feature(self):
        print("Feature from Base")

class FeatureA(Base):
    def __init__(self):
        super().__init__()  # Call parent constructor
        print("FeatureA.__init__")
        
    def feature(self):
        print("Feature from FeatureA")

class FeatureB(Base):
    def __init__(self):
        super().__init__()  # Call parent constructor
        print("FeatureB.__init__")
        
    def feature(self):
        print("Feature from FeatureB")
        
class AdvancedProduct(FeatureA, FeatureB):
    def __init__(self):
        super().__init__()  # This will follow the MRO chain
        print("AdvancedProduct.__init__")
        
    def feature(self):
        print("Feature from AdvancedProduct")
        super().feature()  # This calls the next method in the MRO

# Let's examine the MRO
print("Method Resolution Order:", [cls.__name__ for cls in AdvancedProduct.__mro__])

# Create an instance
product = AdvancedProduct()
print("\nCalling feature method:")
product.feature()