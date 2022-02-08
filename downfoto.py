from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('46d569f822607fa34567a844eb48a0ca')

    forms = jotformAPIClient.get_forms()

    for form in forms:
    	print(form["title"])

if __name__ == "__main__":
    main()