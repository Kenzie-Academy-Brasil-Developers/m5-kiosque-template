# M5 - Kiosque

## Como rodar os testes localmente

1. Instalar o pacote `pytest-testdox`:
```shell
pip install pytest-testdox
```

2. Rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```


### Rodando os testes localmente para o extra (não contabiliza para a entrega)

```shell
pytest --testdox -vvs tests/test_management/extra_add_product.py
```

