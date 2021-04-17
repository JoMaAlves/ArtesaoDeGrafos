import os

#  𝓑𝓸𝓶 𝓭𝓲𝓪 𝓑𝓻𝓮𝓷𝓲𝓷𝓱𝓸, 𝓹𝓸𝓭𝓮𝓻𝓲𝓪𝓼 𝓲𝓷𝓹𝓾𝓽𝓪𝓻 𝓾𝓶 𝓰𝓻𝓪𝓯𝓸 𝓮𝓶 𝓷𝓸𝓼𝓼𝓸 𝓹𝓻𝓸𝓰𝓻𝓪𝓶𝓪? 

def printMenu(type, clear):

    if not type:

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

        print("""
                    +----------------------------------------------------------+   
                    |                                                          |
                    |                  Deseja criar um grafo?                  |
                    |                                                          |
                    |                  [ 1 ] Sim   [ 2 ] Nao                   |
                    |                                                          |
                    +----------------------------------------------------------+
        """)

        while True:
            start = input("                             Resposta: ")
            if ((start == "2") or (start.capitalize() == "Nao") 
                    or (start.capitalize() == "Não")):
                return 0, None, None
            elif ((start == "1") or (start.capitalize() == "Sim")):
                break
        
        os.system(clear)
        
        print("""
                    +----------------------------------------------------------+   
                    |                                                          |
                    |                  Deseja criar um grafo:                  |
                    |                                                          |
                    |         [ 1 ] Direcionado   [ 2 ] Não Direcionado        |
                    |                                                          |
                    +----------------------------------------------------------+
        """)

        answer1 = None
        while True:
            answer1 = input("                             Resposta: ")
            
            if ((answer1 == "1") or (answer1.capitalize() == "Direcionado")):
                answer1 = True
                break
            
            elif ((answer1 == "2") or (answer1.capitalize() == "Não direcionado")
                    or (answer1.capitalize() == "Nao direcionado")):
                answer1 = False
                break

        os.system(clear)
        
        print("""
                    +----------------------------------------------------------+   
                    |                                                          |
                    |                  Deseja criar um grafo:                  |
                    |                                                          |
                    |            [ 1 ] Valorado   [ 2 ] Não Valorado           |
                    |                                                          |
                    +----------------------------------------------------------+
        """)

        answer2 = None
        while True:
            answer2 = input("                             Resposta: ")
            
            if ((answer2 == "1") or (answer2.capitalize() == "Valorado")):
                answer2 = True
                break
            
            elif ((answer2 == "2") or (answer2.capitalize() == "Não valorado")
                    or (answer2.capitalize() == "Nao valorado")):
                answer2 = False
                break

            
        os.system(clear)
        return 1, answer1, answer2
    
    elif (type == 1):
        print("""
                                   __  __                     
                                  |  \/  |  ___   _ _    _  _ 
                                  | |\/| | / -_) | ' \  | || |
                +---------------- |_|  |_| \___| |_||_|  \_,_| ----------------+                      
                |                                                              |
                |   [ 1 ] Adicionar Vertice   [ 5 ] Tamanho do Grafo           |
                |   [ 2 ] Adicionar Aresta    [ 6 ] Checar Vertices Adjacentes |
                |   [ 3 ] Imprimir Grafo      [ 7 ] Checar Grau de Vertice     |
                |   [ 4 ] Ordem do Grafo      [ 0 ] Sair                       |
                |                                                              |
                +--------------------------------------------------------------+
        """)

        return input("                             Resposta: ")
    
    else:
        print("""
                         ___    _            _                    _       
                        / _ \  | |__   _ _  (_)  __ _   __ _   __| |  ___ 
                       | (_) | | '_ \ | '_| | | / _` | / _` | / _` | | _ |
                        \___/  |_.__/ |_|   |_| \__, | \__,_| \__,_| |___|
                                                |___/                     
                                          _ __   ___   _ _ 
                                         | '_ \ / _ \ | '_|
                                         | .__/ \___/ |_|  
                                         |_|               
                     ___                _     _        _                     
                    | _ \  __ _   _ _  | |_  (_)  __  (_)  _ __   __ _   _ _ 
                    |  _/ / _` | | '_| |  _| | | / _| | | | '_ \ / _` | | '_|
                    |_|   \__,_| |_|    \__| |_| \__| |_| | .__/ \__,_| |_|  
                                                          |_|                
        """)
        
        