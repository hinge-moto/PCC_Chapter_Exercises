# May 16.2022

def make_shirt(size, print_slogan):
    """Prints the size and message of a shirt"""
    print(f"Your size {size.title()} shirt will be printed with {print_slogan}.")

make_shirt('m', 'Breast Inspector')
make_shirt(size='m', print_slogan='Breast Inspector')
