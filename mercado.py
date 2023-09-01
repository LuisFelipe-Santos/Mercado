from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda



class Loja:
    def __init__(self) -> None:
        self.produtos: List[Produto] = []

    def is_numero(self, entrada: str) -> bool:
        try:
            float(entrada)
            return True
        except ValueError:
            return False

    def cadastrar_produto(self) -> None:
        print('Cadastro de Produto')
        print('===================')

        nome: str = input('Informe o nome do produto: ')

        preco: float = self.ler_preco()

        produto: Produto = Produto(nome, preco)

        self.produtos.append(produto)

        print(f'O produto {produto.nome} foi cadastrado com sucesso!')
        sleep(1)

    def ler_preco(self) -> float:
        while True:
            preco_str = input('Informe o preço do produto: ')

            # Remove espaços em branco em excesso
            preco_str = preco_str.strip()

            # Substitui vírgula por ponto
            preco_str = preco_str.replace(',', '.')

            if self.is_numero(preco_str):
                preco = float(preco_str)
                return preco
            else:
                print("Erro: Formato de preço inválido. Use números e um ponto ou vírgula como separador decimal.")

    def listar_produtos(self) -> None:
        if len(self.produtos) > 0:
            print('Listagem de produtos cadastrados')
            print('--------------------')
            for produto in self.produtos:
                print(produto)
                print('----------------')
                sleep(1)
        else:
            print('Ainda não existem produtos cadastrados.')
        sleep(1)

    def pega_produto_por_codigo(self, codigo: int) -> Produto:
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None


class Carrinho:
    def __init__(self) -> None:
        self.carrinho: List[Dict[Produto, int]] = []

    def comprar_produto(self, produtos: List[Produto]) -> None:
        if len(produtos) > 0:
            print('Informe o código do produto que deseja adicionar ao carrinho: ')
            print('--------------------------------------------------------------')
            print('================== Produtos Disponíveis ======================')
            for produto in produtos:
                print(produto)
                print('---------------------------------------------------------')
                sleep(1)
            codigo: int = int(input())

            produto: Produto = self.pega_produto_por_codigo(codigo, produtos)

            if produto:
                if len(self.carrinho) > 0:
                    tem_no_carrinho: bool = False
                    for item in self.carrinho:
                        quant: int = item.get(produto)
                        if quant:
                            item[produto] = quant + 1
                            print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                            tem_no_carrinho = True
                            sleep(1)
                            return
                    if not tem_no_carrinho:
                        prod = {produto: 1}
                        self.carrinho.append(prod)
                        print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                        sleep(1)
                        return
                else:
                    item = {produto: 1}
                    self.carrinho.append(item)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(1)
                    return
            else:
                print(f'O produto com código {codigo} não foi encontrado.')
                sleep(1)
        else:
            print('Ainda não existem produtos para vender.')
            sleep(1)

    def pega_produto_por_codigo(self, codigo: int, produtos: List[Produto]) -> Produto:
        for produto in produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def visualizar_carrinho(self) -> None:
        if len(self.carrinho) > 0:
            print('Produtos no carrinho: ')

            for item in self.carrinho:
                for dados in item.items():
                    print(dados[0])
                    print(f'Quantidade: {dados[1]}')
                    print('-----------------------')
                    sleep(1)
        else:
            print('Ainda não existem produtos no carrinho.')
        sleep(1)

    def fechar_pedido(self) -> None:
        if len(self.carrinho) > 0:
            valor_total: float = 0

            print('Produtos do Carrinho')
            for item in self.carrinho:
                for dados in item.items():
                    print(dados[0])
                    print(f'Quantidade: {dados[1]}')
                    valor_total += dados[0].preco * dados[1]
                    print('------------------------')
                    sleep(1)
            valor_formatado = formata_float_str_moeda(valor_total)
            print(f'Sua fatura é {valor_formatado}')
            sleep(1)
        else:
            print('Ainda não existem produtos no carrinho.')
        sleep(1)


class SistemaLoja:

    def __init__(self) -> None:
        self.loja = Loja()
        self.carrinho = Carrinho()

    def main(self) -> None:
        self.mensagem_ini()
        self.menu()

    def mensagem_ini(self) -> None:
        print('===================================')
        print('===========  Bem-vindo(a) ==========')
        print('===========  Geek Shop 🛒  ==========')
        print('===================================')

    def menu(self) -> None:
        while True:
            print('\nSelecione uma opção abaixo: ')
            print('1 - Cadastrar produto')
            print('2 - Listar produtos')
            print('3 - Comprar produto')
            print('4 - Visualizar carrinho')
            print('5 - Fechar pedido')
            print('6 - Sair do sistema')

            escolha = input('Digite a opção escolhida (número ou texto): ')

            if escolha == '1' or escolha.lower() == 'cadastrar produto':
                self.loja.cadastrar_produto()
            elif escolha == '2' or escolha.lower() == 'listar produtos':
                self.loja.listar_produtos()
            elif escolha == '3' or escolha.lower() == 'comprar produto':
                self.carrinho.comprar_produto(self.loja.produtos)
            elif escolha == '4' or escolha.lower() == 'visualizar carrinho':
                self.carrinho.visualizar_carrinho()
            elif escolha == '5' or escolha.lower() == 'fechar pedido':
                self.carrinho.fechar_pedido()
            elif escolha == '6' or escolha.lower() == 'sair do sistema':
                print('Obrigado por escolher a Geek Shop! Esperamos vê-lo novamente em breve. Tenha um ótimo dia! 👋😊')
                sleep(1)
                exit(0)
            else:
                print('Erro: Opção inválida!')
                sleep(1)


