'''
exc_type: O tipo de execução que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None.

exec_val: O valor da execeção que ocorreu, se houver.
    Se não ocorreu nenhuma execeção, este parâmetro será None.

exec_tb: O traceback (rastreamento de pilha) associado à execeção que ocorreu, se houver.
    Se não ocorreu nenhuma execeção, este parâmetro será None.
'''


class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou Saindo")

with AlgumaCoisa() as something:
    print("Estou no meio")
