import sys

import discord
import os
import time
import split_files
async def send_file(client, index, file_path):
    guild_id = 1187381937149595688  # Tutaj podaj ID serwera
    guild = client.get_guild(guild_id)
    if guild:
        try:
            with open(file_path, 'rb') as file:
                channel = guild.text_channels[index + 6]
                await channel.send(file=discord.File(file))
                print("Pomyślnie wysłano plik.")
        except FileNotFoundError:
            await channel.send("Plik nie został znaleziony.")

def increment_number_in_file(file_path):
    try:
        with open(file_path, 'r+') as file:
            number = int(file.read())
            number += 1
            file.seek(0)
            file.write(str(number))
            file.truncate()
            return number
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
        return None

def run_discord_bot():
    folder_path = 'files_ready'
    to_split_path = 'files_to_split'
    for filename in os.listdir(to_split_path):
        split_files.split_file(f'files_to_split/{filename}', to_split_path)

    sys.exit()
    TOKEN = 'MTIwOTQ5Mjk3MDY4MDYxOTAwOA.GPT_dF.hiNPwoBFhmjEyJiA5aKPAjq7Bbd1v_ylpCtePw'
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        index = increment_number_in_file("index")
        if index is not None:
            print(f'\033[91m{client.user} is now running!\033[0m')
            print("\033[92mStarting encoding operation.\033[0m")

            files = os.listdir(folder_path)
            if files:
                guild_id = 1187381937149595688  # Tutaj podaj ID serwera
                guild = client.get_guild(guild_id)
                if guild:
                    channel = guild.text_channels[index + 6]
                    await channel.send(files[0])

            start_time = time.time()

            for filename in os.listdir(folder_path):
                if os.path.isfile(os.path.join(folder_path, filename)):
                    file_path = f'files_to_split/{filename}'
                    print("Nazwa pliku:", filename)
                    await send_file(client, index, file_path)  # Zmieniono na await send_file()
                    os.remove(os.path.join(folder_path, filename))
                    print("Usunięto plik:", filename)

            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"\033[92mTime is: {elapsed_time}. Tkat means that 1gb file would be sending at speed {elapsed_time * 40}\033[0m")

        else:
            print('\033[91mError: Index is wrong. Chech index file!\033[0m')

    client.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot()

