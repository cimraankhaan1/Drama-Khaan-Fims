# Waxaan isticmaaleynaa nooc cusub oo Linux ah (Bookworm) si aan uga badbaadno cilada '404 error'
FROM python:3.10-slim-bookworm

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# Dejinta Timezone-ka (waad iska dhaafi kartaa hadaadan rabin)
ENV TZ=Africa/Mogadishu

# Waxaan isku darnay update-ka iyo install-ka si uu dhismaha u noqdo mid degdeg ah
# Waxaan sidoo kale nadiifinay file-lasha aan loo baahneyn (rm -rf) si boos loo keydiyo
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Koobiyeynta requirements.txt
COPY requirements.txt /requirements.txt

# Ku shubista Python libraries-ka
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

# Sameynta folder-ka shaqada iyo koobiyeynta faylasha
WORKDIR /AV_FILE_TO_LINK
COPY . /AV_FILE_TO_LINK

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# Bilaabida Bot-ka
CMD ["python3", "bot.py"]
