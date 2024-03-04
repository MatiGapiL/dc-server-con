import discord
import os

async def join_files(client, index):
    print("Starting Joining files")
    guild_id = 1187381937149595688  # ID twojego serwera Discord
    guild = client.get_guild(guild_id)
    if guild:
        channel_index = index % 400 + 6
        channel = guild.text_channels[channel_index]
        messages = [msg async for msg in channel.history(limit=None)]  # Użyj listy składanej

        files_to_rejoin = []

        # Szukanie wiadomości startowej
        start_message = None
        for message in messages:
            if message.content == str(index):
                start_message = message
                break

        # Jeśli znaleziono wiadomość startową
        if start_message:
            # Przechodzenie przez wiadomości od wiadomości startowej
            for message in messages[messages.index(start_message) + 1:]:
                # Jeśli wiadomość jest tekstem, którym jest index, to przerywamy
                if message.content == str(index):
                    break
                # Jeśli wiadomość zawiera załącznik
                if message.attachments:
                    for attachment in message.attachments:
                        # Pobieranie załącznika
                        file_path = f'files_to_rejoin/{attachment.filename}'
                        await attachment.save(file_path)
                        files_to_rejoin.append(file_path)

        # Po zebraniu wszystkich plików łączymy je w jeden plik
        output_file_path = f'files_ready_to_dw/{start_message.content}.txt'
        with open(output_file_path, 'wb') as output_file:
            for file_path in files_to_rejoin:
                with open(file_path, 'rb') as file:
                    output_file.write(file.read())
                # Usunięcie pliku po połączeniu
                os.remove(file_path)

        print(f"Pomyślnie połączono pliki i zapisano jako {output_file_path}")

    else:
        print("Nie można połączyć z serwerem Discord.")
    sys.exit()


# Przykład użycia:
def run_it():
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("Hej")
        await join_files(client, 407)  # Przykładowy index

    client.run('MTIwOTQ5Mjk3MDY4MDYxOTAwOA.GPT_dF.hiNPwoBFhmjEyJiA5aKPAjq7Bbd1v_ylpCtePw')

if __name__ == '__main__':
    run_it()
