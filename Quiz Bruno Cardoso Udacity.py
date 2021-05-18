# coding=utf-8
lacuna = '_____'
lacuna_selecionada = '[_____]'

todas_frases = [
  'A {lacuna} é conhecida como a rainha das uvas tintas. A origem dela é da região de Bordeaux, no sudoeste da {lacuna} ela é a uva vinífera mais difundida no mundo. Os vinhos podem ser {lacuna} com diversos pratos e são rico em {lacuna}.',
  'A uva {lacuna} é uma variedade originária da região de Bordeaux, na França. A casta foi dada como extinda após os vinhedos serem devastado pela praga filoxera por volta dos anos 1870. Porém, exemplares da uva acabaram migrando com europeus para o continente sul-americano e sendo cultivados no {lacuna} em meio a vinhedos de {lacuna}, variedade com a qual era confundida. Foi somente em {lacuna} que a vinha foi redescoberta por especialistas e identificada como a mesma que tinha desaparecido na europa.',
  'Se o vinho tem muitos {lacuna}, ele fica com sabor seco e amargo já que dão corpo e complexidade à bebida. Os vinhos de {lacuna} são aqueles amadurecido em barris, envelhecido na garrafa. Por outro lado, {lacuna} são as borbulhas dos {lacuna}.'
]

todas_respostas = [
  ['cabernet sauvignon', 'França', 'harmonizados', 'taninos'],
  ['carmenere', 'Chile', 'Merlot', '1994'],
  ['taninos', 'reserva', 'perlage', 'espumantes']
]

def pergunta_dificuldade():
  """Pergunta ao usuário a dificuldade e retorna o índice correspondente."""
  dificuldade = input('> Selecione um grau de dificuldade (fácil, médio ou difícil):\n')
  while True:
    if dificuldade == 'fácil':
      return 0
    elif dificuldade == 'médio':
      return 1
    elif dificuldade == 'difícil':
      return 2
    else:
      dificuldade = input('> Opção inválida, tente novamente.\n')

def pergunta_numero_tentativas():
  """Pergunta ao usuário o número de tentativas erradas que ele pode fazer antes de perder."""
  resposta = input('> Quantas tentativas você precisa (número maior que zero)?:\n')
  while True:
    try:
      numero_tentativas = int(resposta)
      if numero_tentativas <= 0:
        raise ValueError()
      return numero_tentativas
    except ValueError:
      resposta = input('> Opção inválida, tente novamente.\n')

def obtem_frase_e_respostas(dificuldade):
  """Obtém a frase e a lista de respostas para a dificuldade informada.
  Args:
        dificuldade (int): Indice da dificuldade selecionada pelo usuário.
  Returns:
        str: Frase com lacunas.
        list: Lista com as respostas para cada lacuna.
  """
  return todas_frases[dificuldade].format(lacuna=lacuna), todas_respostas[dificuldade]

def pergunta_resposta(frase, resposta, numero_tentativas):
  """Pergunta ao usuário a resposta para a primeira lacuna da frase.
  Args:
        frase (str): Frase que será exibida para o usuário.
        resposta (str): Resposta correta.
        numero_tentativas (int): Número de tentativas erradas que o usuário pode fazer antes de perder.
  Returns:
        int: Número de tentativas restantes.
        str: Frase com a lacuna substituida pela resposta.
  """
  nova_frase = frase.replace(lacuna, lacuna_selecionada, 1)
  print("\n***\n\n" + nova_frase)
  while numero_tentativas > 0:
    resposta_usuario = input('\n> Qual o conteúdo da lacuna selecionada?\n')
    if resposta_usuario.lower() == resposta.lower():
      nova_frase = nova_frase.replace(lacuna_selecionada, resposta)
      print('👍   Tim tim, você acertou!')
      return numero_tentativas, nova_frase
    else:
      print('👎   Ops, tente novamente.')
      numero_tentativas -= 1
  return numero_tentativas, frase


def inicia_jogo(dificuldade, numero_tentativas):
  """Inicia o jogo com a dificuldade informada.
  Args:
        dificuldade (int): Indice da dificuldade selecionada pelo usuário.
        numero_tentativas (int): Número de tentativas erradas que o usuário pode fazer antes de perder.
  """
  frase, respostas = obtem_frase_e_respostas(dificuldade)

  for resposta in respostas:
    numero_tentativas, frase = pergunta_resposta(frase, resposta, numero_tentativas)
    if numero_tentativas <= 0:
      print('Número de tentativas esgotado! 😣 😣 😣')
      return

  print('\n***\n\nVocê acertou tudo!   😀 😀 😀\nA frase completa é: {0}'.format(frase))

dificuldade = pergunta_dificuldade()
numero_tentativas = pergunta_numero_tentativas()
inicia_jogo(dificuldade, numero_tentativas)
