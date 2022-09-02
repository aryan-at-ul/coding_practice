


class Node:

    def __init__(self, prob, symbol,left = None, right = None):
        self.prob = prob
        self.left = left 
        self.right = right 
        self.symbol = symbol 
        self.code = ''


def calculate_probs(data):
    symbol = dict()
    for symb in data:
        if symb not in symbol.keys():
            symbol[symb] = 1
        else:
            symbol[symb] += 1 


    return symbol


s = "AAAAAAAABBBBBBBBBCDEEFFF"

print(calculate_probs(s))


codes = dict()

def assign_code_to_node(huff_tree, val = ''):

    code =  val + str(huff_tree.code)

    if huff_tree.left:
        assign_code_to_node(huff_tree.left,code)
    if huff_tree.right:
        assign_code_to_node(huff_tree.right,code)
    
    if not huff_tree.left and not huff_tree.right:
        codes[huff_tree.symbol] = code

    return codes

def output_enc_str(data,codes):
    out = []
    for one in data:
        out.append(codes[one])
    return ''.join(out)



def huffman_encode(data):

    symbol_prob = calculate_probs(data)
    symbols = symbol_prob.keys()
    probs = symbol_prob.values()

    nodes = [Node(symbol_prob[symb],symb) for symb in symbols]

    while len(nodes) > 1:

        nodes = sorted(nodes, key = lambda x: x.prob)

        right = nodes[0]
        left  = nodes[1]

        right.code = 1
        left.code = 0 

        newNode = Node(left.prob + right.prob , left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_enc = assign_code_to_node(nodes[0])
    # print(huffman_enc)
    enc_str = output_enc_str(data,codes)
    return huffman_enc,enc_str

print(huffman_encode(s))


    









