def fibbonacci(n):
    sum = 1
    prim = 0
    for i in range(n+1):
        print(prim)
        aux = sum
        sum += prim
        prim = aux


if __name__ == '__main__':
    fibbonacci(int(input("Ingrese un valor: ")))
