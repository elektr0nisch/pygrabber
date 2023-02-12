import argparse

def download(args):
    url = args.input[0]
    target_path = args.output[0]

    print(f"Downloading media from {url} to {target_path} ...")

    

def main():
    parser = argparse.ArgumentParser(description = "Open-source media grabber")
    parser.add_argument("-i", "--input", type = str, nargs = 1, metavar = 'url', help = "URL of the media to be grabbed")
    parser.add_argument("-o", "--output", type = str, nargs = 1, metavar = 'url', help = "Path for saving the grabbed media")

    args = parser.parse_args()

    print(args)

    if args != None:
        download(args)

if __name__ == "__main__":
    main()