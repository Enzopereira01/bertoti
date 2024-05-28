import telebot
import random
import os 
from typing import Dict, KeysView

TOKEN = "6487234556:AAGJgiyTM2yfm34xwv5SiHHHurYdrihSOWQ"

bot = telebot.TeleBot(TOKEN)


class ReceitasDict(dict):
    def keys(self) -> KeysView[str]:
        return super().keys()
    
lista_receitas_comidas = ReceitasDict()

lista_receitas_drinks = ReceitasDict()

lista_receitas_comidas.update({
       # Receitas de comidas
    "Frango ao Curry com Leite de Coco\n\n"
    "Ingredientes: peito de frango, leite de coco, curry em pó, cebola, alho, gengibre, pimenta e sal.\n\n"
    "Modo de preparo: Refogue cebola, alho e gengibre, adicione o frango cortado em cubos, depois acrescente o leite de coco e o curry em pó. Cozinhe até o frango ficar macio e o molho engrossar.":"",

    "Salada de Quinoa com Vegetais Assados\n\n"
    "Ingredientes: quinoa, abobrinha, pimentão, cebola roxa, azeite, limão, sal e pimenta.\n\n"    
    "Modo de preparo: Cozinhe a quinoa e reserve. Corte os vegetais em pedaços, tempere com azeite, sal e pimenta, asse no forno até dourar. Misture os vegetais assados com a quinoa cozida e regue com suco de limão.":"",

    "Salmão Grelhado com Molho de Ervas\n\n"
    "Ingredientes: filés de salmão, azeite, limão, salsa, coentro, cebolinha, sal e pimenta.\n\n"
    "Modo de preparo: Tempere os filés de salmão com sal, pimenta e suco de limão. Grelhe os filés em uma frigideira com um pouco de azeite. Para o molho, misture as ervas picadas com azeite, sal e limão e sirva sobre o salmão.":"",

    "Ratatouille\n\n"
    "Ingredientes: berinjela, abobrinha, tomate, cebola, alho, azeite, tomilho, sal e pimenta.\n\n"
    "Modo de preparo: Corte os legumes em rodelas. Refogue a cebola e o alho em azeite, adicione os legumes em camadas, tempere com sal, pimenta e tomilho. Cozinhe em fogo baixo até os legumes ficarem macios.":"",

    "Tacos de Lentilha com Guacamole\n\n"
    "Ingredientes para os tacos: tortilhas de milho, lentilha cozida, alface, tomate, queijo, coentro.\n\n"
    "Ingredientes para o guacamole: abacate, tomate, cebola roxa, coentro, limão, sal e pimenta.\n\n"
    "Modo de preparo: Monte os tacos com lentilha, alface, tomate e queijo. Para o guacamole, amasse o abacate, misture os outros ingredientes e tempere a gosto.":"",

    "Espaguete de Abobrinha com Molho Pesto\n\n"
    "Ingredientes: abobrinhas, manjericão, nozes, queijo parmesão, alho, azeite, sal e pimenta.\n\n"
    "Modo de preparo: Use um descascador para fazer tiras finas de abobrinha, refogue rapidamente em azeite. Para o molho pesto, bata manjericão, nozes, queijo parmesão, alho e azeite no liquidificador até ficar homogêneo. Misture com as espaguetes de abobrinha.":"",

    "Sopa de Lentilha com Legumes\n\n"
    "Ingredientes: lentilhas, cenoura, batata, cebola, alho, aipo, tomate, caldo de legumes, azeite, sal e pimenta.\n\n"
    "Modo de preparo: Refogue a cebola, o alho e o aipo em azeite, adicione os legumes cortados em cubos, as lentilhas e o caldo de legumes. Cozinhe até que todos os ingredientes estejam macios.":"",

    "Torta de Espinafre e Queijo Feta\n\n"
    "Ingredientes para a massa: farinha de trigo, manteiga, água, sal.\n\n"
    "Ingredientes para o recheio: espinafre, queijo feta, cebola, alho, azeite, sal e pimenta.\n"
    "Modo de preparo: Faça a massa da torta e reserve. Refogue a cebola e o alho em azeite, adicione o espinafre picado, tempere com sal e pimenta. Montagem: forre uma forma com a massa, coloque o recheio por cima e cubra com queijo feta esfarelado. Asse no forno até dourar.":"",

    "Salada de Batata com Mostarda e Endro\n\n"
    "Ingredientes: batatas, cebola roxa, endro fresco, mostarda dijon, azeite, vinagre de maçã, sal e pimenta.\n\n"
    "Modo de preparo: Cozinhe as batatas em água com sal até ficarem macias. Escorra e deixe esfriar. Misture a mostarda, o endro picado, o azeite e o vinagre em uma tigela. Adicione as batatas e a cebola roxa fatiada, misture bem e tempere com sal e pimenta.":"",

    "Sobremesa de Pudim de Chia com Frutas Vermelhas\n\n"
    "Ingredientes: leite de coco, sementes de chia, mel ou adoçante a gosto, frutas vermelhas frescas.\n\n"
    "Modo de preparo: Misture o leite de coco com as sementes de chia e o adoçante. Deixe descansar na geladeira por algumas horas ou durante a noite. Sirva com frutas vermelhas frescas por cima.":""
})

