{
    "name": "@ronak0910 movie bot",
    "description": "When you going to send file on telegram channel this bot will save that in database, So you can search that easily in inline mode",
    "stack": "container",
    "keywords": [
      "telegram",
      "auto-filter",
      "filter",
      "best",
      "indian",
      "pyrogram",
      "media",
      "search",
      "channel",
      "index",
      "inline"
    ],
    "website": "https://github.com/@ronak0910/MovieBot",
    "repository": "https://github.com/@ronak0910/MovieBot",
    "env": {
        "BOT_TOKEN": {
            "description": "Your bot token.",
            "required": true
        },
        "API_ID": {
            "description": "Get this value from https://my.telegram.org",
            "required": true
        },
        "API_HASH": {
            "description": "Get this value from https://my.telegram.org",
            "required": true
        },
        "CHANNELS": {
            "description": "Username or ID of channel or group. Separate multiple IDs by space.",
            "required": false
        },
        "ADMINS": {
            "description": "Username or ID of Admin. Separate multiple Admins by space.",
            "required": true
        },
        "PICS": {
            "description": "Add some telegraph link of pictures .",
            "required": false
        },
        "LOG_CHANNEL": {
            "description": "Bot Logs,Give a channel id with -100xxxxxxx",
            "required": true
        },
        "SUPPORT_CHAT": {
            "description": "Username of a Support Group / ADMIN. ( Should be username without @ and not ID)",
            "required": false
        },
        "AUTH_USERS": {
            "description": "Username or ID of users to give access of inline search. Separate multiple users by space.\nLeave it empty if you don't want to restrict bot usage.",
            "required": false
        },
        "AUTH_CHANNEL": {
            "description": "ID of channel.Make sure bot is admin in this channel. Without subscribing this channel users cannot use bot.",
            "required": false
        },   
        "USE_CAPTION_FILTER": {
            "description": "Whether bot should use captions to improve search results. (True False)",
            "required": false
        },
        "CUSTOM_FILE_CAPTION": {
            "description": "A custom file caption for your files. formatable with , file_name, file_caption, file_size, Read Readme.md for better understanding.",
            "required": false
        },
        "DATABASE_URI": {
            "description": "mongoDB URI. Get this value from https://www.mongodb.com. For more help watch this video - https://youtu.be/dsuTn4qV2GA",
            "required": true
        },
        "DATABASE_NAME": {
            "description": "Name of the database in mongoDB. For more help watch this video - https://youtu.be/dsuTn4qV2GA",
            "required": false
        },
        "COLLECTION_NAME": {
            "description": "Name of the collections. Defaults to Telegram_files. If you are using the same database, then use different collection name for each bot",
            "value": "Telegram_files",
            "required": false
        },
        "CACHE_TIME": {
            "description": "The maximum amount of time in seconds that the result of the inline query may be cached on the server",
            "value": "300",
            "required": false
        },
        "IMDB": {
            "description": "Imdb, the view of information when making True/False ",
            "required": false
        },
        "SINGLE_BUTTON": {
            "description": "choose b/w single or double buttons",
            "required": false
        },
        "P_TTI_SHOW_OFF": {
            "description": "Customize Result Buttons to Callback or Url by (True = url / False = callback)",
            "required": false
        }
    },
    "addons": [],
    "buildpacks": [{
        "url": "heroku/python"
    }],
    "formation": {
        "worker": {
            "quantity": 1,
            "size": "free"
        }
    }
}
