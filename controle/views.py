from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto, Movimentacao

def lista_produtos(request):
    produtos = Produto.objects.all().order_by('nome')
    return render(request, 'controle/lista_produtos.html', {'produtos': produtos})

def cria_produto(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria', '')
        estoque_minimo = request.POST.get('estoque_minimo', 0)

        if not codigo or not nome:
            contexto = {'erro': 'Código e nome são obrigatórios.'}
            return render(request, 'controle/cria_produto.html', contexto)

        Produto.objects.create(
            codigo=codigo,
            nome=nome,
            categoria=categoria,
            estoque_minimo=estoque_minimo or 0
        )
        return redirect('lista_produtos')

    return render(request, 'controle/cria_produto.html')


def registra_movimentacao(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        quantidade = int(request.POST.get('quantidade', 0))
        observacao = request.POST.get('observacao', '')

        if quantidade <= 0:
            messages.error(request, 'A quantidade deve ser maior que zero.')
            return redirect('registra_movimentacao', produto_id=produto.id)

        # regra de negócio: não permitir saída maior que o estoque atual
        if tipo == 'S' and quantidade > produto.quantidade_atual:
            messages.error(request, 'Quantidade de saída maior que o estoque atual.')
            return redirect('registra_movimentacao', produto_id=produto.id)

        # cria a movimentação
        Movimentacao.objects.create(
            produto=produto,
            tipo=tipo,
            quantidade=quantidade,
            observacao=observacao
        )

        # atualiza o saldo
        if tipo == 'E':
            produto.quantidade_atual += quantidade
        else:
            produto.quantidade_atual -= quantidade
        produto.save()

        messages.success(request, 'Movimentação registrada com sucesso.')
        return redirect('lista_produtos')

    return render(request, 'controle/registra_movimentacao.html', {'produto': produto})
