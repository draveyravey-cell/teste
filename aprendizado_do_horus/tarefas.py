import json
from datetime import datetime
import os

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.arquivo_tarefas = "tarefas.json"
        self.carregar_tarefas()

    def adicionar_tarefa(self, descricao, prazo=None):
        tarefa = {
            "id": len(self.tarefas) + 1,
            "descricao": descricao,
            "concluida": False,
            "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "prazo": prazo,
        }
        self.tarefas.append(tarefa)
        self.salvar_tarefas()
        print(f"\nTarefa '{descricao}' adicionada com sucesso!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("\nNenhuma tarefa encontrada!")
            return

        print("\n=== Lista de Tarefas ===")
        for tarefa in self.tarefas:
            status = "✓" if tarefa["concluida"] else " "
            prazo = f", Prazo: {tarefa['prazo']}" if tarefa['prazo'] else ""
            print(f"[{status}] {tarefa['id']}. {tarefa['descricao']} (Criada em: {tarefa['data_criacao']}{prazo})")

    def marcar_concluida(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                self.salvar_tarefas()
                print(f"\nTarefa '{tarefa['descricao']}' marcada como concluída!")
                return
        print("\nTarefa não encontrada!")

    def salvar_tarefas(self):
        with open(self.arquivo_tarefas, "w", encoding="utf-8") as arquivo:
            json.dump(self.tarefas, arquivo, ensure_ascii=False, indent=2)

    def carregar_tarefas(self):
        if os.path.exists(self.arquivo_tarefas):
            with open(self.arquivo_tarefas, "r", encoding="utf-8") as arquivo:
                self.tarefas = json.load(arquivo)

def exibir_menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Sair")
    return input("\nEscolha uma opção (1-4): ")

def main():
    gerenciador = GerenciadorTarefas()
    
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            descricao = input("\nDigite a descrição da tarefa: ")
            prazo = input("Digite o prazo (opcional, pressione Enter para pular): ").strip()
            prazo = prazo if prazo else None
            gerenciador.adicionar_tarefa(descricao, prazo)
            
        elif opcao == "2":
            gerenciador.listar_tarefas()
            
        elif opcao == "3":
            gerenciador.listar_tarefas()
            try:
                id_tarefa = int(input("\nDigite o ID da tarefa concluída: "))
                gerenciador.marcar_concluida(id_tarefa)
            except ValueError:
                print("\nID inválido! Digite um número.")
                
        elif opcao == "4":
            print("\nObrigado por usar o Gerenciador de Tarefas!")
            break
            
        else:
            print("\nOpção inválida! Por favor, escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()
