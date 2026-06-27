def convert(text):
    text= text.replace(":)","🙂").replace(":(","🙁")
    return text

def main():
    text= input()
    result= convert(text)
    print(result)

main()
