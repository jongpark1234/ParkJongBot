import discord
from ObjectInfo.Mob import *
from ObjectInfo.weapon import *
from ObjectInfo.armor import *
from Database.bgm import *
from Database.map import *
from Database.emoji import *
from Database.mapnum import *
from config import TOKEN
from discord.utils import get
from discord.message import implement_partial_methods
from discord.ext import commands
import random
import asyncio
import glob
import pickle
import math
import datetime

bot = commands.Bot(command_prefix="!")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot Affected")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!도움말"))
weapondamage = {}  # 현재 무기가 부여하는 공격력
leveldamage = {}  # 레벨에 따라 증가하는 공격력
weaponnumber = {}  # 무기가 가진 고유번호
weaponname = {}  # 무기가 가진 고유 이름

armornumber = {} # 방어구가 가진 고유번호
armorname = {} # 방어구가 가진 고유 이름
armordefense = {} # 현재 방어구가 부여하는 방어력

weaponcritchance = {} # 무기가 가진 크리티컬 확률
weaponcritdamage = {} # 무기가 가진 크리티컬 데미지

armorcritchance = {} # 방어구가 가진 크리티컬 확률
armorcritdamage = {} # 방어구가 가진 크리티컬 데미지

critical_chance = {} # 플레이어의 크리티컬 확률
critical_damage = {} # 플레이어의 크리티컬 데미지

exp = {}  # 현재 플레이어의 경험치
maxexp = {}  # 해당 레벨의 경험치 상한선
damage = {} # 웨폰데미지 + 레벨데미지 + 증가퍼센트를 합산한 최종 데미지
maxhp = {} # 자신의 최대 체력
hp = {} # 자신의 현재 체력
level = {}  # 플레이어의 레벨
meso = {}  # 플레이어의 보유골드
potioncount = {} # 플레이어의 포션 카운트

mobdamage = {} # 해당 몬스터의 공격력
mobmaxhp = {}  # 해당 몬스터의 원래 체력
mobhp = {} # 해당 몬스터의 현재 체력
mobexp = {}  # 해당 몬스터의 경험치
mobname = {} # 해당 몬스터의 이름
mobmeso = {} # 해당 몬스터의 골드
mobworld = {} # 해당 몬스터의 소속 지역명
mobicon = {} # 해당 몬스터의 소속 지역 아이콘
mobimg = {} # 해당 몬스터의 이미지

mapnum = {} # 해당 맵의 고유번호
battle = {} # 전투 중인지 여부

@bot.command()
async def 정보등록(ctx):
    try:
        mapnum[ctx.author.id] += 0
        await ctx.send(embed=discord.Embed(title='이미 등록된 회원 정보입니다.'))
    except KeyError:
        leveldamage[ctx.author.id] = levelupInfo[0][2]  # 레벨이 부여하는 공격력
        weapondamage[ctx.author.id] = w0.damage  # 현재 무기가 부여하는 공격력
        weaponnumber[ctx.author.id] = w0.number  # 무기가 가진 고유번호
        weaponname[ctx.author.id] = w0.name  # 무기가 가진 고유 이름 

        armordefense[ctx.author.id] = a0.defense # 현재 방어구가 부여하는 방어력
        armornumber[ctx.author.id] = a0.number # 방어구가 가진 고유번호
        armorname[ctx.author.id] = a0.name # 방어구가 가진 고유 이름

        weaponcritchance[ctx.author.id] = w0.c_chance # 현재 무기가 부여하는 크리티컬 확률
        weaponcritdamage[ctx.author.id] = w0.c_damage # 현재 무기가 부여하는 크리티컬 데미지

        armorcritchance[ctx.author.id] = a0.c_chance # 현재 방어구가 부여하는 크리티컬 확률
        armorcritdamage[ctx.author.id] = a0.c_damage # 현재 방어구가 부여하는 크리티컬 데미지

        critical_chance[ctx.author.id] = min(100, weaponcritchance[ctx.author.id] + armorcritchance[ctx.author.id]) # 현재 플레이어의 크리티컬 확률 ( weaponcritchance + armorcritchance )
        critical_damage[ctx.author.id] = weaponcritdamage[ctx.author.id] + armorcritdamage[ctx.author.id] # 현재 플레이어의 크리티컬 데미지 ( weaponcritdamage + armorcritdamage )

        exp[ctx.author.id] = 0  # 현재 플레이어의 경험치
        maxexp[ctx.author.id] = levelupInfo[0][0]  # 해당 레벨의 경험치 상한선
        damage[ctx.author.id] = weapondamage[ctx.author.id] + leveldamage[ctx.author.id] # 웨폰데미지 + 레벨데미지 + 증가퍼센트를 합산한 최종 데미지
        maxhp[ctx.author.id] = 100 # 자신의 최대 체력
        hp[ctx.author.id] = 100 # 자신의 현재 체력
        level[ctx.author.id] = 1  # 플레이어의 레벨
        meso[ctx.author.id] = 1000  # 플레이어의 보유메소
        potioncount[ctx.author.id] = 0 # 플레이어의 포션 카운트

        mobdamage[ctx.author.id] = 1 # 해당 몬스터의 공격력
        mobmaxhp[ctx.author.id] = 1  # 해당 몬스터의 최대 체력
        mobhp[ctx.author.id] = 1 # 해당 몬스터의 현재 체력
        mobexp[ctx.author.id] = 141  # 해당 몬스터의 경험치
        mobname[ctx.author.id] = "강원기" # 해당 몬스터의 이름
        mobmeso[ctx.author.id] = 141 # 해당 몬스터의 메소
        mobworld[ctx.author.id] = "메이플 월드" # 해당 몬스터의 소속 지역명
        mobicon[ctx.author.id] = icon_maple_world # 해당 몬스터의 소속 지역 아이콘
        mobimg[ctx.author.id] = "Null" # 해당 몬스터의 이미지

        mapnum[ctx.author.id] = 13 # 해당 맵의 고유번호
        battle[ctx.author.id] = False # 전투 중인지 여부

        await ctx.send(embed=discord.Embed(title='서버에 정보가 등록되었습니다.', description=f'{len(exp)}번째 유저 {ctx.author.nick}님을 환영합니다.'))

