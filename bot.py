import discord
import responses
import privateKey


def run_discord_bot():
    TOKEN = privateKey.TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)



    @client.event
    async def on_ready():
        print(f'{client.user} is now running')



    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f" {username} said : '{user_message}' ({channel}")

        if user_message[0] == '?':
            print('entered ?')
            user_message = user_message[1:]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)


    async def send_message(message, user_message, is_private):
        emojis = {
            0: ':white_small_square:',
            1: discord.utils.get(client.emojis, name="2048_2"),
            2: discord.utils.get(client.emojis, name="2048_4"),
            3: discord.utils.get(client.emojis, name="2048_8"),
            4: discord.utils.get(client.emojis, name="2048_16"),
            5: discord.utils.get(client.emojis, name="2048_32"),
            6: discord.utils.get(client.emojis, name="2048_64"),
            7: discord.utils.get(client.emojis, name="2048_128"),
            8: discord.utils.get(client.emojis, name="2048_256"),
            9: discord.utils.get(client.emojis, name="2048_512"),
            10: discord.utils.get(client.emojis, name="2048_1024"),
            11: discord.utils.get(client.emojis, name="2048_2048"),
            12: "nah"
        }
        try:
            response = responses.handle_response(message, emojis)
            if len(response) < 50:
                print("Response:", response)  # Debug output
            if is_private:
                await message.channel.send(str(emojis[1]) * 30)
            else:
                await message.channel.send(response)
        except Exception as e:
            print("Error:", e)  # Debug output

        except Exception as e:
            print(e)



    client.run(TOKEN)
