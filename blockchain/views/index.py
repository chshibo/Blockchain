"""
blockchain index view

Created by Shibo Chen, Data:1/26/2018
University of Michigan, class of 2019
email: chshibo@umich.edu
"""
import flask
from flask import request
import blockchain
from blockchain.views.blockchain_functionality.block_chain import Blockchain
from blockchain.views.blockchain_functionality.block import Block
from blockchain.views.blockchain_functionality.transaction import Transaction


def construct_block_dictionary(index=-1):
    """
    Contruct a dictionary for block at index in chain

    Parameters
    ----------
    index : Int (default : -1 (last block))
        Index of which you want to contruct a dictionary

    Returns
    -------
    block_dict : {}
        A dictionary for block at index in chain
    """
    block = Blockchain.get_block(index)
    block_dict = {}
    block_dict['identity'] = block.identity
    block_dict['timestamp'] = block.timestamp
    block_dict['proof'] = block.proof
    block_dict['previous_block_hash'] = block.previous_block_hash
    block_dict['transactions'] = []
    for transaction in block.transactions:
        transaction_dict = {}
        transaction_dict['sender'] = transaction.sender
        transaction_dict['receiver'] = transaction.receiver
        transaction_dict['value'] = transaction.value
        block_dict['transactions'].append(transaction_dict)
    return block_dict

@blockchain.app.route('/')
def show_personal_page():
    """redirect to personal page"""
    return flask.redirect("http://www-personal.umich.edu/~chshibo/")

@blockchain.app.route('/blockchain/')
def show_blockchain():
    """show indext page of api"""
    context = {}
    return flask.render_template("index.html", **context)

@blockchain.app.route('/blockchain/mine', methods=['GET', 'POST'])
def mine():
    """Mine a block"""
    context = {}
    context['show'] = 0
    Blockchain.create_block()
    if request.method == 'POST':
        context['show'] = 1
        context['difficulty'] = blockchain.app.config['DIFFICULTY']
        context['block'] = construct_block_dictionary()
    return flask.render_template("mine.html", **context)

@blockchain.app.route('/blockchain/transactions/new/', methods=['GET', 'POST'])
def new_transactions():
    """Create a new transaction"""
    context = {}
    context['show'] = 0
    if request.method == 'POST':
        context['show'] = 1
        context['difficulty'] = blockchain.app.config['DIFFICULTY']
        sender = request.form['sender']
        receiver = request.form['receiver']
        value = request.form['value']
        Blockchain.create_transaction(sender, receiver, value)
        lastIndex = Blockchain.get_block(-1).identity
        context['block'] = construct_block_dictionary(lastIndex)

    return flask.render_template("transaction_new.html", **context)

@blockchain.app.route('/blockchain/chain/')
def show_chain():
    """Show current blocks on chain"""
    context = {}
    context['difficulty'] = blockchain.app.config['DIFFICULTY']
    context['blocks'] = []
    for i in range(0, Blockchain.get_block(-1).identity+1):
        context['blocks'].append(construct_block_dictionary(i))
    return flask.render_template("chain.html", **context)
