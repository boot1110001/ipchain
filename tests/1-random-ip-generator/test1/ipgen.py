
import random

NUMBER_OF_IPS = 50

def get_ip():
    n1 = str(random.randint(1, 192))
    n2 = str(random.randint(1, 254))
    n3 = str(random.randint(1, 254))
    n4 = str(random.randint(1, 254))
    p = str(random.randint(49153, 65534))
    return n1+'.'+n2+'.'+n3+'.'+n4+':'+p

def generate(n):
    out = []
    i = 0
    while i < n:
        out.append(get_ip())
        i+=1
    return out

def main():
    ips = generate(NUMBER_OF_IPS)
    print(ips)
    # for ip in ips:
    #     print(ip)

if __name__ == "__main__": main()
