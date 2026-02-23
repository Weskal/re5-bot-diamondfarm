# RE5 Boot Bot (Automação da fase final)

Bot de automação para **Resident Evil 5**, focado no farm da fase final (run da diamante), com reinício automático do ciclo.

## Objetivo

Este projeto executa uma sequência repetitiva para:

1. Entrar na fase.
2. Trocar para o lança-foguetes.
3. Atirar na pedra.
4. Correr até o ponto do diamante/tesouro.
5. Coletar o item.
6. Reiniciar a run automaticamente.

## Ambiente usado (referência)

- **Sistema:** Windows
- **Monitor:** 27"
- **Resolução:** 1920x1080 (Full HD)
- **Tecla de troca do lança-foguetes (inventário):** `2`

> As posições de câmera, tempo de ação e comportamento do inventário podem variar de máquina para máquina.

## Estrutura do projeto

- `RE5_BOT_DIAMOND-ALLSTRATEGIES-withESC-FUNCTIONAL.py`: versão principal funcional com fluxo completo.

## Como executar

1. Abra o jogo e deixe a janela com o título **RESIDENT EVIL 5** disponível (de preferência no modo janela).
2. Execute o script principal:

```bash
python RE5_BOT_DIAMOND-ALLSTRATEGIES-withESC-FUNCTIONAL.py
```

## Dependências

Instale os pacotes usados pelos scripts:

```bash
pip install pywin32 pynput pyautogui
```

## Onde trocar a tecla do inventário (lança-foguetes)

No seu caso, a tecla é `2`. Se quiser alterar para outra tecla (exemplo: `3`, `1`, `q`, etc.), mude na função `send_key_2()`.

### Arquivo principal

No arquivo `RE5_BOT_DIAMOND-ALLSTRATEGIES-withESC-FUNCTIONAL.py`, altere:

```python
keyboard.press('2')
keyboard.release('2')
```

## Ajustes recomendados

- Se seu monitor/resolução for diferente, ajuste tempos de `sleep` e movimentos de câmera.
- Mantenha sempre o jogo em foco para garantir que os inputs sejam registrados corretamente.
- Não deixe o jogo no modo online.
- Se o inventário estiver em outra ordem, altere a tecla de seleção da arma.
- Mantenha o jogo em modo/janela e foco corretos para melhor consistência da automação.
- Altere o loop for (for i in range(1)) na linha 459 de acordo com a quantidade de runs desejada (exemplo: `for i in range(10)` para 10 runs).

## Aviso

Projeto criado para uso educacional/experimental em automação de input local.
Não é recomendado o uso de bots em jogos online ou que possam violar os termos de serviço do jogo. Use com responsabilidade.

## Autoria
Desenvolvido por Gabriel Paliato.
