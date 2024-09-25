# Validação de Dados e Tratamento de Exceções

# Objetivo
Desenvolver testes unitários para validar corretamente a inserção de dados em um sistema, garantindo o tratamento adequado de exceções. A atividade deverá seguir uma estrutura de pastas organizada.

# Descrição
Você deve implementar esta atividade conforme do diagrama de classes em anexo.

# Requisitos
## 1. Validação de Dados:
* Implemente métodos para garantir que os dados inseridos sejam válidos.
* Caso algum dado seja inválido, deve ser lançada uma exceção personalizada com uma mensagem adequada. Por exemplo:
* Nome inválido: O nome não pode ser vazio.
* Idade negativa: A idade deve ser maior ou igual a zero.
* Tipo de dado inválido: A idade deve ter apenas números inteiros.

## 2. Tratamentos de Exceções:
* O sistema deve capturar as exceções lançadas durante a validação e exibir uma mensagem de erro apropriada ao usuário.

## 3. Testes Unitários:
* Crie testes unitários para todos os cenários possíveis, incluindo:
* Inserção de dados válidos.
* Inserção de dados inválidos que disparem as exceções (ex: nome vazio, idade negativa, tipo de dado inválido).
* Cada teste deve garantir que a exceção correta seja lançada com a mensagem apropriada. 
* Use a biblioteca **pytest** para implementar os testes.

# Entrega
* O código deve estar corretamente versionado em etapas 
* Crie um repositório para armazenar o código fonte que responde a atividade proposta compartilhando o endereço do repositório via GitHub.
* Envie um comentário particular nesta atividade com o nome completo dos alunos que participaram.
* Apenas um dos componentes precisa enviar.

# Critérios de Avaliação
* Validação e tratamento correto de exceções.
* Cobertura completa de testes.
* Estrutura de pastas adequada.
* Clareza e organização do código.

# Contribuidores
<a href="https://github.com/f3rnn/SENAI-validacao-de-dados/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=f3rnn/SENAI-validacao-de-dados" alt="contrib.rocks image" />
</a>
