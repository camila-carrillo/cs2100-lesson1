"""
TODO: A very useful temperature-conversion app.
"""
TEMP_THRESHOLD_F: float = 68

def greet_human() -> None:
    """ get a name from the keyboard
    and say hello! """
    name: str = input("What is your name?")
    print(f"hello { name }")

def is_it_cold_f(temp_f: float) -> bool:
    '''
    Determines if the supplied temperature 
    is below a threshold

    Parameters
    ==========
    temp_f : float
        supplied temperature in F
    
    Returns
    =========
    bool
        True if it is below a threshold
    '''
    return temp_f < TEMP_THRESHOLD_F


def main() -> None:
    pass # ... has the same functionality as pass!

if __name__ == "__main__":
    main()

