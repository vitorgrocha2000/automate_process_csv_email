# Automatização de Processo de E-mail para Relatório de Compras

Este código em Python tem como objetivo automatizar o processo de geração e envio de um relatório diário de compras para o seu chefe. O relatório contém informações sobre as compras de mercadorias da empresa, incluindo o total gasto, a quantidade de produtos comprados e o preço médio dos produtos.

## Funcionalidades

1. Autenticação no sistema da empresa: O código realizará o login no sistema da empresa para ter acesso aos dados das compras.

2. Download do arquivo CSV: Após o login, o código irá baixar o arquivo CSV que contém as informações sobre as compras realizadas.

3. Cálculo dos indicadores: O código processará o arquivo CSV e calculará o total gasto, a quantidade de produtos comprados e o preço médio dos produtos.

4. Envio do e-mail: Após calcular os indicadores, o código enviará um e-mail automático para o seu chefe contendo as informações solicitadas no relatório.

## Pré-requisitos

Antes de executar o código, certifique-se de que você possui os seguintes requisitos:

- Python 3 instalado
- Bibliotecas necessárias (ex: pandas, smtplib)
- Acesso ao sistema da empresa
- Configurações de e-mail para enviar mensagens SMTP

## Como usar

1. Faça o clone ou download do repositório para obter os arquivos necessários.

2. Certifique-se de ter todas as bibliotecas necessárias instaladas em seu ambiente Python.

3. Edite o arquivo `automate_process_csv_email.py` para adicionar as informações de login no sistema da empresa e as configurações de e-mail, como o endereço de e-mail do remetente e do destinatário.

4. Execute o script `automate_process_csv_email.py` para iniciar o processo de automação. O código realizará o login, baixará o arquivo CSV, calculará os indicadores e enviará o e-mail com o relatório de compras.

5. Verifique a caixa de e-mail do destinatário para confirmar o recebimento do relatório.

## Considerações Finais

Este código de automação simplificará o processo de geração e envio de relatórios diários de compras para o seu chefe, economizando tempo e esforço manual. Sinta-se à vontade para personalizar e ajustar o código de acordo com as necessidades da sua empresa.

Lembre-se de que as informações de login no sistema da empresa e as configurações de e-mail devem ser fornecidas corretamente para garantir o funcionamento adequado do código.

Espero que esta solução automatizada seja útil para você e ajude a otimizar suas tarefas diárias. Em caso de dúvidas ou problemas, não hesite em entrar em contato.

Divirta-se automatizando!
