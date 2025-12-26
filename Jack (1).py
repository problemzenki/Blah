# tele_userbot_full.py
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError
import random
import asyncio
import tempfile
import os
import traceback
# ====== CONFIG ======
api_id = {API_ID}
api_hash = "{API_HASH}"

# Owner IDs - only these can run commands
OWNER_IDS = {OWNER_IDS}

session_name = "userbot"
# ====== DATA (harmless defaults) ======
auto_replies = [

    "စောက်ခွက်ကို 360° လည့်ပြီးရိုက်ပစ်လိုက်မယ်",
    "မင်းအမေဖာသည်မကြီးကိုလမ်းထိပ်မှာတွေ့ခဲ့တယ်",
    "မင်းအမေကိုငါဆားသိပ်ပြီးလိုးလိုက်လို့ရှောသွားပြီရဖ",
    "မင်းအမေဖင်ခံတာကျွမ်းတယ်",
    "ငါလိုးမခွေးအူချက်",
    "၀က်ပေါက်ရေမင်းဘာစောက်ဆင့်ရှိသလဲ",
    "ငါလိုးမကြွက်အိကျိအိကျိနှင့်အူချက်",
    "မင်းအမေကိုလိုးလိုက်လို့ oh my fucking goodness ဖြစ်သွားမယ်",
    "မင်းအမေ bitch ဖင်ကြီးကိုသံကိုအပူပေးပြီးထိုးထည့်ပစ်မယ်",
    "မင်းစော်ဖင်ကြီးကိုက်ဆွဲပစ်မယ်",
    "မင်းအမေအသုဘငါရောက်ခဲ့တယ်ရဖ",
    "ဘောမတင်းနေတာလားတင်းနေရင်ဖင်ခံလိုက်",
    "ငါလိုးမကြွက်သခေါ",
    "ယျောင့်ငါးစိမ်သည်မသား",
    "ငါလိုးမသားမင်းလို stt တွေရှိလို့မြန်မာနိုင်ငံမတိုးတက်တာ",
    "ကိုမေကိုလိုးလေးမင်းလိုကောင်တွေဆဲချင်ရင်ငါ တယ်လီဂရမ်ရောက်လာတာ",
    "မင်းကြည့်လိုက်ရင်အမြဲခံနေရတာကြီးသနားလာပြီ",
    "ငါကလမ်းမတော်မှာဆျာလေမင်းကတော့ခွေးသာပေါ့",
    "ယျောင့်၀က်ကြီးကင်စားပစ်မယ်",
    "ယျောင့်မင်းအမေဖင်ထဲ cum ပစ်မယ်ကွာ",
    "မင်းကလစ်ကနှေးနေတယ်ဟ",
    "ဟုတ်တယ်ဟကုလားမဆိုတာမင်းအမ",
    "မင်းမမှီလို့စိတ်ဓာတ်ကျတာလား",
    "ဘာလဲချိဖငါကမြန်တယ်ပေါ့",
    "ဝက်ကြီးတို့မမြန်လို့တင်းနေပြီ",
    "မင်းအမေဖာသည်မအေကိုက်လို့ဝလုးချီးသုတ်ရမ်းတာလား",
    "မင်းအမေဖင်ကိုသရေကွင်းနဲ့သုံးချက်တိတိပြစ်ပေးမယ်",
    "အမ်းဟုတ်တယ်လေ ငါနိုင်တယ်",
    "ဟာဘောမ မင်းအမေမချစ်လို့လား",
    "ဟမ် မဟုတ်ပါဘူး မင်းအမေငါမလိုးပါဘူး",
    "အပြောကောင်းတယ်ဖင်ခံပလား",
    "ဘာလဲတောသားလောင်တာလား",
    "သေချာရေးလေ ကုလား",
    "မင်းဆရာငါဆိုတာလက်ခံတာလား",
    "ဟေ့ကောင်သတောင်းစားလေး",
    "ငါမလိုးပါ",
    "သခင်ငဒူးကမြတ်တယ်လေ",
    "အရှုံးမရှိသခင်ငဒူးလေ",
    "ငဒူးလာရင်အကုန်ပြေးကြတာပဲ",
    "အေးအဲ့တော့မင်းအမေသေတာလား",
    "လီးပဲဆဲနေတာတောင်အဓိပ္ပာယ်ရှိရှိဆဲတဲ့ငါ့ကိုအားကျစမ်းပါဟ",
    "လူတကားလိုးခံရတဲ့အမေကနေမွေးလာတဲ့သား",
    "ကြွက်မသား",
    "ဟိတ်ကောင်",
    "သေမယ်နော်",
    "ငါလိုးမ၀က်",
    "လက်တွေတုန်နေပြီးစာတွေတောင်မမှန်တော့ပါလားဟ",
    "တုန်ရမယ်လေ မင်းရင်ဆိုင်နေရတဲ့လူက သခင်လေညီ",
    "မနေ့တနေ့ကမှဆိုရှယ်ထဲဝင်လာပြီးအရှင်ဘုရင်ကိုပုန်ကန်တာသေဒဏ်နော်ခွေးရ",
    "ရုက္ခဆိုးလိုးမသား",
    "ငါလိုး ငါ့လောက်အထာမကျလို့ခိုးငိုနေတာလား",
    "တကယ့်ကောင် စောက်ရုပ်ဆိုး",
    "စောက်အထာကျနည်းသင်ပေးမယ်ဖေဖေခေါ်",
    "လီးဦးနှောက်နဲ့ခွေးမက လာယှဥ်နေတာ",
    "ဂျပိုးလိုးမသား",
    "အိမ်‌ေမြာင်လိုးမသား",
    "ကြွက်လိုးမသား",
    "ဒိုင်ဆိုဆောလိုးမသား",
    "ခွေးမျိုးတုံးခြင်နေတာခွေးမက",
    "မအေလိုးနာဇီမသား",
    "ယေရှူကိုးကွယ်တဲ့ကုလားဟလီးဘဲ",
    "ဘုရားသခင်လီးကျွေးပါစေ",
    "မင်းကိုကောင်းချီးပေးပြီးဖင်လိုးမှာလေစောက်ကုလား",
    "ဟိတ်၀က် နတ်ပြည်တာ၀တိံသာက အရှင်ဘုရင်ကြွလာပြီဖင်လိုးတော့မယ်ဟမင်းကို",
    "ငါလိုးးမကုလားစာထပ်ပို့ရင်အခိုင်းစေ",
    "ငါလိုးမကုလားကအခိုင်းစေလို့၀န်ခံတာဟငိငိ",
    "၀က်မသားတောင်းပန်လေလီးကြည့်နေတာလား",
    "ငါလိုးမခွေးဆဲရင်ငြိမ်ခံခုန်မကိုက်နဲ့",
    "ဖင်လိုးစခန်းကပါ ညီရေဖင်လိုးပါရစေ",
    "ဖင်လိုးခွင့်ပြုပါ",
    "မအေလိုးကလဲနဲနဲပဲစရသေးတယ်လောင်နေဘီ",
    "မင်းအမေအိမ်လွှတ်လိုက်ငါလိုးမသားမင်းအမေငါ့လိင်တံကြီးကိုကြိုက်နေတာမသိဘူးလား",
    "လိပ်မသားလားဟ",
    "လိပ်နဲ့တက်လိုးလို့ထွက်လာတဲ့ကောင်ကြနေတာဘဲ",
    "နှေးကွေးနေတာပဲစာတစ်လုံးနဲ့တစ်လုံးက",
    "မအေလိုးလေးရယ်မင်းစာတစ်ကြောင်းကငါ့စာလေးကြောင်းလောက်ထွက်တယ်ဟ",
    "ခွေးမသားကလဲငိုဖြဲဖြဲဖြစ်နေဘီဟ",
    "၀က်မလေးကုလားမသား",
    "ခွေးမသားလို့ပြောရင်လဲငါခွေးမသားဆိုပြီးဂုဏ်ယူနေမယ့်ကောင်ပဲဟ",
    "စာလုံးပေါင်းသတ်ပုံတောင်မမှန်ပဲဟောင်နေတာဟ",
    "ခွေးမလေးဟောင်ပြ",
    "သေမယ်၀က်မ မင်းအမေ၀က်မကိုစားပြ",
    "မအေလိုးရုပ်က ပဲရေပွကြော်ပဲစားနေရတဲ့စောက်ခွက်",
    "ကိုကြီးတို့လို ချိစ်ဘာဂါ မာလာရှမ်းကောတွေ မ၀ယ်စားနိုင်တာဆို",
    "ကြက်ဥကြော်ပဲနေ့တိုင်းစားနေရတာဆိုဆင်းရဲသား",
    "ငါလိုးမကုလားပဲဟင်းပဲစားရတာဆို",
    "မင်းအမေတညလွတ်လိုက်လေ ဖုန်းပြင်ခပေးမယ်လေ",
    "မင်းအမေကမင်းဖုန်းမှန်ကွဲနေတာမပြင်ပေးနိုင်တာဆို ပိုက်ဆံမရှိတာဆို",
    "မင်းဖုန်းမှန်ကွဲနေတာမလဲနိုင်တာဆို",
    "ဘယ်လိုလုပ်မလဲဟ",
    "ငါလိုးမသားလေးမင်းအဆဲခံနေရဘီဟ",
    "မအေလိုးမင်းကိုဆဲတယ် မင်းမိဘနှမငါတက်လိုး",
    "ချေပနိုင်စွမ်းမရှိလို့ဆိုညီက",
    "မအေလိုး လီးဖုန်းစောက်စုတ်နဲ့",
    "မင်းအမေဗစ်ခိုးပြီးရှုတာဆို",
    "သေမယ်နော်၀က်မ",
    "ငါလိုးမသား မင်းစာဘာအဓိပ္ပာယ်မှကိုမရှိဘူး စောက်ပညာမဲ့",
    "ငါလိုးမလိပ်နှေးကွေးနေတာပဲစာတစ်လုံးနဲ့တစ်လုံးဆို",
    "ကျွန် မသားတွေ ဖျော်ဖြေပေးစမ်းကွာ",
    "ငါလိုးမကုလားမင်းအမေသေဘီဆို",
    "မင်းအမေရက်လည်နေ့ကမလာနိုင်တာဆောတီးကွာ",
    "မင်းအဖေထောင်ကျနေတာလားဘာအမှုနဲ့လဲဟ",
    "မင်းအဖေ ခိုးမှုနဲ့ ထောင်ကျတာဆို",
    "ယျောင့် မင်း‌ထောင်ထွက်သားဆို",
    "ငါလိုးမစောက်တောသား",
    "ညီလိုင်းမကောင်းဘူးလား ဘာလဲ ဆင်းရဲလို့လား",
    "ညီတို့တောဘက်မှာ 4g internet မရဘူးလားဟ",
    "ငါလိုးမကုလား ဘေချေသုံးနေရတဲ့အဆင့်နဲ့",
    "မရှက်ဘူးလားဟ အမေလစ်ရင် ပိုက်ဆံခိုးတာ",
    "တနေ့မုန့်ဖိုး500ပဲရတာဆိုညီက",
    "စာတွေမမှန်ဘူးညီ မင်းအမေကျောင်းမထားနိုင်ဘူးလားဟ",
    "ငါလိုးမသားငါ့ကြောက်လို့လက်တုန်ပြီးစာမှန်ဘူးဆို",
    "ညီမင်းစာတွေထပ်နေတယ်ဘာလဲကြောက်လို့လား",
    "စောက်စုန်းလားလီးစုန်းလားလီးစုပ်စုန်းလားဟ",
    "ငါလိုးမကုလားသေမယ်",
    "မင်းအမေကိုမှန်းပြီးအာသာဖြေတာဆို",
    "မင်းအမေကိုမင်းဖေကလိင်မဆက်ဆံတော့မင်းအမေကသူများလိုးခိုင်းရတာဟ",
    "မင်းကဂေးဆိုညီငါသိတယ်နော်",
    "မင်းအဖေကဂေးဆိုညီ",
    "မင်းအ‌မေငါတက်လိုးလို့လူဖြစ်လာတာ မအာနဲ့ခွေးမသား"
    "မေမေ့သားလားဟ မင်းကလဲ ငါဆဲလို့ငိုယိုပြီးသွားတိုင်ရတယ်တဲ့",
    "မင်းအမေကိုသွာတိုင်နေတာလားဟ",
    "တကယ့်ကောင် ကိုယ့်အမေကိုသူများလိုးခိုင်းရတယ်လို့",
    "ဘာလဲမင်းစာမှန်အောင်ငါတက်လိုးပေးပြီးထွက်လာရင် မှန်မယ်ထင်တယ်",
    "တော်စမ်းခွေးရာ ခွေးစကားတွေစောက်ရမ်းပြောတယ်နော်",
    "ဖြည့်တွေ့ရအောင်မင်းက ဖြည့်တွေးပေးလိုရတဲ့စောက်ဆင့်ရှိရဲ့လား",
    "စာတွေကလဲလိပ်တက်လိုးလို့ထွက်လာတဲ့ကောင်ကျနေတာပဲ",
    "မနာလိုမှုတွေများပြီး မင်းငါစလို့ကြိတ်ခိုးလောင်နေတာဆို",
    "ဘာလဲငါ့ဆဲတဲ့စာကိုမင်းအရမ်းကြိုက်သွားတာလား",
    "ဟိတ်ခွေးမင်းငါ‌ဆဲသလိုပြန်ဆဲတာလား",
    "စောက်ရူးလို့ပြောရင်မင်းကိုယ်မင်းစောက်ရူးဆိုပြီးဂုဏ်ယူနေအုံးမယ်",
    "မင်အမေဗစ်ရာလေးတွေမြင်ပြီးလီးတောင်တာဆို",
    "မင်းအမေအာသာဖြေနေတာကိုမင်းချောင်းကြည့်ပြီးထုနေတာဆို၀က်ရ",
    "ညညမင်းအမေမှန်းထုတာဆိုညီ",
    "ငိုစမ်း",
    "ချေပနိုင်စွမ်းမရှိ",
    "လိုးတတ်တယ်မင်းအမကို",
    "ဦးနှောက်ဂုတ်ကပ်",
    "ဖာသည်မသားလေးလိုးခွဲပေးမယ်စာကိုလီးလောက်တတ်",
    "မင်းမေလိုးဖာသည်မသား ဘိတ်မရလို့ခိုးငိုတာလားဟ Typingကြတော့လဲနှေးကွေးဖာပိန်းမသား ငါနင်းတာက ငါလိုးရင်ငြိမ်နေ",
    "နှမလိုးလေး",
    "နွားမသား",
    "ငှက်လိုးမသား",
    "ဝက်မသား",
    "တောပိန်း",
    "ကုလား",
    "ရေငုပ်တာလား",
    "ဖေဖေခေါ်",
    "ငနုလေးစောက်ကုလား",
    "ဆရာခေါ်",
    "တပည့်",
    "နွားမသားခိုးငိုတာလားဟ",
    "ရိုက်ဟ",
    "ဖာသည်မသားရရိုက်‌လေဘာလို့ကြာနေတာလဲမင်းလက်ပျက်နေလို့လားငနုဖျင်းချက်ဘဲငါအတွက်ပျော်စရာမကောင်းဘူးပျင်းစရာဘဲ",
    "ဖာသည်မသားမင်းကိုငါ role အကျခံပြီးဆဲပေးနေတာကိုဘဲမင်းကျေးဇူးတင်သင့်တယ်။",
    "မင်းလိုကောင်မျိုးကိုငါ aura နှင့်တင်သတ်ပစ်လို့ရတယ်"
]


