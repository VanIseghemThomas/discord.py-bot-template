import discord
import logging
import json

def load_commands():
    # Commands are found in commands.json
    # Load the json and convert it to a dictionary
    with open('./commands.json') as json_file:
        try:
            commands = json.load(json_file)
            logging.info('Loaded commands from json')
            return commands
        except:
            logging.error('Error loading commands.json, check if it is available or valid!')
            return {}

def generate_command_embed(command_dict, prefix):
    # Generate a command embed
    embed = discord.Embed(
        title='Commands',
        description='A list of all commands',
        color=0x00ff00
    )

    for command in command_dict:
        if 'description' in list(command.keys()):
            embed.add_field(
                name= prefix + command['command'],
                value=command['description'],
                inline=False
            )
        else:
            embed.add_field(
                name= prefix + command['command'],
                value="\u200b",
                inline=True
            )

    return embed