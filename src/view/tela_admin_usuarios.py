from view.utils import limpar_console

class TelaAdminUsuario():
    def tela_opcoes(self):
        print('SISTEMA DE MONITORAMENTO DE HARD SKILLS')
        print('--- MENU ADMIN. USUARIOS ---')
        print('Escolha uma opção:')
        print('1 - Listar usuarios')
        print('0 - Retornar')
        opcao = int(input('Digite a opção desejada: '))
        limpar_console()
        return opcao
    
    def mostra_usuario(self, dados_usuario):
        print('USERNAME DO USUARIO: @', dados_usuario['username'])
        print('NOME DO USUARIO: ', dados_usuario['nome'])
        print('CARREIRA ESCOLHIDA: ', dados_usuario['carreira'])

    def mostra_mensagem(self, mensagem):
        print(mensagem)