# ====== STATE ======
target_id = None           # /hell auto-reply target
hide_targets = set()       # automatically delete messages from these ids
_attacks = {}              # tid -> asyncio.Task for /attack
name_map = {}              # tid -> display name override

# Attack timing (modifiable with /speed)
# ====== Attack timing (modifiable with /speed) ======
# Safer limits: not below 0.7s and not above 1.0s
attack_interval = 0.9   # default (between min and max)
MIN_INTERVAL = 0.7
MAX_INTERVAL = 1.0

# ====== CLIENT ======
client = TelegramClient(session_name, api_id, api_hash)

# ====== HELPERS ======
def is_owner_event(event):
    return getattr(event, "sender_id", None) in OWNER_IDS

async def resolve_to_id(arg_or_none, event=None):
    """
    Resolve @username or numeric id or reply sender id.
    Raises ValueError on failure.
    """
    if arg_or_none:
        arg = arg_or_none.strip()
        if arg.startswith("@"):
            ent = await client.get_entity(arg)
            return ent.id
        else:
            return int(arg)
    elif event and event.is_reply:
        reply = await event.get_reply_message()
        if reply and reply.sender_id:
            return reply.sender_id
        raise ValueError("Reply message မတွေ့ပါ")
    else:
        raise ValueError("Argument မပေးထားပါ")

