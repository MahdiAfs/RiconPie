import argparse

def argges():
    
    parser = argparse.ArgumentParser(description='Process some inputs.')

    parser.add_argument('--input', type=str, help='input to run the program')
    parser.add_argument('--information', help=' information for program' , required=False)
    parser.add_argument('--Hwork', help='information for program work' , required=False)


    args = parser.parse_args()

    if args.input is not None:
        url = args.input
        print (url)
    if args.information:
        print(f"This project is to identify the target for cyber attack.")
    if args.Hwork:
        print(f" When the user enters the input, it will display all the links of the site \n and all the subdomains of the links and the IPs of the links and all the open ports of the IPs \n and title lines in addition to the Status codes of the links.")
