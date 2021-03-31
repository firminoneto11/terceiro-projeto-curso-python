from main_window import main

# Executing the main() function
if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        input(f"Houve um erro na hora de executar o programa.\nDetalhes do mesmo -> {error}.\nPressione enter para "
              f"finalizar o programa: ")
