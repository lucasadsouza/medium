import json, os
import nextcord
from nextcord.ext import commands


# Cria uma instância que representa nosso bot do Discord.
bot = commands.Bot()

# Estou apenas declarando algumas variáveis importantes.
settings = None
DISCORDTOKEN = None


# A função principal do nosso código, ela carrega apenas o básico para que nosso código possa funcionar plenamente.
def main():
  # Carrega as configurações do bot do arquivo settings.json
  with open('settings.json', 'r', encoding='utf-8') as f:
    settings = json.load(f)

  # Verifica se a variável settings não é nula, pois se for será lançado um RuntimeError.
  if settings:
    DISCORDTOKEN = settings['discord_token']

  else:
    raise RuntimeError('O arquivo settings.json não foi carregado.')


  # Verifica a existência das pastas contendo as classes Cog e as importa para dentro do bot.
  for folder in os.listdir('commands'):
    if os.path.exists(os.path.join('commands', folder, 'cog.py')):
      bot.load_extension(f'commands.{folder}.cog')


  # Declara uma função on_ready que será executada pelo bot quando ele estiver online e pronto para funcionar.
  @bot.event
  async def on_ready():
    print(f'{bot.user.name} está online.') # Imprime no console que o bot está online

    channel = await bot.fetch_channel(1048760235122245634) # Returna uma instância de TextChannel representando o canal que passamos o id.
    
    await channel.send('Hello World!') # Envia uma mensagem no canal que buscamos com a função acima.


  bot.run(DISCORDTOKEN) # Inicia o bot.


# Verifica se está no arquivo principal do projeto antes de executar a função main.
if __name__ == '__main__':
  main()
