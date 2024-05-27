# Gerenciador de Finanças Pessoais

Um aplicativo simples para gerenciar suas finanças pessoais, permitindo o rastreamento de receitas e despesas, geração de relatórios e visualização de gráficos.

## Funcionalidades

- **Rastreamento de Transações**: Adicione receitas e despesas com categorias, descrições, valores e datas.
- **Exibição de Transações**: Veja todas as transações registradas.
- **Geração de Relatórios**: Gere relatórios financeiros mensais e anuais.
- **Visualização de Gráficos**: Visualize dados financeiros através de gráficos.

## Requisitos

- Python 3.x
- Tkinter
- tkcalendar
- pandas
- matplotlib

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/MiguelPereiraDantas/Aplicativo-de-Finan-as-Pessoais.git
    cd gerenciador-financas-pessoais
    ```

2. Instale as dependências:
    ```sh
    pip install tkcalendar pandas matplotlib
    ```

## Uso

1. Execute o arquivo `app.py`:
    ```sh
    python app.py
    ```

2. A interface gráfica será aberta, permitindo:
    - Adicionar transações preenchendo os campos e clicando no botão "Adicionar".
    - Exibir todas as transações clicando no botão "Exibir Transações".
    - Gerar e exibir relatórios mensais e anuais clicando nos respectivos botões.
    - Visualizar gráficos mensais e anuais clicando nos respectivos botões.

## Estrutura do Banco de Dados

O banco de dados SQLite `financas_pessoais.db` contém uma tabela `transacoes` com as seguintes colunas:

- `id` (INTEGER): Identificador único da transação.
- `tipo` (TEXT): Tipo da transação ("Receita" ou "Despesa").
- `categoria` (TEXT): Categoria da transação.
- `descricao` (TEXT): Descrição da transação.
- `valor` (REAL): Valor da transação.
- `data` (TEXT): Data da transação.

## Exemplo de Uso

### Adicionar Transação

Preencha os campos do formulário:
- Tipo: Receita ou Despesa
- Categoria: Alimentação, Transporte, etc.
- Descrição: Detalhes sobre a transação
- Valor: Quantia em dinheiro
- Data: Data da transação

Clique em "Adicionar" para salvar a transação.

### Exibir Transações

Clique em "Exibir Transações" para visualizar todas as transações registradas.

### Gerar Relatórios

Clique em "Relatório Mensal" ou "Relatório Anual" para gerar e visualizar os relatórios financeiros correspondentes.

### Visualizar Gráficos

Clique em "Gráfico Mensal" ou "Gráfico Anual" para visualizar gráficos das transações agregadas por mês ou ano.

## Contribuição

1. Fork este repositório.
2. Crie uma branch: `git checkout -b minha-nova-funcionalidade`.
3. Faça suas alterações e commit: `git commit -m 'Adicionei uma nova funcionalidade'`.
4. Envie para o branch original: `git push origin minha-nova-funcionalidade`.
5. Crie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autor

- [Miguel Pereira Dantas de Oliveira](https://github.com/MiguelPereiraDantas)
