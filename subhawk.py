
# using try for KeyboardInterrupt
try:
    import argparse
    import requests
    import time
    import tldextract



    parser = argparse.ArgumentParser(epilog="Author: Abdullah Fayyad")

    # add the arguments

    parser.add_argument('-d', '--domain', help='target domain [example.com]', type=str, required=True)
    parser.add_argument('-v', '--verbose', help='show valid and invalid subdomains', action='store_true')
    parser.add_argument('-o', '--output', help='save the valid subdomains in a text file' )
    parser.add_argument('-l', '--list', help='add list of subdomains [example.txt]' )
    parser.add_argument('-t', '--timeout', help='set the timeout (in seconds) for each request. default is 3 seconds',type=int )


    args = parser.parse_args()




    # Test if domain is valid
    try:
        extracted = tldextract.extract(args.domain)
        extra = f"{extracted.domain}.{extracted.suffix}"

        requests.get(f"http://{extra}", timeout=3)
        domain = f".{extra}"


        print("\n\n")
        text = "\033[93m[*]Staring...\033[0m"
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.2)
        print("\n\n")

        # Check if the user provided a list or is using the default list 
        listOfSubs = None
        if bool(args.list):
            listOfSubs = open (args.list,"r")

        else:
            listOfSubs = open ("subs.txt","r")

        subs = listOfSubs.read()


        # Check if the user provided a timeout 
        timeout = None
        if bool(args.timeout):
            timeout = args.timeout
        else:
            timeout = 3

        # Check if the user enabled the verbose option 
        if args.verbose:
            validSub = []
            inValidSub = []

            # Loop through the list of subs and concatenate with the domain 
            for sub in subs.splitlines():
                url= sub+domain

                # Check if the subdomain is valid 
                try:
                    response = requests.get(f"http://{url}", timeout=timeout)
                    print(f"\033[92m[+] Found: {url} - Status: {response.status_code}\033[0m")
                    validSub.append(url)
                    # Check if the user wants to save the output 
                    if args.output:
                        output = open(args.output,"a")
                        output.write(f"{url}\n")
                except requests.exceptions.RequestException:
                    print(f"\033[91m[-] Failed: {url}\033[0m")
                    inValidSub.append(url)

            print('\n\n\n')

            print("\033[93m[+]Valid Subdomains\n\033[0m")

            # Loop through the valid subdomains and print them
            for subdomain in validSub:
                print(subdomain)


            print('\n\n\n')
            print("\033[93m[-]Invalid Subdomains\n\033[0m")

            # Loop through the invalid subdomain and print them
            for subdomain in inValidSub:
                print(subdomain)


        else :
            for sub in subs.splitlines():
                url= sub+domain
                try:
                    response = requests.get(f"http://{url}", timeout=timeout)
                    print(f"\033[92m[+] Found: {url} - Status: {response.status_code}\033[0m")
                    if bool(args.output):
                        output = open(args.output,"a")
                        output.write(f"{url}\n")
                except requests.exceptions.RequestException:
                    pass

        print("\n\n")
        text = "\033[93m[*]Ending.\033[0m"
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)             



    except requests.exceptions.RequestException:
        print(f"\033[31m{args.domain} is not a real domain\033[0m")


except KeyboardInterrupt:
    exit(0)
    