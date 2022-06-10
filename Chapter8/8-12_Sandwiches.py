# May 19.2022

def build_sandwich(*ingredients):
    """Print a sandwich summary."""
    print("This sandwich has these great ingredients:")
    for ingredient in ingredients:
        print(f" - {ingredient}")

build_sandwich('ham', 'cheese', 'mayo', 'lettuce', 'tomato', 'saltnpep')
