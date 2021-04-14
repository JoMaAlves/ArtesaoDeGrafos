def printMenu(type):
    # print("=" * 24, " MENU ", "=" * 24)
    # print("=" * 56)
    if not type:

        
        print("""
        +-----------------------------------+
        |                                   |
        |       BEM VINDO AO SISTEMA        |
        |            DE GRAFOS!!            |
        |             PRESSIONE             |
        |             [ ENTER ]             |
        |          PARA CONTINUAR!          |
        |                                   |
        +-----------------------------------+
        """)
        input("        Começar: ")

        print("""
        +----------------------------------+
        |                                  |
        |      Deseja criar um grafo:      |
        |                                  |
        |      [ 1 ] Direcionado           |
        |      [ 2 ] Não Direcionado       |
        |                                  |
        +----------------------------------+
        """)

        answer1 = int(input("        Sua reposta: "))


        print("""
        +----------------------------------+
        |                                  |
        |      Deseja criar um grafo:      |
        |                                  |
        |      [ 1 ] Valorado              |
        |      [ 2 ] Não Valorado          |
        |                                  |
        +----------------------------------+
        """)

        answer2 = int(input("        Sua reposta: "))

        return answer1, answer2
    else:
        return 0, 1