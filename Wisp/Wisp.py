import discord
from discord.ext import commands
from discord import Intents
import praw

import random

import datetime

import pytz

import time

reddit = praw.Reddit(
    client_id = "8ZHsXepRnow4pg", 
    client_secret = "s6dDHt-iVmJIFvfPR90-0bVTexterA", 
    username = "aveni121",
    password = "Slayer18346150!", 
    user_agent = "something")

bot = commands.Bot(command_prefix = '.', intents= Intents.all())

#This program is a discord love bot that does different things
#It makes use of the APIs discordpy and praw which is for Discord and Reddit
#each command has a description of what it does.

#Greets the member of the discord server in the general channel everytime they go online
@ bot.event
async def on_member_update(before, after):
    channel = bot.get_channel(766944488773648418)
    if str(before.status) == "offline":
        if str(after.status) == "online":
            await channel.send("Hello {} you are the most beautiful person in the world".format(after.name))


#prints once to the console/terminal once the bot goes online
@bot.event
async def on_ready():
    print("Bot:Wisp online...")

#prints a quote depending on user choice
#.remind 0 prints "Your lover just wants to remind you that you are a special person"
@bot.command()
async def remind(ctx):

    list1 = range(10)
    choice = random.choice(list1)

    if choice == 0:
        await ctx.send("Your lover just wants to remind you that you are a special person")
    elif choice == 1:
        await ctx.send("You are missed, and always will be missed when you're not around")
    elif choice == 2:
        await ctx.send("You are the best thing in his/her life")
    elif choice == 3:
        await ctx.send("A day with you is always a day filled with happiness")
    elif choice == 4:
        await ctx.send("Life wasn't this good until you came around")
    elif choice == 5:
        await ctx.send("Someday you guys will be married, so drop all the problems and the troublesome thoughts and pick each other")
    elif choice == 6:
        await ctx.send("You are the reason behind someone's smile")
    elif choice == 7:
        await ctx.send("If you could see yourself through his/her eyes, you would understand how special you are to him/her")
    elif choice == 8:
        await ctx.send("Forever wants to be spent with you and only you")
    elif choice == 9:
        await ctx.send("Life's greatest treasure is the person you spend it with")

#Grabs a random post from the "hot" section of a subreddit
#It would print the title of the post and an image if the posts
#contains one
#this is useful for grabbing posts for memes and food
@bot.command()
async def show(ctx, arg = "all"):
    try:
        arg.lower()
        subreddit = reddit.subreddit(arg)
        all_submissions = []

        hot = subreddit.hot(limit = 50)

        for submission in hot: 
            all_submissions.append(submission)

        random_submission = random.choice(all_submissions)

        name = random_submission.title
        url = random_submission.url

        em = discord.Embed(title = name)

        em.set_image(url = url)

        if arg == "nsfw" :
            await ctx.send("Access Denied.")
        else:
            await ctx.send(embed = em)

    except:
        await ctx.send(arg + " has no results")

#This command calls a function that calculates the days till a certain celebration
#It makes use of timezones and converts it from UTC to PST
#the default celebration is anniversary but can be changed to monthsary by typing
#.till monthsary
@bot.command()
async def till(ctx, celebration = "anniversary"):
    celebration.lower()

    #Initialize dates
    #Anniversary is Dec 9 of every year

    today = datetime.datetime.now(tz = pytz.utc)
    anniv_date = datetime.datetime(today.year, 12, 9, 8, tzinfo = pytz.utc)

    #Create timezone object for PST
    source_time_zone = pytz.timezone("US/Pacific")

    #Dates with timezone

    anniv_date_PST = anniv_date.astimezone(source_time_zone)
    today_date_PST = today.astimezone(source_time_zone)

    #Checking for right monthsary date
    #Monthsary is the 9th of every motnh

    if(today_date_PST.day < 9):
        #Sets the monthsary date to the 9th of the current month
        monthsary_date = datetime.datetime(today.year, today.month, 9, 8, tzinfo = pytz.utc)
    elif(today_date_PST.day == 9 and today.month == 12):
        #if the current day and month is the same as anniversary
        await ctx.send("Happy Anniversary!")
    elif(today_date_PST.day == 9):
        #if the current day is the monthsary
        monthsary_date = today_date_PST
        await ctx.send("Happy Monthsary!")
    else:
        #if it's December sets the next monthsary date to January 9 of the next year
        if(today_date_PST.month == 12):
            monthsary_date = datetime.datetime(today.year+1, 1, 9, 8, tzinfo = pytz.utc)
        #Sets the monthsary date to the 9th of next month
        else:
            monthsary_date = datetime.datetime(today.year, today.month+1, 9, 8, tzinfo = pytz.utc)

    #Convert monthsary date with timezone

    monthsary_date_PST = monthsary_date.astimezone(source_time_zone)

    #Choice

    if celebration == "anniversary":
        days_till_anniv = anniv_date_PST - today_date_PST
        round_anniv = str(days_till_anniv).split(":")
        await ctx.send(round_anniv[0] + " hours " + round_anniv[1] + " minutes " + round_anniv[2].split(".")[0] + " seconds")

    elif celebration == "monthsary":
        days_till_monthsary = monthsary_date_PST - today_date_PST
        round_monthsary = str(days_till_monthsary).split(":")
        await ctx.send(round_monthsary[0] + " hours " + round_monthsary[1] + " minutes " + round_monthsary[2].split(".")[0] + " seconds")

#command that grabs a reason for loving from lovequotes.txt
#the command can be entered as ".reason N" where N is the number of quotes you want to be printed
#each quote is printed with a delay of 5 seconds to avoid spamming in discord
@bot.command()
async def reason(ctx, i = 1):
    await ctx.send("Here's a reason why I love you:")
    with open("lovequotes.txt", "r") as inFile:
        data = inFile.read()
        quote_list = data.split("\n")
    
    while i > 0:
        grab_reason = random.choice(quote_list)
        await ctx.send(grab_reason)
        i -= 1
        time.sleep(5)

bot.run("NzgyNDQwNTIwMDU5ODQ2Njg2.X8MOhQ.rmzyoeHk6ocP_KV8mqM9THtzDy8")