@bot.command()
async def 청소(ctx):
    await ctx.send("." + '\n' * 100 + '.')

@bot.command()
async def 버그수정(ctx):
    battle[ctx.author.id] = False
    await ctx.send('전투 모드가 비활성화 되었습니다.')


@bot.command()
async def 도움말(ctx):
    embed=discord.Embed(title="도움말", description="Made by JongPark#0001", color=0xeeff00)
    embed.add_field(name="!정보등록", value="자신의 정보를 등록합니다. 봇을 사용하기 위해 필수로 입력해야 합니다.", inline=False)
    embed.add_field(name="!인벤토리", value="자신의 정보, 스테이터스와 보유장비를 확인할 수 있습니다.", inline=False)
    embed.add_field(name="!월드맵", value="월드맵 창을 띄웁니다. 이모지를 이용하여 이동할 수 있습니다.", inline=False)
    embed.add_field(name="!사냥", value="지역에 따라 다르게 나오는 적을 사냥할 수 있습니다.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 무기상점(ctx, index: int): # 이름(w.name), 번호(w.number), 요구메소(w.meso), 공격력(w.damage), 치명타 확률(w.c_chance), 치명타 데미지(w.c_damage)
    try:
        if index in range(1, 2): # 설정된 인덱스를 벗어나지 않았을 경우
            embed=discord.Embed(title="무기상점", description=f"{index} 페이지", color=0xf99090)
            for i in range(1, 11):
                idx = (index - 1) * 10 + i - 1
                if idx == 0:
                    continue
                embed.add_field(
                    name = f'{WL[idx].number}. {WL[idx].name} ( ' + format(WL[idx].meso, ',') + ' 메소 )',
                    value = f'공격력 : {WL[idx].damage}\n치명타 확률 : {WL[idx].c_chance}%\n치명타 데미지 : {round(WL[idx].c_damage * 100)}' + '%',
                    inline = False
                )
            embed.set_footer(text = f'{ctx.author.nick} 님의 메소 : ' + format(meso[ctx.author.id], ','))
        else: # 설정된 인덱스가 아닐 경우
            embed=discord.Embed(title="존재하지 않는 인덱스입니다", description="도움이 필요하신가요 ? => !도움말", color=0xf99090)
        await ctx.send(embed=embed) # 임베드 출력
    except IndexError:
        await ctx.send("개발중입니다.")
    except KeyError:
        await ctx.send("정보등록을 하지 않으셨나요?")

@bot.command()
async def 무기구매(ctx, index: int):
    try:
        if index == 0 or index >= len(WL): # 잘못된 인덱스 선택 시
            embed=discord.Embed(title="존재하지 않는 장비 번호입니다.", description="도움이 필요하신가요 ? => !도움말", color=0xf99090)
        elif meso[ctx.author.id] >= WL[index].meso:
            meso[ctx.author.id] -= WL[index].meso
            weapondamage[ctx.author.id] = WL[index].damage
            weaponname[ctx.author.id] = WL[index].name
            weaponnumber[ctx.author.id] = WL[index].number
            weaponcritchance[ctx.author.id] = WL[index].c_chance
            weaponcritdamage[ctx.author.id] = WL[index].c_damage
            embed=discord.Embed(title=f'{WL[index].name} 을(를) 구매하셨습니다.', description='보유 메소 : ' + format(meso[ctx.author.id], ','), color=0xf99090)
        else:
            embed=discord.Embed(title="메소가 부족합니다.", description='필요 메소 : ' + format(WL[index].meso - meso[ctx.author.id], ','), color=0xf99090)
        await ctx.send(embed=embed)
    except KeyError:
        await ctx.send("정보등록을 하지 않으셨나요?")

@무기상점.error
async def info_error(ctx, error):
    embed=discord.Embed(title="페이지 번호를 입력해주세요.", description="예 : !무기상점 1", color=0xf99090)
    await ctx.send(embed=embed)

@bot.command()
async def 아머상점(ctx, index: int): # 이름(a.name), 번호(a.number), 요구메소(a.meso), 방어력(a.defense), 치명타 확률(a.c_chance), 치명타 데미지(a.c_damage)
    try:
        if index in range(1, 2): # 설정된 인덱스를 벗어나지 않았을 경우
            embed=discord.Embed(title="아머상점", description=f"{index} 페이지", color=0x7b4ee4)
            for i in range(1, 11):
                idx = (index - 1) * 10 + i - 1 # 인덱스 계산
                if idx == 0: # 0일 시 해당하는 물품이 없으므로 예외처리 ( continue )
                    continue
                embed.add_field(
                    name = f'{AL[idx].number}. {AL[idx].name} ( ' + format(AL[idx].meso, ',') + ' 메소 )',
                    value = f'방어력 : {AL[idx].defense}\n치명타 확률 : {AL[idx].c_chance}%\n치명타 데미지 : {round(AL[idx].c_damage * 100)}' + '%',
                    inline = False
                )
            embed.set_footer(text = f'{ctx.author.nick} 님의 메소 : ' + format(meso[ctx.author.id], ','))
        else: # 설정된 인덱스가 아닐 경우
            embed=discord.Embed(title="존재하지 않는 인덱스입니다.", description="도움이 필요하신가요 ? => !도움말", color=0x7b4ee4)
        await ctx.send(embed=embed) # 임베드 출력
    except IndexError: # 인덱스를 벗어날 경우
        await ctx.send("개발중입니다.")
    except KeyError: # 변수 초기화가 되지 않은 경우
        await ctx.send("정보등록을 하지 않으셨나요?")

@bot.command()
async def 아머구매(ctx, index: int):
    try:
        if index == 0 or index >= len(AL): # 잘못된 인덱스 선택 시
            embed=discord.Embed(title="존재하지 않는 장비 번호입니다.", description="도움이 필요하신가요 ? => !도움말", color=0x7b4ee4)
        elif meso[ctx.author.id] >= AL[index].meso:
            meso[ctx.author.id] -= AL[index].meso
            armordefense[ctx.author.id] = AL[index].defense
            armorname[ctx.author.id] = AL[index].name
            armornumber[ctx.author.id] = AL[index].number
            armorcritchance[ctx.author.id] = AL[index].c_chance
            armorcritdamage[ctx.author.id] = AL[index].c_damage
            embed=discord.Embed(title=f'{AL[index].name} 을(를) 구매하셨습니다.', description='보유 메소 : ' + format(meso[ctx.author.id], ','), color=0x7b4ee4)
        else:
            embed=discord.Embed(title="메소가 부족합니다.", description='필요 메소 : ' + format(AL[index].meso - meso[ctx.author.id], ','), color=0x7b4ee4)
        await ctx.send(embed=embed)
    except KeyError:
        await ctx.send("정보등록을 하지 않으셨나요?")
        
@아머상점.error
async def info_error(ctx, error):
    embed=discord.Embed(title="페이지 번호를 입력해주세요.", description="예 : !아머상점 1", color=0x7b4ee4)
    await ctx.send(embed=embed)

@bot.command()
async def 레벨설정(ctx, user: int):
    try:
        level[ctx.author.id] = user
        await ctx.send(str(user) + "레벨이 되었습니다.")
    except KeyError:
        await ctx.send("정보등록 하세요 ^^ㅣ발")

@bot.command()
async def 경험치설정(ctx, user: int):
    try:
        exp[ctx.author.id] = user
        await ctx.send(str(user) + "경험치가 되었습니다.")
    except KeyError:
        await ctx.send("정보등록 하세요 ^^ㅣ발")

@bot.command()
async def 메소설정(ctx, user: int):
    try:
        meso[ctx.author.id] = user
        await ctx.send(str(user) + "메소가 주어졌습니다.")
    except KeyError:
        await ctx.send("정보등록 하세요 ^^ㅣ발")

@bot.command()
async def 인벤토리(ctx):
    try:
        EXP = format(exp[ctx.author.id], ',') # 현재 경험치에 , 를 넣어줌.
        MAXEXP = format(maxexp[ctx.author.id], ',') # 최대 경험치에 , 를 넣어줌.
        damage[ctx.author.id] = weapondamage[ctx.author.id] + leveldamage[ctx.author.id] # 공격력 = 레벨공격력 + 무기공격력
        critical_chance[ctx.author.id] = min(100, armorcritchance[ctx.author.id] + weaponcritchance[ctx.author.id]) # 치명타 확률 = 방어구 치명타 확률 + 무기 치명타 확률
        critical_damage[ctx.author.id] = 1.5 + armorcritdamage[ctx.author.id] + weaponcritdamage[ctx.author.id] # 치명타 데미지 = 방어구 치명타 데미지 + 무기 치명타 데미지
        embed=discord.Embed(title=ctx.author.nick + "님의 인벤토리")
        embed.add_field(name="무기", value=weaponname[ctx.author.id], inline=True)
        embed.add_field(name="공격력", value=str(damage[ctx.author.id]), inline=True)
        embed.add_field(name="메소", value=str(meso[ctx.author.id]), inline=True)
        embed.add_field(name="방어구", value=armorname[ctx.author.id], inline=True)
        embed.add_field(name="방어력", value=str(armordefense[ctx.author.id]), inline=True)
        embed.add_field(name="체력", value=format(maxhp[ctx.author.id], ','), inline=True)
        embed.add_field(name="치명타 확률", value=str(critical_chance[ctx.author.id]) + "%", inline=True)
        embed.add_field(name="치명타 데미지", value=str(round(critical_damage[ctx.author.id] * 100)) + "%", inline=True) # 실제 치명타 데미지 배수 * 100 을 반올림 ( % 로 표기하기 위해 )
        embed.set_footer(text=f'레벨 : {level[ctx.author.id]}\n경험치 : {EXP} / {MAXEXP} ( {int(exp[ctx.author.id] / maxexp[ctx.author.id] * 100)}% )')
        await ctx.send(embed=embed)
    except KeyError: # 키에러일 시 ( 정보등록을 하지 않았을 시 )
        await 정보등록(ctx)
        await 인벤토리(ctx)

@bot.command()
async def 경험치(ctx):
    try:
        EXP = format(exp[ctx.author.id], ',') # 현재 경험치에 , 를 넣어줌.
        MAXEXP = format(maxexp[ctx.author.id], ',') # 최대 경험치에 , 를 넣어줌.
        expper = int(exp[ctx.author.id] / maxexp[ctx.author.id] * 10) # 현재 경험치 퍼센트
        embed = discord.Embed(title=f'경험치 : {EXP} / {MAXEXP} ( {int(exp[ctx.author.id] / maxexp[ctx.author.id] * 100)}% )',
                            description=f':green_square:' * expper + ':white_large_square:' * (10 - expper))
        embed.set_footer(text=f'called by {ctx.author.nick}')
        await ctx.send(embed=embed)
    except KeyError:
        await 정보등록(ctx)
        await 경험치(ctx)

levelupInfo = { # 레벨업 정보
    #  <레벨>: [ 경험치 요구, 최대 체력, 레벨 데미지 ]
        0: [100, 150, 20], # 기본 경험치 요구량, 기본 최대 체력, 기본 레벨 데미지
        1: [300, 200, 35], # 1레벨에서 2레벨로 넘어갈 때 ( 1레벨일 시 )
        2: [500, 300, 40],
        3: [1500, 500, 60],
        4: [2000, 600, 90],
        5: [3550, 800, 105],
        6: [4200, 1000, 130],
        7: [7600, 1350, 170],
        8: [10500, 2000, 230],
        9: [20750, 3000, 255],
        10: [30782, 3500, 300],
        11: [37895, 4200, 450],
        12: [48720, 5000, 600],
        13: [56345, 6500, 720],
        14: [140000, 8000, 800],
        15: [327000, 12000, 1180],
        16: [650000, 15000, 1600],
        17: [1320000, 52000, 3000],
        18: [3350000, 67000, 3500],
        19: [7720000, 83000, 4300],
        20: [11340000, 100000, 4800],
        21: [23920000, 150000, 6000],
        22: [34587500, 220000, 9000],
        23: [49000000, 350000, 15000]
    }

async def levelup(reaction, user): # 레벨업 함수
    jumped = 0 # 한 번에 몇 번 레벨업 하였는지를 저장할 변수
    while exp[user.id] >= maxexp[user.id]: # 현재 경험치량이 경험치 요구량보다 적어질 때 까지 반복 ( 한번에 연속 레벨업 가능 )
        jumped += 1
        exp[user.id] = exp[user.id] - maxexp[user.id] # 경험치량 초기화
        maxexp[user.id] = levelupInfo[level[user.id]][0] # 새로운 경험치 요구량
        maxhp[user.id] = levelupInfo[level[user.id]][1] # 최대 체력 증가
        leveldamage[user.id] = levelupInfo[level[user.id]][2] # 레벨 데미지 증가
        level[user.id] += 1 # 레벨 + 1
        hp[user.id] = maxhp[user.id] # 체력을 초기화시킴
    jumptimes = f'( x{jumped} )' if jumped >= 2 else '' # 한번에 2회 이상 레벨업했으면 횟수를 표시하고, 그 외에는 표시할 이유가 없으므로 공란
    embed=discord.Embed(title=f'{level[user.id]} 레벨이 되었습니다! {jumptimes}')
    await reaction.message.channel.send(embed=embed) # 임베드 출력

async def BattleStatus(reaction, user, iscrit): # 배틀 창 표시 함수
    myhpper = f" ( {int((hp[user.id] / maxhp[user.id]) * 100)}% )" # 자신의 HP 퍼센트 변수
    mobhpper = f" ( {int((mobhp[user.id] / mobmaxhp[user.id]) * 100)}% )" # 몹의 HP 퍼센트 변수
    HP = format(hp[user.id], ',') # 내 현재 체력
    MAXHP = format(maxhp[user.id], ',') # 내 최대 체력
    MOBHP = format(mobhp[user.id], ',') # 몹의 현재 체력
    MOBMAXHP = format(mobmaxhp[user.id], ',') # 몹의 최대 체력
    embed=discord.Embed(title=":crossed_swords: 전투 :crossed_swords:", color=0xfffff9)
    embed.set_author(name=mobworld[user.id], icon_url=mobicon[user.id])
    embed.set_image(url=mobimg[user.id])
    embed.add_field(name=mobname[user.id], value=f"\n내 HP : {HP} / {MAXHP} {myhpper}\n\n적의 HP : {MOBHP} / {MOBMAXHP} {mobhpper} {iscrit}", inline=False)
    message = await reaction.message.channel.send(embed=embed)
    for i in battle_emoji2:
        await message.add_reaction(i)

async def BattleAppear(ctx):
    MOBMAXHP = format(mobmaxhp[ctx.author.id], ',')
    battle[ctx.author.id] = True # 전투 상태 활성화
    embed=discord.Embed(title=":mag: 몬스터 발견 :mag_right:", color=0xfffff9)
    embed.set_author(name=mobworld[ctx.author.id], icon_url=mobicon[ctx.author.id])
    embed.set_image(url=mobimg[ctx.author.id])
    embed.add_field(name=mobname[ctx.author.id], value=f"HP : {MOBMAXHP}", inline=True)
    message = await ctx.send(embed=embed)
    for i in battle_emoji1:
        await message.add_reaction(i)

def MobSetting(ctx, region, mobchance): # 전투 몹 설정 함수
    mobname[ctx.author.id] = eval(f'mob_{region}{mobchance}.name')
    mobdamage[ctx.author.id] = eval(f'mob_{region}{mobchance}.damage')
    mobmaxhp[ctx.author.id] = eval(f'mob_{region}{mobchance}.hp')
    mobhp[ctx.author.id] = eval(f'mob_{region}{mobchance}.hp')
    mobmeso[ctx.author.id] = eval(f'mob_{region}{mobchance}.meso')
    mobexp[ctx.author.id] = eval(f'mob_{region}{mobchance}.exp')
    mobworld[ctx.author.id] = eval(f'mob_{region}{mobchance}.world')
    mobimg[ctx.author.id] = eval(f'mob_{region}{mobchance}.img')
    mobicon[ctx.author.id] = eval(f'mob_{region}{mobchance}.icon')

@bot.command()
async def 월드맵(ctx):
    try:
        embed = discord.Embed(title=keyword_mapnum[mapnum[ctx.author.id]][1], # Embed 설정
                            description="",
                            color=0xFFFFF9)
        embed.set_image(url=eval(f'map_{keyword_mapnum[mapnum[ctx.author.id]][0]}')) # 월드맵 이미지 설정
        message = await ctx.send(embed=embed)
        for i in linked_map[mapnum[ctx.author.id]]:
            await message.add_reaction(i)
    except KeyError:
        await 정보등록(ctx)
        await 월드맵(ctx)

@bot.event
async def on_reaction_add(reaction, user):
    if user.id == bot.user.id: 
        return
    if reaction.message.author.id == bot.user.id:
        if reaction.me:
            if str(reaction.emoji) in maplist0: # 월드 이모지일 시
                await reaction.message.delete() # 메세지 삭제
                mapnum[user.id] = icon_mapnum[str(reaction.emoji)] # mapnum 설정
                embed = discord.Embed(title=keyword_mapnum[mapnum[user.id]][1], # Embed 설정
                        description="",
                        color=0xFFFFF9)
                embed.set_image(url=eval(f'map_{keyword_mapnum[mapnum[user.id]][0]}')) # 월드맵 이미지 설정
                message = await reaction.message.channel.send(embed=embed)
                for i in linked_map[mapnum[user.id]]:
                    await message.add_reaction(i)


            if str(reaction.emoji) == '⚔️':
                await reaction.message.delete() # 반응한 메세지를 삭제함.

                critical_chance[user.id] = min(100, armorcritchance[user.id] + weaponcritchance[user.id]) # 치명타 확률 = 방어구 치명타 확률 + 무기 치명타 확률
                critical_damage[user.id] = 1.5 + weaponcritdamage[user.id] + armorcritdamage[user.id] # 치명타 공격력 = 기본 150% + 무기 치명타 공격력 + 아머 치명타 공격력
                damage[user.id] = weapondamage[user.id] + leveldamage[user.id] # 공격력 = 무기 공격력 + 레벨 공격력

                Damage = random.randrange(int(damage[user.id] * 0.9), int(damage[user.id] * 1.1)) # 공격력의 랜덤값 ( ±10% )
                Mobdamage = random.randrange(int(mobdamage[user.id] * 0.9), int(mobdamage[user.id] * 1.1)) # 몹 공격력의 랜덤값 ( ±10% )
                crit = random.randrange(100) # 크리티컬 확률 난수 생성


                if (Mobdamage <= armordefense[user.id]): # 방어력이 몬스터의 공격력 이상이라면
                    hp[user.id] -= 1 # 1 의 데미지를 입음.
                else: # 아니라면 정상적으로 데미지를 입음.
                    hp[user.id] -= Mobdamage - armordefense[user.id] # 체력 = 몬스터의 공격력 - 방어구의 방어력

                if (crit < critical_chance[user.id]): # 크리티컬이 터질 시
                    mobhp[user.id] -= int(Damage * critical_damage[user.id]) # 공격력 * 크리티컬 데미지 ( 정수변환 )
                    iscrit = " ( 치명타 )" # 크리티컬 메세지 표시
                else: # 크리티컬이 터지지 않을 시
                    mobhp[user.id] -= Damage # 공격력 
                    iscrit = " " # 크리티컬 메세지 비표시

                if (mobhp[user.id] <= 0): # 적을 처치했을 시
                    battle[user.id] = False # 전투 상태를 종료시킴
                    hp[user.id] = maxhp[user.id] # 체력을 초기화시킴
                    meso[user.id] += mobmeso[user.id] # 적 몬스터가 주는 메소만큼 메소를 더함
                    exp[user.id] += mobexp[user.id] # 적 몬스터가 주는 경험치만큼 경험치를 더함
                    potioncount[user.id] = 0 # 포션 카운트를 초기화시킴
                    embed=discord.Embed(title=mobname[user.id] + "을(를) 처치했습니다.")
                    embed.add_field(name="경험치", value="+ " + str(mobexp[user.id]), inline=True)
                    embed.add_field(name="메소", value="+ " + str(mobmeso[user.id]), inline=True)
                    await reaction.message.channel.send(embed=embed)
                    if (exp[user.id] >= maxexp[user.id]): # 경험치가 레벨업 경험치 요구량 까지 채워질 경우
                        await levelup(reaction, user) # 레벨업
                    return None

                if (hp[user.id] <= 0): # 죽을 시
                    battle[user.id] = False # 전투 상태를 비활성화시킴
                    exp[user.id] = 0 # 경험치를 초기화시킴
                    hp[user.id] = maxhp[user.id] # 체력을 초기화시킴
                    potioncount[user.id] = 0 # 포션 카운트를 초기화시킴
                    embed=discord.Embed(title="적에게 죽어 모든 경험치를 잃었습니다.")
                    await reaction.message.channel.send(embed=embed)
                    return None

                await BattleStatus(reaction, user, iscrit) # 전투 창 표시 ( 첫 매개 변수 : reaction, 두번째 매개 변수 : user, 세번째 매개 변수 : 치명타 여부 ( iscrit ) )

            if str(reaction.emoji) == '🧪': # 물약을 마셨을 시

                await reaction.message.delete() # 반응한 메세지를 삭제시킴.
                
                usemeso = meso[user.id] // 100 # 지불하는 메소 = 현재 메소의 1 % 
                meso[user.id] -= usemeso # 현재 메소에서 지불하는 메소의 양을 차감

                if (potioncount[user.id] <= 4): # 포션 카운트가 5개가 넘지 않았을 때
                    potioncount[user.id] += 1 # 포션 카운트를 1 증가시킴
                    hp[user.id] += int(maxhp[user.id] / 2) # 현재 체력을 최대 체력의 1/2 만큼 회복시킴.
                    if (hp[user.id] > maxhp[user.id]): # 만약 회복 시켰는데 현재 체력이 최대 체력을 넘기면
                        hp[user.id] = maxhp[user.id] # 현재 체력을 최대 체력과 똑같게 만듦.
                    embed=discord.Embed(title=str(usemeso) + " 메소를 지불하여 최대 체력의 50%를 회복하였습니다.\n( 남은 물약 사용 가능 횟수 : " + str(5 - potioncount[user.id]) + " ) ") 
                    await reaction.message.channel.send(embed=embed)
                else: # 포션 카운트를 5개 모두 사용하였을 때
                    embed=discord.Embed(title="물약 사용 가능 횟수를 모두 소진하였습니다.")
                    await reaction.message.channel.send(embed=embed)

                await BattleStatus(reaction, user, '') # 전투 창 표시 ( 첫 매개 변수 : reaction, 두번째 매개 변수 : user, 세번째 매개 변수 : 치명타 여부 ( iscrit ) )

            if str(reaction.emoji) == '🏳️': # 도망쳤을 시
                await reaction.message.delete() # 전투 메세지 삭제
                battle[user.id] = False # 전투 상태를 종료시킴
                hp[user.id] = maxhp[user.id] # 체력을 초기화시킴
                potioncount[user.id] = 0 # 포션 카운트를 초기화시킴
                으 = '으' if (ord(mobname[user.id][-1]) - 0xAC00) % 28 > 0 else '' # 몹 이름 마지막 글자가 종성이 있으면 ~으로, 종성이 없으면 ~로 라고 출력.
                embed=discord.Embed(title=f'{mobname[user.id]}{으}로부터 도망쳤습니다.')
                await reaction.message.channel.send(embed=embed)

@bot.command()
async def 사냥(ctx):
    try:
        if battle[ctx.author.id] == True:
            await ctx.send(embed=discord.Embed(title="이 명령어를 사용할 수 없는 상태입니다!"))
            return None
        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        if mapnum[ctx.author.id] == 0: # 에델슈타인 ( edel, leben )
            mobchance = random.randrange(25)
            if mobchance < 13: # mobchance 가 0 ~ 12 일 시 ( 에델슈타인 )
                MobSetting(ctx, 'edel', mobchance + 1) # 첫 매개변수로 ctx 전달, 두번째 매개변수로 변수의 지역 이름 축약명 전달, 세번째 매개변수로 mobchance와 맞춰 변경될 몹 번호 전달.
            else: # mobchance 가 13 ~ 24 일 시 ( 레벤 광산 )
                MobSetting(ctx, 'leben', mobchance - 12)
        elif mapnum[ctx.author.id] == 2: # 니할사막 ( nihal )
            bosschance = random.randrange(100)
            mobchance = random.randrange(30)
            if bosschance == 0: # bosschance 가 0 일 시 데우
                if random.randrange(5) == 0: # 그 중에서 1/5 확률로 히든 데우
                    MobSetting(ctx, 'nihal', 32)
                else: # 일반 데우
                    MobSetting(ctx, 'nihal', 31)
            elif bosschance == 1: # bosschance 가 1 일 시 루루모
                if random.randrange(5) == 0: # 그 중에서 1/5 확률로 루루모모
                    MobSetting(ctx, 'nihal', 34)
                else: # 루루모
                    MobSetting(ctx, 'nihal', 33)
            elif bosschance == 2: # bosschance 가 2 일 시 호문스페큘러
                MobSetting(ctx, 'nihal', 35)
            elif bosschance == 3: # bosschance 가 3 일 시 디트와 로이
                MobSetting(ctx, 'nihal', 36)
            elif bosschance == 4: # bosschance 가 4 일 시 키메라
                if random.randrange(5) == 0: # 그 중에서 1/5 확률로 히든 키메라
                    MobSetting(ctx, 'nihal', 38)
                else: # 키메라
                    MobSetting(ctx, 'nihal', 37)
            elif bosschance == 5: # bosschance 가 5 일 시 프랑켄로이드
                if random.randrange(5) == 0: # 그 중에서 1/5 확률로 화난 프랑켄로이드
                    MobSetting(ctx, 'nihal', 40)
                else: # 프랑켄로이드
                    MobSetting(ctx, 'nihal', 39)
            else: # 일반 몬스터
                MobSetting(ctx, 'nihal', mobchance + 1)
        elif mapnum[ctx.author.id] == 3: # 아쿠아로드 ( aquaroad )
            bosschance = random.randrange(100)
            mobchance = random.randrange(22)
            if bosschance < 5: # bosschance 가 0, 1, 2, 3, 4 일 시 세르프
                MobSetting(ctx, 'aquaroad', 23)
            elif bosschance == 5: # bosschance 가 5 일 시 피아누스
                MobSetting(ctx, 'aquaroad', 24)
            else: # 일반 몬스터
                MobSetting(ctx, 'aquaroad', mobchance + 1)
        elif mapnum[ctx.author.id] == 4: # 엘나스 산맥 ( orbis, elnath )
            bosschance = random.randrange(100)
            mobchance = random.randrange(31)
            if bosschance < 4: # bosschance 가 0, 1, 2, 3 일 시 orbis 지역 보스
                MobSetting(ctx, 'orbis', bosschance + 16)
            elif bosschance < 8: # bosschance 가 4, 5, 6, 7 일 시 elnath 지역 보스
                MobSetting(ctx, 'elnath', bosschance + 13)
            else: # 일반 몬스터
                if mobchance < 15: # mobchance 가 15 미만이면 orbis, 15 이상이면 elnath
                    MobSetting(ctx, 'orbis', mobchance + 1)
                else:
                    MobSetting(ctx, 'elnath', mobchance - 14)
        elif mapnum[ctx.author.id] == 5: # 루더스 호수 ( luduslake )
            bosschance = random.randrange(100)
            mobchance = random.randrange(19)
            if bosschance < 3: # bosschance 가 0, 1, 2 일 시 롬바드
                MobSetting(ctx, 'luduslake', 20)
            elif bosschance < 5: # bosschance 가 3, 4 일 시 타이머
                MobSetting(ctx, 'luduslake', 21)
            else: # 일반 몬스터
                MobSetting(ctx, 'luduslake', mobchance + 1)
        elif mapnum[ctx.author.id] == 6: # 에레브 ( ereb )
            mobchance = random.randrange(5)
            MobSetting(ctx, 'ereb', mobchance + 1)
        elif mapnum[ctx.author.id] == 8: # 리엔 ( rien )
            mobchance = random.randrange(5)
            MobSetting(ctx, 'rien', mobchance + 1)
        elif mapnum[ctx.author.id] == 1: # 빅토리아 아일랜드 ( vic )
            bosschance = random.randrange(100)
            mobchance = random.randrange(36) 
            if bosschance < 5: # bosschance 가 0, 1, 2, 3, 4 일 시 보스 ( 5% )
                MobSetting(ctx, 'vic', bosschance + 37)
            else:
                MobSetting(ctx, 'vic', mobchance + 1)
        elif mapnum[ctx.author.id] == 10: # 미나르숲 ( minar )
            mobchance = random.randrange(28)
            bosschance = random.randrange(100)
            if bosschance == 0: # bosschance 가 0 일 시 마스터 호브
                MobSetting(ctx, 'minar', 29)
            elif bosschance == 1: # bosschance 가 1 일 시 마스터 하프
                MobSetting(ctx, 'minar', 30)
            elif bosschance == 2: # bosschance 가 2 일 시 마뇽
                if random.randrange(5): # 그 중에서 1/5 확률로 히든 마뇽
                    MobSetting(ctx, 'minar', 31)
                else: # 히든 마뇽
                    MobSetting(ctx, 'minar', 32)
            elif bosschance == 3: # bosschance 가 3 일 시 그리프
                if random.randrange(5): # 그 중에서 1/5 확률로 히든 그리프
                    MobSetting(ctx, 'minar', 33)
                else: # 히든 그리프
                    MobSetting(ctx, 'minar', 34)
            elif bosschance == 4: # bosschance 가 4 일 시 켄타우로스 킹
                MobSetting(ctx, 'minar', 35)
            elif bosschance == 5: # bosschance 가 5 일 시 레비아탄
                if random.randrange(5): # 그 중에서 1/5 확률로 히든 레비아탄
                    MobSetting(ctx, 'minar', 36)
                else: # 히든 레비아탄
                    MobSetting(ctx, 'minar', 37)
            elif bosschance == 6: # bosschance 가 6 일 시 드래고니카
                MobSetting(ctx, 'minar', 38)
            elif bosschance == 7: # bosschance 가 7 일 시 드래곤라이더
                MobSetting(ctx, 'minar', 39)
            else: # 일반 몬스터
                MobSetting(ctx, 'minar', mobchance + 1)
        elif mapnum[ctx.author.id] == 14: # 슬리피우드 ( slp )
            mobchance = random.randrange(9)
            bosschance = random.randrange(100)
            if bosschance < 2: # bosschance 가 0, 1 일 시 주니어발록
                MobSetting(ctx, 'slp', 10)
            elif bosschance < 5: # bosschance 가 2, 3, 4 일 때 좀비머쉬맘
                MobSetting(ctx, 'slp', 11)
            else:
                MobSetting(ctx, 'slp', mobchance + 1)
        elif mapnum[ctx.author.id] == 21: # 아랫마을 ( folk )
            mobchance = random.randrange(7)
            MobSetting(ctx, 'folk', mobchance + 1)
        elif mapnum[ctx.author.id] == 22: # 폐광 ( deepmine )
            mobchance = random.randrange(5)
            MobSetting(ctx, 'deepmine', mobchance + 1)
        elif mapnum[ctx.author.id] == 23: # 사자왕의 성 ( lioncastle )
            bosschance = random.randrange(100)
            mobchance = random.randrange(9)
            if bosschance < 2: # bosschance 가 0, 1 일 때 킹 캐슬 골렘
                MobSetting(ctx, 'lioncastle', 10)
            elif bosschance == 2: # bosschance 가 2 일 때 교도관 아니
                MobSetting(ctx, 'lioncastle', 11)
            else: # 일반 몬스터
                MobSetting(ctx, 'lioncastle', mobchance + 1)
        elif mapnum[ctx.author.id] == 27: # 시계탑 최하층 ( clocktower )
            bosschance = random.randrange(100)
            mobchance = random.randrange(23)
            if bosschance < 5: # bosschance 가 0 ~ 4 일 때 알리샤르
                MobSetting(ctx, 'clocktower', 24)
            else: # 일반 몬스터
                MobSetting(ctx, 'clocktower', mobchance + 1)
        elif mapnum[ctx.author.id] == 43: # 리에나 해협 ( riena )
            mobchance = random.randrange(8)
            MobSetting(ctx, 'riena', mobchance + 1)
        elif mapnum[ctx.author.id] == 61: # 엘리넬 ( elinel )
            bosschance = random.randrange(100)
            mobchance = random.randrange(9)
            if bosschance < 5: # bosschance 가 0 ~ 5 일 때 몰킹
                MobSetting(ctx, 'elinel', 10)
            else: # 일반 몬스터
                MobSetting(ctx, 'elinel', mobchance + 1)
        elif mapnum[ctx.author.id] == 62: # 골드비치 ( goldbeach )
            bosschance = random.randrange(100)
            mobchance = random.randrange(11)
            if bosschance < 5: # bosschance 가 0 ~ 5 일 때 캡틴 블랙 슬라임
                MobSetting(ctx, 'goldbeach', 12)
            else: # 일반 몬스터
                MobSetting(ctx, 'goldbeach', mobchance + 1)
        elif mapnum[ctx.author.id] == 63: # 엘로딘 ( elodin )
            mobchance = random.randrange(10)
            MobSetting(ctx, 'elodin', mobchance + 1)
        elif mapnum[ctx.author.id] == 64: # 버섯의 성 ( mushroom )
            bosschance = random.randrange(100)
            mobchance = random.randrange(10)
            if bosschance < 3: # bosschance 가 0, 1, 2 일 때 검은 바이킹
                MobSetting(ctx, 'mushroom', 11)
            elif bosschance < 5: # bosschance 가 3, 4 일 때 총리대신
                MobSetting(ctx, 'mushroom', 12)
            else: # 일반 몬스터
                MobSetting(ctx, 'mushroom', mobchance + 1)
        else:
            await ctx.send(embed=discord.Embed(title='사냥할 수 없는 지역입니다.', description=f'현재 지역 : {keyword_mapnum[mapnum[ctx.author.id]][1]}'))
            return None
        await BattleAppear(ctx) # 배틀 창 출현
    except KeyError:
        await 정보등록(ctx)
        await 사냥(ctx)



bot.run(TOKEN)