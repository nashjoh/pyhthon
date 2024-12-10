def hello (name,lang):
    greetings = {
        "English": "Hello",
        "Spanish":"hola",
        "German":"hallo"
    }
    msg =f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == '__main__':    
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provide  personal greeting."
    )

    parser.add_argument(
        "-n","--name", metavar ="name",
        required = True,help = "the name of the person to greet."
    )

    parser.add_argument(
        "-l","--lang",metavar= "laguage",
        required=True, choices=["English","Spanish","German"],
        help = "the language of the greeting ."
    )
    args = parser.parse_args()

hello(args.name,args.lang)