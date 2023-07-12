from . import rep

def main():
    while True:
        try:
            text = input('sql_lisfy> ')
        except (EOFError, KeyboardInterrupt):
            break

        res = rep.rep(text)
        if res:
            print(res)
