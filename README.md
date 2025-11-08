# Shatasks

Shatasks é um sistema ágil de gerenciamento de tarefas, permitindo criar, listar, atualizar e excluir tarefas, além de monitorar o progresso da equipe.

## Tecnologias
- Python 3.11
- Flask
- Pytest
- GitHub Actions

## Como Rodar
1. Clone o repositório: `git clone https://github.com/seuusuario/Shatasks.git`
2. Instale dependências: `pip install -r requirements.txt`
3. Execute o sistema: `python src/app.py`

## Metodologia
O projeto utiliza **Kanban** no GitHub Projects para organizar tarefas: To Do, In Progress, Done.

## 🔄 Mudança de Escopo

Durante o desenvolvimento, o cliente solicitou a adição de um novo campo `due_date` nas tarefas, permitindo definir uma data de entrega.  
Essa mudança exigiu:
- Atualização do endpoint de criação de tarefas (`POST /tasks`)
- Ajuste nos testes automatizados (`test_create_task_with_due_date`)
- Registro da mudança no Kanban (card “Adicionar campo due_date às tarefas”)

Essa modificação demonstra a flexibilidade e adaptabilidade do projeto às mudanças de requisitos — princípios fundamentais das metodologias ágeis.

