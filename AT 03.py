#DICIONARIO - ATIVIDADE 03

alunos= {
     'Ana' : 8.5 ,
    'Pedro' :7.0 ,
    'Maria' : 9.2
}

alunos['Carlos'] = 6.5
alunos['Ana'] = 9.0

del alunos ['Pedro']

somanotas = sum(alunos.values())
quantidadealunos = len(alunos)
media = somanotas / quantidadealunos
print ( 'A media dos alunos: ' , round(media, 2 ))

if 'Maria' in alunos:
  print('Maria esta presente no dicionario.')
else:
  print ('Maria nao esta no dicionario .')

  print('\nDicionario de alunos e suas notas: ')
  print(alunos) 

