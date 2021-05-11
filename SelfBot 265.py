print("[?] Token; ")
token = input ('> ')
print("  ")
print("[?] Prefix; ")
prefix = input ('> ')

import discord
import colorama
import requests
import os
import datetime
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred
from colorama import Fore, init
init(convert=True)

os.system('cls')
print("...")
class MyClient(discord.Client):
  async def on_connect(self):
    os.system('cls')
    print(f"""
{Fore.RED}
      ██████╗  ██████╗ ███████╗
      ╚════██╗██╔════╝ ██╔════╝
       █████╔╝███████╗ ███████╗
      ██╔═══╝ ██╔═══██╗╚════██║
      ███████╗╚██████╔╝███████║
      ╚══════╝ ╚═════╝ ╚══════╝{Fore.RESET}

------------------------------------------
[{Fore.RED}+{Fore.RESET}] Conectado com sucesso!
[{Fore.RED}-{Fore.RESET}] Não copie o codigo, isso não te faz um programador!
[{Fore.RED}!{Fore.RESET}] 265 Selfbot by Const#0007
------------------------------------------
[{Fore.RED}>{Fore.RESET}] Token: {token}
[{Fore.RED}>{Fore.RESET}] Prefix: {prefix}
------------------------------------------
""")

  async def on_message(self, message):
    if message.author != client.user:
      return
    if message.content == f"{prefix}help":
      await help(message)
    if message.content == f"{prefix}clear":
      await clear(message)
    if message.content == f"{prefix}nuke":
      await nuke(message)
    if message.content == f"{prefix}logout":
      await logout(message)

async def logout(message):
  await message.delete()
  await client.logout()
  print(f"[{Fore.RED}!{Fore.RESET}] Cliente Logado com Sucesso!")

async def help(message):
  await message.delete()
  emHelp = discord.Embed(
    description = f"""
**Commands:**
**
[-] {prefix}help
Mostrar está mensagem.

[-] {prefix}logout
Deslogar do Token e Fechar o SelfBot
 
[-] {prefix}clear
Limpa suas mensagens no canal.
 
[-] {prefix}nuke*
Destruir o servidor, Será solicitada sua confirmação no console.
**
    """)
  emHelp.set_author(name = "265", icon_url = client.user.avatar_url, url = "https://images-ext-2.discordapp.net/external/1PoDepE9qqoBi-M-B1UJs1xrtINEfOvW8ixAve4ZLoI/%3Fsize%3D2048/https/cdn.discordapp.com/icons/792333411221766174/a_7fd61f502b4cc2795ca9d7add136eca9.gif")
  emHelp.set_footer(text = "265")
  try:
    await message.channel.send(embed = emHelp, delete_after = 30)
  except:
    await message.channel.send(
      """
**Commands:**
**
[-] {prefix}help
Mostrar está mensagem.

[-] {prefix}logout
Deslogar do Token e Fechar o SelfBot
 
[-] {prefix}clear
Limpa suas mensagens no canal.
 
[-] {prefix}nuke*
Destruir o servidor, Será solicitada sua confirmação no console.
""",
     delete_after = 30
    )

async def servernuke(ctx):
    for user in ctx.guild.members:
        try:
            await user.kick()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="265",
            description="265",
            reason="265"
        )
    except:
        pass
    for _i in range(1):
        await ctx.guild.create_text_channel(name="Owned by 265 :)")
    for _i in range(1):
        await ctx.guild.create_role(name="Owned by 265 :)",)


async def nuke(message):
  await message.delete()
  if isinstance(message.channel, discord.DMChannel):
    print(f"Nuke Cancelado!\n")
    return
  elif isinstance(message.channel, discord.GroupChannel):
    print(f"Nuke Cancelado!\n")
    return
  try:
    confirmation = inputimeout(f"\n[?] Pedido de Nuke, (y/n) \n \n>", timeout = 30)
    if confirmation.lower() == "n":
      print(f"\n Nuke off\n")
      return
    elif confirmation.lower() == "y":
      print(f"\n Nuking...\n")
      member = message.guild.get_member(client.user.id)
      perms = member.guild_permissions
      if perms.manage_channels == True and perms.ban_members == True:
        await servernuke(message)
      else:
        print(f"\n[{Fore.RED}!{Fore.RESET}] Tarefa Concluida!\n")
        return
    else:
      print(f"\nNuke Cancelado!")
  except TimeoutOccurred:
    print(f"\nNuke cancelled.\n")
    return

async def clear(message):
  await message.delete()
  print(f"[{Fore.RED}-{Fore.RESET}] Deletando Mensagens do Privado...")
  async for message in message.channel.history(limit=None):
    if message.author == client.user and message.type == discord.MessageType.default:
      await message.delete()
  print(f"[{Fore.RED}!{Fore.RESET}] Tarefa Concluida: Apagar Todas Mensagens da DM!\n")


client = MyClient()
try:
  client.run(token, bot = False)
except discord.LoginFailure:
  print(f"Client failed to log in. [Invalid token]")
except discord.HTTPException:
  print(f"Client failed to log in.[Unknown Error]")

