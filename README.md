# Validador de Cartões de Crédito

Este projeto é um validador de cartões de crédito desenvolvido em Python. Ele identifica a bandeira do cartão e valida o número utilizando o algoritmo de Luhn.

## Funcionalidades

- **Identificação da bandeira**: Detecta automaticamente a bandeira do cartão (Visa, MasterCard, Elo, American Express, Discover, Hipercard, Diners Club, EnRoute, JCB, Voyager e Aura) com base no número informado.
- **Validação do número**: Utiliza o algoritmo de Luhn para verificar se o número do cartão é válido.

## Como usar

1. Clone este repositório ou baixe os arquivos.
2. Execute o arquivo `index.py` com Python 3.x.
3. Altere o valor da variável `card_number` para o número do cartão que deseja validar.

Exemplo de uso:

```python
card_number = 5042216951795880  # Número de cartão de exemplo
result = validate_credit_card(card_number)
print(result)
```

Saída esperada:

```python
{'valid': True, 'bandeira': 'Aura'}
```

## Estrutura do Projeto

- `index.py`: Código principal com as funções de validação e identificação da bandeira.

## Requisitos

- Python 3.x

## Observações

- Este projeto é apenas para fins educacionais e não deve ser utilizado em produção para validação real de cartões de crédito.
- Não armazene nem compartilhe números reais de cartões de crédito.
