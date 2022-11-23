import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Derivative calculation using Newton's method.")
    parser.add_argument("f", type=str, help='The function to derive.')
    parser.add_argument("--x0", default=1, type=float, help="Start point.")
    parser.add_argument("", default=)



if __name__ == "__main__":
