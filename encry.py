from py_adyen_encrypt import encryptor

ADYEN_KEY = "10001|D31156DAF03E256CF3280AEEC87DDD006B6069F8672E1B2A45AE080B53F51CD118EA89C96F4278FF5AAA22C6A83C4A61AB70E9E7A38300A9684B7D1A2EE3DE2C2AD0D3CCE48FA74441D128C928D01AED520F9EA165D7538B79EEE4BEAD41D7291CFDEE01A2A5A99F6E6DBAD232071BFDD6CD1C7BB8252386743E8260AC4B09B2D742A8259C26BC45C3BB5D069495640A23DEF2C8C25ED6686EFF7B6C79B38FB19963583C7E40908C6806FEBA3B1E56B4B79ACA9648DF13F1215E9B469DA0F6B2F29EAD01EB10C205FA4C836396DC710D3BE40DAA01EB90C6B6ED5E91AF7B5A0759C9613C876D0DB035F3915EF7D5716CA88EF22CE923658F62F67EDABDA71C63"

# Função para processar um único cartão
def processar_cartao(cartao, cvv, mes, ano):
    enc = encryptor(ADYEN_KEY)
    enc.adyen_version = '_0_1_25'

    card = enc.encrypt_card(card=cartao, cvv=cvv, month=mes, year=ano)
    print(card)

# Função para processar a lista de cartões
def processar_lista_cartoes(lista_cartoes):
    for linha in lista_cartoes:
        dados_cartao = linha.split("|")
        if len(dados_cartao) == 4:
            cartao, cvv, mes, ano = dados_cartao
            processar_cartao(cartao, cvv, mes, ano)
        else:
            print("Erro: Formato de dados do cartão inválido")

# Exemplo de uso com uma lista de cartões
lista = input('Digite a lista de cartões (formato: cartao|cvv|mes|ano separados por vírgula): ')
dados_cartoes = lista.split(",")

processar_lista_cartoes(dados_cartoes)
