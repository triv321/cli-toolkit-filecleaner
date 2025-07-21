import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description="CLI Utility tools")
    parser.add_argument("--run", help="Run the command")
    parser.add_argument("--echo", help="Prints the input")
    parser.add_argument("--cwd", action="store_true" ,help="prints cwd")
    args = parser.parse_args()

    if args.run:
        result = subprocess.run(args.run, shell=True, capture_output=True, text=True)
        print(result.stdout.strip())

    if args.echo:
        print(args.echo)

    if args.cwd:
        print(os.getcwd())

if __name__=="__main__":
    main()