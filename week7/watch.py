import re


def main():
    print(parse(input("HTML: ")))


def parse(s):

    first_search = re.search(r'src="(.+?)"', s)
    if first_search and 'youtube.com' in first_search.group(1) and 'iframe' in s:
        second_search = re.search(r'embed/(\w)+', first_search.group(1))
        embed, link = second_search.group(0).split('/')
        return f"https://youtu.be/{link}"
    else:
        return None

...


if __name__ == "__main__":
    main()