lista_receitas_drinks.update({
        # Receitas para drinks
    "Mojito:\n\n"
    "Ingredientes: Rum branco, hortelã, açúcar, suco de limão, água com gás.\n\n"
    "Modo de preparo: Macere folhas de hortelã com açúcar e suco de limão, adicione rum e gelo, complete com água com gás.":"",

    "Blue Lagoon:\n\n"
    "Ingredientes: Vodka, Blue Curaçao, limonada.\n\n"
    "Modo de preparo: Em um copo com gelo, adicione vodka e Blue Curaçao, complete com limonada.":"",

    "Martini Clássico:\n\n"
    "Ingredientes: Gin, vermute seco, azeitona.\n\n"
    "Modo de preparo: Misture gin e vermute com gelo, coe em uma taça e decore com uma azeitona.":"",

    "Sangria:\n\n"
    "Ingredientes: Vinho tinto, frutas (laranja, maçã, limão), açúcar, club soda.\n\n"
    "Modo de preparo: Misture todos os ingredientes em uma jarra e deixe na geladeira por algumas horas antes de servir.":"",

    "Daiquiri:\n\n"
    "Ingredientes: Rum branco, suco de limão, xarope simples.\n\n"
    "Modo de preparo: Agite os ingredientes com gelo e coe em uma taça.":"",

    "Gin Tônica:\n\n"
    "Ingredientes: Gin, água tônica, limão.\n\n"
    "Modo de preparo: Em um copo com gelo, adicione gin e água tônica, finalize com uma fatia de limão.":"",

    "Margarita:\n\n"
    "Ingredientes: Tequila, licor de laranja, suco de limão, sal.\n\n"
    "Modo de preparo: Agite os ingredientes com gelo, sirva em uma taça previamente salgada.":"",

    "Cosmopolitan:\n\n"
    "Ingredientes: Vodka, licor de laranja, suco de cranberry, suco de limão.\n\n"
    "Modo de preparo: Agite todos os ingredientes com gelo e coe em uma taça de martini.":"",

    "Piña Colada:\n\n"
    "Ingredientes: Rum branco, suco de abacaxi, leite de coco, gelo.\n\n"
    "Modo de preparo: Bata todos os ingredientes no liquidificador com gelo até ficar homogêneo.":"",

    "Caipirinha:\n\n"
    "Ingredientes: Cachaça, limão, açúcar.\n\n"
    "Modo de preparo: Macere limão com açúcar, adicione cachaça e gelo, misture bem.":""
})

receita_atual_drinks = None

receita_atual_comidas = None

# Função para iniciar o menu
@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    boas_vindas = "Bem-vindo ao Bot de Perguntas receitas!\n\n" \
                  "O Bot possui alguns conhecimentos sobre receita."\
                  "Para começar, use o comando /receita.\n\n" \
                  "Aqui estão alguns comandos disponíveis:\n" \
                  "/receita - Para conseguir visualizar uma receita em questão de forma simples.\n" \
                  "/drinks - Para conseguir visualizar algumas receitas de algumas bebidas."

    bot.send_message(chat_id, boas_vindas)

# Função para mostrar uma receita de comidas
@bot.message_handler(commands=['receita'])
def handle_text(message):
    chat_id = message.chat.id
    receita_atual_comidas = random.choice(list(lista_receitas_comidas.keys()))
    bot.send_message(chat_id, receita_atual_comidas)

# Função para mostrar uma receita de comidas
@bot.message_handler(commands=['drinks'])
def handle_text(message):
    chat_id = message.chat.id
    receita_atual_drinks = random.choice(list(lista_receitas_drinks.keys()))
    bot.send_message(chat_id, receita_atual_drinks)

# Inicialização do bot
bot.polling()