from time import sleep

def printMenu(type):

    if not type:
#  𝓑𝓸𝓶 𝓭𝓲𝓪 𝓑𝓻𝓮𝓷𝓲𝓷𝓱𝓸, 𝓹𝓸𝓭𝓮𝓻𝓲𝓪𝓼 𝓲𝓷𝓹𝓾𝓽𝓪𝓻 𝓾𝓶 𝓰𝓻𝓪𝓯𝓸 𝓮𝓶 𝓷𝓸𝓼𝓼𝓸 𝓹𝓻𝓸𝓰𝓻𝓪𝓶𝓪?

        print("""
                         ___                  __   __  _             _
                        | _ )  ___   _ __     \ \ / / (_)  _ _    __| |  ___ 
                        | _ \ / -_) | '  \     \ V /  | | | ' \  / _` | | _ |
                        |___/ \___| |_|_|_|     \_/   |_| |_||_| \__,_| |___|
                                            __ _   ___ 
                                           / _` | | _ |
                                           \__,_| |___|
                             ___   _        _                         
                            / __| (_)  ___ | |_   ___   _ __    __ _  
                            \__ \ | | (_-< |  _| / -_) | '  \  / _` | 
                            |___/ |_| /__/  \__| \___| |_|_|_| \__,_| 
   _           _                                  _            ___                 __            
  /_\    _ _  | |_   ___   ___  __ _   ___     __| |  ___     / __|  _ _   __ _   / _|  ___   ___
 / _ \  | '_| |  _| / -_) (_-< / _` | / _ \   / _` | / -_)   | (_ | | '_| / _` | |  _| / _ \ (_-<
/_/ \_\ |_|    \__| \___| /__/ \__,_| \___/   \__,_| \___|    \___| |_|   \__,_| |_|   \___/ /__/
        """)
        
        sleep(5)

        print("""
                    +----------------------------------------------------------+   
                    |                                                          |
                    |                     Deseja iniciar?                      |
                    |                                                          |
                    |                  [ 1 ] Sim   [ 2 ] Nao                   |
                    |                                                          |
                    +----------------------------------------------------------+
        """)

        while True:
            start = input("                             Resposta: ")
            if((start == "2") or (start.capitalize() == "Nao") or (start.capitalize() == "Não")):
                return 0, None, None
            elif((start == "1") or (start.capitalize() == "Sim")):
                break
        
        print("""
                    +----------------------------------------------------------+   
                    |                                                          |
                    |                  Deseja criar um grafo:                  |
                    |                                                          |
                    |         [ 1 ] Direcionado   [ 2 ] Não Direcionado        |
                    |                                                          |
                    +----------------------------------------------------------+
        """)

        answer1 = int(input("        Sua reposta: "))

        print("""
                    +----------------------------------------------------------+   
                    |                                                          |
                    |                  Deseja criar um grafo:                  |
                    |                                                          |
                    |            [ 1 ] Valorado   [ 2 ] Não Valorado           |
                    |                                                          |
                    +----------------------------------------------------------+
        """)

        answer2 = int(input("        Sua reposta: "))

        return 1, answer1, answer2
    else:
        print("""
        +--------------------------------------+
        |                                      |
        |   [ 1 ] Adicionar Vertice            |
        |   [ 2 ] Adicionar Aresta             |
        |   [ 3 ] Imprimir Grafo               |
        |   [ 4 ] Ordem do Grafo               |
        |   [ 5 ] Tamanho do Grafo             |
        |   [ 6 ] Checar Vertices Adjacentes   |
        |   [ 7 ] Checar Grau de Vertice       |
        |                                      |
        +--------------------------------------+
        """)

        return 
        
        