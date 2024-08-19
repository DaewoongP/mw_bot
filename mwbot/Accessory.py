import All
import discord
import random
import MyToken
import json


def UpdateJson(new_user_data):
    with open('grinddata.json', 'r', encoding='utf-8') as f:
        my_data = json.load(f)
        
    is_new = True
    for user in my_data['users']:
        if user['name'] == new_user_data['name']:
            user.update(new_user_data)
            is_new = False
            break
    if is_new:
        my_data['users'].append(new_user_data)
        
    with open('grinddata.json', 'w', encoding='utf-8') as f:
        json.dump(my_data, f, ensure_ascii=False, indent=4)


class SelectMenu(discord.ui.Select):
    def __init__(self, ctx, user_data):
        self.ctx = ctx
        self.user_data = user_data
        super().__init__(
            placeholder = f"{ctx.author.display_name} : 연마할 악세를 선택해주세요.", 
            options=[
                discord.SelectOption(label="목걸이", description="현재는 테스트 기능입니다."),
                # discord.SelectOption(label="귀걸이 1"),
                # discord.SelectOption(label="귀걸이 2"),
                # discord.SelectOption(label="반지 1"),
                # discord.SelectOption(label="반지 2")
            ])
        
    async def callback(self, interaction: discord.Interaction):
        # self.values를 통해 선택한 옵션 label을 리스트형태로 가져온다.
        if interaction.user.id == self.ctx.author.id:
            for selected_value in self.values:
                if selected_value == "목걸이":
                    await interaction.response.send_message(
                        " ",
                        view=CheckCountButton(self.ctx, self.user_data, 'necklace'),
                        ephemeral=True
                    )

class Select(discord.ui.View):
    def __init__(self, ctx, user_data):
        super().__init__()
        self.add_item(SelectMenu(ctx, user_data))


class CheckCountButton(discord.ui.View):
    def __init__(self, ctx, user_data, item_name):
        super().__init__()
        self.ctx = ctx
        self.user_data = user_data
        self.item_name = item_name

    @discord.ui.button(label="연마", style=discord.ButtonStyle.primary, custom_id="grind")
    async def grind_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        option_fullname, option_value, option_color = All.get_random_option(All.necklace_list, self.user_data['necklace'][0]['option'], self.user_data['necklace'][1]['option'])
        
        option_name = option_fullname[:-2]
        option_style = option_fullname[-1:]

        embed = discord.Embed(
            #title=f"{option_name} {option_value}{option_style}",
            color=option_color
        )
        
        embed.add_field(name=f"{option_name}", value=f"{option_value}{option_style}")
    
        await interaction.response.send_message(embed=embed)
        
        is_updated = False
        for data in self.user_data[self.item_name]:
            if data['option'] == 'x':
                data['option'] = option_fullname
                data['value'] = option_value
                is_updated = True
                break
            
        if is_updated == False:
            self.user_data[self.item_name][0]['option'] = option_fullname
            self.user_data[self.item_name][0]['value'] = option_value
            self.user_data[self.item_name][1]['option'] = 'x'
            self.user_data[self.item_name][1]['value'] = 0
            self.user_data[self.item_name][2]['option'] = 'x'
            self.user_data[self.item_name][2]['value'] = 0
                
        UpdateJson(self.user_data)
        
        embed = discord.Embed(
            title="연마 성공 !!",
            color=0x000000
        )
        embed.set_footer(text=f"{self.ctx.author.display_name}", icon_url=self.ctx.author.avatar.url)
        embed.add_field(name="목걸이", value=f"{self.user_data['necklace'][0]['option']}\n{self.user_data['necklace'][0]['value']}\n", inline=True)
        embed.add_field(name="ㅤㅤㅤ", value=f"{self.user_data['necklace'][1]['option']}\n{self.user_data['necklace'][1]['value']}\n", inline=True)
        embed.add_field(name="ㅤㅤㅤ", value=f"{self.user_data['necklace'][2]['option']}\n{self.user_data['necklace'][2]['value']}\n", inline=True)
        await self.ctx.send(embed=embed)
        await self.ctx.send("==============================")


    # @discord.ui.button(label="전부 연마", style=discord.ButtonStyle.success, custom_id="all_grind")
    # async def grind_button_all(self, interaction: discord.Interaction, button: discord.ui.Button):
    #     option_fullname, option_value, option_color = All.get_random_option(All.necklace_list)
        
    #     option_name = option_fullname[:-2]
    #     option_style = option_fullname[-1:]
        
    #     embed = discord.Embed(
    #         title=f"{option_name} {option_value}{option_style}",
    #         color=option_color
    #     )
    
    #     await interaction.response.send_message(embed=embed)

def start(client, commands, discord, channel_id):
    # 악세 연마
    @client.hybrid_command(name="연마", with_app_command=True, description="로스트아크 악세 연마를 진행합니다.")
    async def command_grinding(ctx: commands.Context):
        with open('grinddata.json', 'r', encoding='utf-8') as f:
            grind_data = json.load(f)
            
        is_new = True
        user_data = dict()
        
        for user in grind_data['users']:
            if user['id'] == ctx.author.id:
                user_data = user
                is_new = False
                break

        
        if is_new:
            user_data = {
                "name": ctx.author.name,
                "id": ctx.author.id,
                "necklace": [
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    }
                ],
                "earring1": [
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    }
                ],
                "earring2": [
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    }
                ],
                "ring1": [
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    }
                ],
                "ring2": [
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    },
                    {
                        "option": "x",
                        "value": 0
                    }
                ]
            }
            
            grind_data['users'].append(user_data)

        embed = discord.Embed(
            title="현재 악세 연마 현황",
            color=0xFFFFFF
        )
        embed.set_footer(text=f"{ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        embed.add_field(name="목걸이", value=f"{user_data['necklace'][0]['option']}\n{user_data['necklace'][0]['value']}\n", inline=True)
        embed.add_field(name="ㅤㅤㅤ", value=f"{user_data['necklace'][1]['option']}\n{user_data['necklace'][1]['value']}\n", inline=True)
        embed.add_field(name="ㅤㅤㅤ", value=f"{user_data['necklace'][2]['option']}\n{user_data['necklace'][2]['value']}\n", inline=True)
        await ctx.send(embed=embed)
        
        # ---------------------------------

        send_messsage = await ctx.reply(view=Select(ctx, user_data))
        
        # ---------------------------------

        # if ctx.clean_prefix == "!":
        #     await ctx.message.delete()