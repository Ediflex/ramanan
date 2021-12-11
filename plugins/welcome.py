import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Welcome {message.from_user.mention} to {message.chat.username} ,  Happy to have here ഞാൻ രമണൻ എന്റെ Groupലാണ് നിങ്ങൾ Movie Search ചെയ്യുന്നത് അതുകൊണ്ട് Movieയുടെ Name Google ൽ നോക്കി Groupൽ Search ചെയ്യുക. Movieയുടെ Name ൽ Spelling Mistake ഉണ്ടെങ്കിൽ ഞാൻ നിങ്ങൾക്ക് Movie തരുന്നതല്ല.             എന്ന് നിങ്ങളുടെ രമണൻ",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Bye ,  {message.from_user.mention} , പോയിട്ട് Vada Ramanan നിന്നെ Wait ചെയ്യുന്നുണ്ട്",chat_id=chatid)
	

