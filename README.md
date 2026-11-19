# EP1.Tableaux

Script de provas de validade de um sequente usando a técnica de tableaux semânticos.

## Uso

- `verify_valid(expression)`: Recebe um argumento `Proposition`, retorna uma tripla com a primeira entrada sendo a valoração que falsifica a expressão, a segunda sendo os passos do Tableaux e a terceira a árvore de decisão.

```python
from code_base_EP1 import *

P, Q = vars('P', 'Q') # define as variáveis

verify_valid(P | ~P) # 'None', a expressão é válida
verify_valid(P & ~P) # ['P': False], a expressão é falsificável
verify_valid((P >> Q) >> (~P | Q)) # 'None', a expressão é válida
```

## Testando

A implementação requer `unittest`. Testes podem ser executados com:

    python -m unittest tests/checker.py
