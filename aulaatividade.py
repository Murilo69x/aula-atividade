produto = {
    'id' ; 1,
    'nome' : 'teclado'
    'preco' : 150.0,
    'ativo' : true
}
    print (produto["nome"])
produto2 = {
    'id' : 2,
    'nome' : 'Mouse',
    'preco' : 80.0,
}
    print(produto2.get('ativo')) #none
    print(produto2.get('ativo', False)) #false
    produto2['ativo'] = True
    print(produto2.get('ativo'))
    #==================================================
    usuario = {'nome' : 'Murilo', 'ativo' : False}
    usuario['ativo'] = True
    usuario{'perfil'} = 'admin'}
    usuario.update({'cidade': 'Aracaju', 'idade': 18})
    print(usuario)
