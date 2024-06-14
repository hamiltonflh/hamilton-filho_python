def notas(*n):
  detalhes = dict()
  detalhes['notas'] = n
  detalhes['total'] = len(n)
  detalhes['media'] = sum(n)/len(n)
  detalhes['maior'] = max(n)
  detalhes['menor'] = min(n)
  return detalhes

resp = notas(2.5, 5.6, 7.8)
print(resp)

  
  
  