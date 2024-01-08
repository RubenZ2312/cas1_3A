def escriure_quadrat(n):
    num_actual = 0
    for fila in range(n):
        for columna in range(n):
            print(num_actual, end='')
            num_actual = (num_actual + 1) % 10
        print()
    print()  # Línea en blanc entre quadrats

def main():
    try:
        n = int(input())
        while n > 0:
            escriure_quadrat(n)
            n = int(input())
    except EOFError:
        pass

if __name__ == "__main__":
    main()

