---
name: "Validar tela"
description: "Use quando precisar validar visualmente uma tela, pagina ou fluxo da aplicacao em desktop e mobile"
argument-hint: "URL ou tela e cenario a validar"
agent: "agent"
---

Execute uma validacao visual da interface para: ${input:alvo:URL ou tela e cenario a validar}.

1. Identifique como iniciar ou acessar a aplicacao usando a documentacao e configuracao existentes. Nao altere arquivos, a menos que eu solicite uma correcao apos o relatorio.
2. Abra a tela no navegador e valide o cenario informado. Se o alvo nao especificar uma URL, determine a rota relevante a partir do codigo.
3. Inspecione a tela nos viewports desktop (1440 x 900) e mobile (390 x 844). Interaja com os controles essenciais do cenario antes de concluir.
4. Capture screenshots da tela nos dois viewports apos executar o cenario. Inclua os caminhos ou anexos dessas capturas no relatorio.
5. Relate somente problemas observados ou estados que nao puderam ser verificados. Verifique especialmente: carregamento, elementos cortados ou sobrepostos, legibilidade, responsividade, feedback de erro/sucesso e controles inacessiveis.

Responda em portugues no formato abaixo:

## Resultado
`Aprovado`, `Reprovado` ou `Validacao parcial`

## Achados
- `[Gravidade]` Descricao objetiva do problema, viewport/acao que o reproduz e impacto.

## Evidencias
- Screenshot desktop: caminho ou anexo.
- Screenshot mobile: caminho ou anexo.

## Nao verificado
- Dependencias, credenciais, dados ou limitacoes que impediram a verificacao.

Nao invente achados. Se nao houver problemas observados, escreva `Nenhum problema visual observado` em **Achados**.