from . import products_bp
from flask import request, render_template, url_for, redirect, flash
from database import Session
from models.user import User
from models.products import Product
from flask_login import login_required, current_user

# Dashboard com listagem e criação de produtos
@products_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    db = Session()

    # Se o usuário enviou o formulário, cria a produto
    if request.method == 'POST':
        nome_produto = request.form['nome_produto']
        preco_produto = request.form['preco_produto']
        descricao = request.form['descricao']
        nova_produto = Product(nome=nome_produto, descricao=descricao, preco=preco_produto, id_usuario=current_user.id)
        db.add(nova_produto)
        db.commit()
        flash('Product adicionada com sucesso!')

    # Lista as produtos do usuário logado
    produtos = db.query(Product).filter_by(id_usuario=current_user.id).all()
    db.close()

    return render_template('dashboard.html', usuario=current_user.nome, produtos=produtos)

@products_bp.route('/remover_produto/<int:id_produto>', methods=['POST'])
@login_required
def remover_produto(id_produto):
    db = Session()
    produto = db.query(Product).filter_by(id=id_produto, id_usuario=current_user.id).first()
    if produto:
        db.delete(produto)
        db.commit()
        flash('Product removido com sucesso!')
    db.close()
    return redirect(url_for('products.dashboard'))


# ROTA PARA EDITAR produto
@products_bp.route('/editar_produto/<int:id_produto>', methods=['POST'])
@login_required
def editar_produto(id_produto):
    db = Session()
    produto = db.query(Product).filter_by(id=id_produto, id_usuario=current_user.id).first()
    if produto:
        novo_produto = request.form['novo_produto']
        produto.nome = novo_produto
        db.commit()
        flash('Product atualizado com sucesso!')
    db.close()
    return redirect(url_for('products.dashboard'))

