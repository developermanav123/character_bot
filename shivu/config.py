class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5744615352"
    sudo_users = "5744615352", "7147738922"
    GROUP_ID = -1002244950802
    TOKEN = "6812839917:AAHdWH1QAnHGtS8TWMfGHY_ZyqMTJsPiRRc"
    mongo_url =
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "-1002159228892"
    UPDATE_CHAT = "-1002202067318"
    BOT_USERNAME = "chracter_bot"
    CHARA_CHANNEL_ID = "-1002244950802"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