def make_clickable_name(name, userid):
    safe_name = str(name).replace("`", "'")
    return f"[{safe_name}](tg://user?id={userid})"

async def get_joined_groups():
    """Return dialogs that are groups or megagroups or channels where we can send."""
    dialogs = await client.get_dialogs()
    groups = []
    for d in dialogs:
        # include normal groups and megagroups and channels (you are a participant)
        entity = d.entity
        # some dialogs have .is_group/.is_channel flags; fallback checks:
        try:
            if getattr(entity, "megagroup", False) or getattr(entity, "broadcast", False) or getattr(d, "is_group", False) or getattr(d, "is_channel", False):
                groups.append(d)
            else:
                # also include basic groups
                if getattr(d, "is_group", False):
                    groups.append(d)
        except Exception:
            continue
    return groups

# ====== COMMANDS ======

# /help
@client.on(events.NewMessage(pattern=r"^/help$"))
async def help_cmd(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    help_text = """
💡 Userbot Commands Guide (owner only)

/hell <id|@username>       → Set auto-reply target (won't allow owners)
/stophell [id|@username]  → Stop auto-reply target
/attack <id|@username>    → Start continuous harmless attack (owner cannot be targeted)
/stop <id|@username>      → Stop attack
/speed <0.1-1.2|reset>    → Adjust attack interval
/name <id|@username> <name> → Set custom display name for mention
/delname <id|@username>   → Delete stored name
/hide <id|@username>      → Auto-delete messages from this id
/unhide <id|@username>    → Stop auto-delete
/id <id|@username|reply>  → Show resolved id
/delete                   → Log out and delete session
/send                     → Reply to a message then send that message to all joined groups
"""
    await event.respond(help_text)

# /id
@client.on(events.NewMessage(pattern=r"^/id(?: (.+))?$"))
async def get_id(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    arg = event.pattern_match.group(1)
    try:
        uid = await resolve_to_id(arg, event)
        await event.reply(f"`{uid}`", parse_mode="markdown")
    except Exception as e:
        await event.reply(f"❌ User မတွေ့ပါ: {e}")

# /name
@client.on(events.NewMessage(pattern=r"^/name (.+?) (.+)$"))
async def set_name(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    arg = event.pattern_match.group(1)
    display = event.pattern_match.group(2)
    try:
        tid = await resolve_to_id(arg, event)
        name_map[tid] = display
        await event.reply(f"✅ `{tid}` အတွက် name သတ်မှတ်ပြီး: {make_clickable_name(display, tid)}", parse_mode="markdown")
    except Exception as e:
        await event.reply(f"❌ Error setting name: {e}")

# /delname
@client.on(events.NewMessage(pattern=r"^/delname (.+)$"))
async def del_name(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    try:
        tid = await resolve_to_id(event.pattern_match.group(1), event)
        if tid in name_map:
            name_map.pop(tid)
            await event.reply(f"🗑 `{tid}` အတွက် name ဖျက်ပြီးပါပြီ", parse_mode="markdown")
        else:
            await event.reply(f"⚠️ `{tid}` အတွက် name မရှိပါ", parse_mode="markdown")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")

# /hide
@client.on(events.NewMessage(pattern=r"^/hide (.+)$"))
async def hide(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    try:
        tid = await resolve_to_id(event.pattern_match.group(1), event)
        hide_targets.add(tid)
        await event.reply(f"👻 Target hide enabled: `{tid}`", parse_mode="markdown")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")

# /unhide
@client.on(events.NewMessage(pattern=r"^/unhide (.+)$"))
async def unhide(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    try:
        tid = await resolve_to_id(event.pattern_match.group(1), event)
        hide_targets.discard(tid)
        await event.reply(f"👻 Target hide disabled: `{tid}`", parse_mode="markdown")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")

# /hell (set auto-reply target)
@client.on(events.NewMessage(pattern=r"^/hell (.+)$"))
async def hell(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    try:
        tid = await resolve_to_id(event.pattern_match.group(1), event)
        if tid in OWNER_IDS:
            await event.reply("Owner ကို auto-reply target အဖြစ် သတ်မှတ်၍ မရပါ။", parse_mode="markdown")
            return
        global target_id
        target_id = tid
        await event.reply(f" Auto-reply Target သတ်မှတ်ပြီး: `{tid}`", parse_mode="markdown")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")

# /stophell
@client.on(events.NewMessage(pattern=r"^/stophell(?: (.+))?$"))
async def stophell(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    try:
        arg = event.pattern_match.group(1)
        global target_id
        if arg:
            tid = await resolve_to_id(arg, event)
            if target_id == tid:
                target_id = None
                await event.reply(" Auto-reply ပိတ်ပြီး Target ဖျက်ပြီးပါပြီ", parse_mode="markdown")
            else:
                await event.reply(" Target မဟုတ်ပါ")
        else:
            target_id = None
            await event.reply(" Auto-reply ပိတ်ပြီး Target ဖျက်ပြီးပါပြီ", parse_mode="markdown")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")


# /speed
@client.on(events.NewMessage(pattern=r"^/speed(?:\s+(.+))?$"))
async def speed_cmd(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    global attack_interval
    arg = event.pattern_match.group(1)
    try:
        if not arg:
            await event.reply(f"⚙️ Current attack interval: {attack_interval}s (min {MIN_INTERVAL}, max {MAX_INTERVAL})", parse_mode="markdown")
            return
        arg = arg.strip().lower()
        if arg in ("reset","default"):
            attack_interval = 0.9  # reset to safer default within bounds
            await event.reply(f" Attack interval reset to default: {attack_interval}s", parse_mode="markdown")
            return
        val = float(arg)
        # enforce the requested bounds: at least 0.7, at most 1.0
        if val < MIN_INTERVAL or val > MAX_INTERVAL:
            await event.reply(f"❌ Interval must be between {MIN_INTERVAL} and {MAX_INTERVAL} seconds")
            return
        attack_interval = val
        await event.reply(f"✅ Attack interval set to: {attack_interval}s", parse_mode="markdown")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")


# =========================
# ATTACK LOOP (NO ERROR)
# =========================
async def _attack_loop(send_target, tid, display):
    if tid in OWNER_IDS:
        return

    try:
        while True:
            task = _attacks.get(tid)
            if task is None or task.cancelled() or task is not asyncio.current_task():
                break

            replies = random.sample(auto_replies, min(2, max(1, len(auto_replies))))

            for r in replies:
                task = _attacks.get(tid)
                if task is None or task.cancelled() or task is not asyncio.current_task():
                    break

                try:
                    await client.send_message(
                        send_target,
                        f"{display} {r}",
                        parse_mode="markdown"
                    )

                except FloodWaitError as e:
                    wait = int(getattr(e, "seconds", 0)) or 1
                    await asyncio.sleep(wait)
                    try:
                        await client.send_message(
                            send_target,
                            f"{display} {r}",
                            parse_mode="markdown"
                        )
                    except Exception:
                        pass

                except Exception:
                    pass

                await asyncio.sleep(max(attack_interval, 0.8) + random.uniform(0, 0.05))

            await asyncio.sleep(max(attack_interval, 0.8))

    except asyncio.CancelledError:
        pass
    finally:
        _attacks.pop(tid, None)


# =========================
# /attack COMMAND (AUTO GROUP / DM DETECT)
# =========================
@client.on(events.NewMessage(pattern=r"^/attack (.+)$"))
async def attack_cmd(event):
    if not is_owner_event(event):
        await event.delete()
        return

    await event.delete()

    try:
        tid = await resolve_to_id(event.pattern_match.group(1), event)

        if tid in OWNER_IDS:
            await event.reply("Owner ကို attack လုပ်မရပါ။", parse_mode="markdown")
            return

        if tid in _attacks:
            await event.reply(
                f"⚠️ `{tid}` အပေါ် attack already running",
                parse_mode="markdown"
            )
            return

        # ✅ Prepare Clickable Display Name
        display_name = name_map.get(tid)
        if not display_name:
            try:
                ent = await client.get_entity(tid)
                display_name = getattr(ent, "first_name", str(tid)) or str(tid)
            except Exception:
                display_name = str(tid)

        display = make_clickable_name(display_name, tid)

        # ✅ AUTO DETECT SEND PLACE
        if event.is_private:
            send_target = tid            # ✅ DM → Target DM
            place = "DM"
        else:
            send_target = event.chat_id # ✅ Group → Same Group
            place = "GROUP"

        # ✅ Start Attack Task
        _attacks[tid] = asyncio.create_task(
            _attack_loop(send_target, tid, display)
        )

        await event.reply(
            f"🚀 Attack started on `{tid}` in {place}\n{display}",
            parse_mode="markdown"
        )

    except Exception as e:
        await event.reply(f"❌ Error: {e}")


# =========================
# /stop COMMAND (NO ERROR)
# =========================
@client.on(events.NewMessage(pattern=r"^/stop (.+)$"))
async def stop_cmd(event):
    if not is_owner_event(event):
        await event.delete()
        return

    await event.delete()

    try:
        tid = await resolve_to_id(event.pattern_match.group(1), event)

        task = _attacks.get(tid)
        if not task:
            await event.reply(
                f"❗ `{tid}` အတွက် running attack မရှိပါ",
                parse_mode="markdown"
            )
            return

        task.cancel()
        _attacks.pop(tid, None)

        await event.reply(
            f"🛑 Attack stopped: `{tid}`",
            parse_mode="markdown"
        )

    except Exception as e:
        await event.reply(f"❌ Error: {e}")


# /delete (logout)
@client.on(events.NewMessage(pattern=r"^/delete$"))
async def delete_session(event):
    if not is_owner_event(event):
        await event.delete(); return
    await event.delete()
    await event.reply("🗑 Logging out and deleting session...")
    await client.log_out()

# ===== /send (broadcast reply to all joined groups) =====
@client.on(events.NewMessage(pattern=r"^/send$"))
async def send_all_groups(event):
    if not is_owner_event(event):
        await event.delete(); return

    if not event.is_reply:
        await event.reply("Reply to a message (text/photo/video/doc) and then use /send to broadcast it to all joined groups.")
        return

    await event.delete()
    reply_msg = await event.get_reply_message()
    await event.reply("📤 စတင်ပို့နေပါတယ် — gathering groups...")

    groups = await get_joined_groups()
    total = len(groups)
    sent = 0
    failed = 0

    # download media to temp file if any
    temp_path = None
    try:
        if reply_msg.media:
            temp_path = await reply_msg.download_media(file=tempfile.gettempdir())

        for d in groups:
            gid = d.id
            try:
                if reply_msg.media and temp_path:
                    caption = reply_msg.text or None
                    try:
                        await client.send_file(gid, temp_path, caption=caption)
                    except FloodWaitError as e:
                        wait = int(getattr(e, "seconds", 0)) or 1
                        print(f"⏳ FloodWait {wait}s while sending file to {gid} — sleeping...")
                        await asyncio.sleep(wait)
                        await client.send_file(gid, temp_path, caption=caption)
                else:
                    text = reply_msg.text or ""
                    if text.strip() == "":
                        continue
                    try:
                        await client.send_message(gid, text)
                    except FloodWaitError as e:
                        wait = int(getattr(e, "seconds", 0)) or 1
                        print(f"⏳ FloodWait {wait}s while sending msg to {gid} — sleeping...")
                        await asyncio.sleep(wait)
                        await client.send_message(gid, text)

                sent += 1
                await asyncio.sleep(1.2)  # safe pause between groups
            except Exception as e:
                failed += 1
                print(f"Failed to send to {getattr(d, 'name', d.id)} ({gid}): {e}")
                await asyncio.sleep(1.0)
    finally:
        try:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)
        except Exception:
            pass

    await event.reply(f"✅ Done — sent: {sent}, failed: {failed}, total groups: {total}")

# ===== Auto reply global handler (hell target + hide) =====
@client.on(events.NewMessage)
async def auto_reply(event):
    global target_id, hide_targets
    try:
        sender = await event.get_sender()
        if not sender or not getattr(sender, "id", None):
            return
        sid = sender.id

        # auto-delete messages from hide_targets
        if sid in hide_targets:
            try:
                await event.delete()
            except Exception:
                pass
            return

        # never auto-reply to owners
        if sid in OWNER_IDS:
            return

        # hell auto-reply: if target matches sender
        if target_id and sid == target_id:
            mention = make_clickable_name(name_map.get(sid, getattr(sender, "first_name", str(sid))), sid)
            replies = random.sample(auto_replies, min(2, len(auto_replies)))
            for r in replies:
                try:
                    await event.reply(f"{mention} {r}", parse_mode="markdown")
                except Exception:
                    pass
    except Exception:
        # ignore unexpected errors in global handler
        traceback.print_exc()

# ===== RUN =====
# ===== RUN =====

def start_bot():
    print("🔐 Connecting Telegram (SAFE MODE)...")
    client.start()

    print(f"🛡️ Warm-up {SAFE_WARMUP} seconds — NO ACTION")
    time.sleep(SAFE_WARMUP)

    print("🟢 SAFE MODE OFF — bot active now")
    client.run_until_disconnected()

if __name__ == "__main__":
    start_bot()
