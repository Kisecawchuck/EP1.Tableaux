# EP1.Tableaux

Script de provas de validade de um sequente usando a técnica de tableaux semânticos.

## Uso

- `verificar_sequente(premissas, conclusao)`: Recebe uma lista de premissas e uma conclusão. Retorna um objeto com entradas `valido: bool` se o sequente é válido, `contraexemplo: {}` uma valoração que falsifica a expressão (se existir), e `regras: []` os passos da árvore de decisão do tableau.

- `mostra_resultado(r)`: Recebe o objeto de retorno de `verificar_sequente`, imprime se o sequente é válido, o contraexemplo se não for válido e os passos da árvore de decisão.

```python
from code_base_EP1 import *

P, Q = vars('P', 'Q') # define as variáveis

mostra_resultado(verificar_sequente([P >> Q, P], Q)) 'True', sequente válido
```

## Testando

A implementação requer `unittest`. Testes podem ser executados com:

    python -m unittest tests/checker.py
