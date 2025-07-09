import sys
import os

def crack_zip(file, wordlist):
    import pyzipper
    with pyzipper.AESZipFile(file) as zf:
        for pwd in open(wordlist, "r", errors="ignore"):
            try:
                zf.extractall(pwd=pwd.strip().encode())
                print(f"[+] ZIP Password Found Tool made by @NGYT777GG: {pwd.strip()}")
                return
            except:
                print(f"[-] ZIP Trying: {pwd.strip()}")
    print("[-] Password not found in wordlist.")

def crack_rar(file, wordlist):
    for pwd in open(wordlist, "r", errors="ignore"):
        cmd = f'unrar x -p"{pwd.strip()}" "{file}" > /dev/null 2>&1'
        if os.system(cmd) == 0:
            print(f"[+] RAR Password Found: {pwd.strip()}")
            return
        else:
            print(f"[-] RAR Trying: {pwd.strip()}")
    print("[-] Password not found in wordlist.")

def crack_7z(file, wordlist):
    for pwd in open(wordlist, "r", errors="ignore"):
        cmd = f'7z x -p"{pwd.strip()}" "{file}" -oextracted > /dev/null 2>&1'
        if os.system(cmd) == 0:
            print(f"[+] 7Z Password Found: {pwd.strip()}")
            return
        else:
            print(f"[-] 7Z Trying: {pwd.strip()}")
    print("[-] Password not found in wordlist.")

def crack_pdf(file, wordlist):
    import pikepdf
    for pwd in open(wordlist, "r", errors="ignore"):
        try:
            pikepdf.open(file, password=pwd.strip())
            print(f"[+] PDF Password Found: {pwd.strip()}")
            return
        except:
            print(f"[-] PDF Trying: {pwd.strip()}")
    print("[-] Password not found in wordlist.")

def crack_docx(file, wordlist):
    import msoffcrypto
    import io
    for pwd in open(wordlist, "r", errors="ignore"):
        try:
            office_file = msoffcrypto.OfficeFile(open(file, "rb"))
            office_file.load_key(password=pwd.strip())
            office_file.decrypt(io.BytesIO())
            print(f"[+] DOCX Password Found: {pwd.strip()}")
            return
        except:
            print(f"[-] DOCX Trying: {pwd.strip()}")
    print("[-] Password not found in wordlist.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python brutecrack.py <file> <password.txt>")
        sys.exit(1)
    
    file = sys.argv[1]
    wordlist = sys.argv[2]

    if file.endswith(".zip"):
        crack_zip(file, wordlist)
    elif file.endswith(".rar"):
        crack_rar(file, wordlist)
    elif file.endswith(".7z"):
        crack_7z(file, wordlist)
    elif file.endswith(".pdf"):
        crack_pdf(file, wordlist)
    elif file.endswith(".docx") or file.endswith(".xlsx"):
        crack_docx(file, wordlist)
    else:
        print("[-] Unsupported file type!")

if __name__ == "__main__":
    main()

