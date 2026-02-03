


file = input("File name: ").strip().lower()

'''
.jpeg .jpg .gif .png image/png
.pdf application/pdf
.txt text/plain
.zip application/zip

everything else application/octect-stream

'''

if file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.gif') or file.endswith('.png'):
    print("application/pdf")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")