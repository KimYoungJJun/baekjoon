def cut_chocolate(n,m):
    return (n-1) + n * (m-1)

if __name__ == "__main__":
    n,m = map(int,input().split())
    print(cut_chocolate(n,m))