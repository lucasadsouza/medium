import nextcord
from nextcord.ext import commands


# Declara uma clase que herda de Cog e será passada para o bot posteriormente.
class PingCog(commands.Cog, name='Ping'):
  def __init__(self, bot: commands.Bot):
    self.bot = bot # O bot passa a sí próprio por padrão por isso é importante adicionarmos ele aqui.

  @nextcord.slash_command(guild_ids=[1048760234656665710]) # Ao passar qualquer id ao guild_ids estamos solicitando que seja registrada apenas nesse servidor.
  async def ping(self, interaction: nextcord.Interaction): # Uma Slash Command recebe por padrão uma interaction.
    await interaction.response.defer() # Indica ao Discord que irá executar alguma coisa e posteriormente fornecer uma resposta.
    await interaction.followup.send('Pong!') # Fornece a resposta esperada pelo Discord, no caso, um texto.


# É obrigatória para que uma classe Cog funcione, ela é responsável por adicionar a Cog ao bot e também passar os parametros necessários.
def setup(bot: commands.Bot):
  bot.add_cog(PingCog(bot))
