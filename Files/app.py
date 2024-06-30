import pybase64
import base64
import requests
import binascii
import os

# Define a fixed timeout for HTTP requests
TIMEOUT = 20  # seconds

# Define the fixed text for the initial configuration
fixed_text = """#profile-title: base64:8J+GkyBHaXRodWIgfCBCYXJyeS1mYXIg8J+ltw==
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/coldwater-10/V2ray-Config
#profile-web-page-url: https://github.com/coldwater-10/V2ray-Config
"""

# Base64 decoding function
def decode_base64(encoded):
    decoded = ""
    for encoding in ["utf-8", "iso-8859-1"]:
        try:
            decoded = pybase64.b64decode(encoded + b"=" * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded

# Function to decode base64-encoded links with a timeout
def decode_links(links):
    decoded_data = []
    for link in links:
        try:
            response = requests.get(link, timeout=TIMEOUT)
            encoded_bytes = response.content
            decoded_text = decode_base64(encoded_bytes)
            decoded_data.append(decoded_text)
        except requests.RequestException:
            pass  # If the request fails or times out, skip it
    return decoded_data

# Function to decode directory links with a timeout
def decode_dir_links(dir_links):
    decoded_dir_links = []
    for link in dir_links:
        try:
            response = requests.get(link, timeout=TIMEOUT)
            decoded_text = response.text
            decoded_dir_links.append(decoded_text)
        except requests.RequestException:
            pass  # If the request fails or times out, skip it
    return decoded_dir_links

# Filter function to select lines based on specified protocols
def filter_for_protocols(data, protocols):
    filtered_data = []
    for line in data:
        if any(protocol in line for protocol in protocols):
            filtered_data.append(line)
    return filtered_data

# Create necessary directories if they don't exist
def ensure_directories_exist():
    output_folder = os.path.abspath(os.path.join(os.getcwd(), ".."))
    base64_folder = os.path.join(output_folder, "Base64")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(base64_folder):
        os.makedirs(base64_folder)

    return output_folder, base64_folder

# Main function to process links and write output files
def main():
    output_folder, base64_folder = ensure_directories_exist()  # Ensure directories are created

    protocols = ["vmess", "vless", "trojan", "ss", "ssr", "hy2", "tuic", "warp://"]
    links = [
        "http://104.168.107.230/aggregate.txt",
        "http://sub.giga-downloader.com/clean.txt",
        "http://sub.giga-downloader.com/hiddify.txt",
        "https://alienvpn402.github.io/AlienVPN402-subscribe-servers-sing-box",
        "https://alienvpn402.github.io/AlienVPN402-subscribe-servers",
        "https://api.yebekhe.link/shervin",
        "https://miner.isherv.in",
        "https://raw.githubusercontent.com/1Shervin/Sub/main/v2ray",
        "https://bamarambash.monster/subscriptions/b8767a6a-1c30-11ee-ba76-9ee097a90b8b",
        "https://branch.blanku.me",
        "https://confighub.site/sub.txt",
        "https://drive.google.com/uc?export=download&id=1Gkg2Ru0fO7-4UDNEks5vBWEXih-6_DKW",
        "https://eliv2ray.cloud/Mixed-Elena-Sub.json",
        "https://eliv2ray.cloud/Mixed-Sub-ELENA.txt",
        "https://eliv2ray.cloud/TLS-MCI-By-ELiV2RAY.txt",
        "https://eliv2ray.cloud/New-Sub-ELiV2ray.txt",
        "https://eliv2ray.cloud/Join-ELiV2RaY.txt#Elena",
        "https://eliv2ray.cloud/Vmess-Shadowsocks-Sub.txt#elena",
        "https://freevpn878.hamidimorteza680.workers.dev/sub",
        "https://gist.githubusercontent.com/johhny1898/eef96d3998241a8527bbb9557704d6bb/raw/0e6ff0583ca5e226e82756d0f602ae18d6ac5a9b/gistfile1.txt",
        "https://igdux.top/~Nekobox",
        "https://links.achaemenidempireofpersia.uk/cR3Q5X#IrancpinetSub1",
        "https://sub1.achaemenidempireofpersia.uk#IrancpinetSub2",
        "https://sub2.achaemenidempireofpersia.uk/#irancpinetSub3",
        "https://sub3.achaemenidempireofpersia.uk/#irancpinetSub4",
        "https://links.achaemenidempireofpersia.uk/8HjGm3",
        "https://links.achaemenidempireofpersia.uk/afDNsf#IranCPI_shdwtls2",
        "https://links.achaemenidempireofpersia.uk/4rYbN5#IranCPI_shdwtls2_IPV6",
        "https://links.achaemenidempireofpersia.uk/PjXNif#Hiddify_CPI_temp",
        "https://msdonor.pages.dev/sub/7f035a95-4b51-4e0b-8995-59864a9cde22#BPB-Normal",
        "https://panel.quickservice.sbs/gWQfDehzDHyfmKXWUK9N4sSL6fRn/2d0c6203-f715-4b14-973a-ac25e560b03e/all.txt?name=panel.quickservice.sbs-unknown&asn=unknown&mode=new",
        "https://qiaomenzhuanfx.netlify.app",
        "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/server.txt",
        "https://raw.githubusercontent.com/Airuop/cross/master/sub/sub_merge.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/SS-Kcptun/ssconfig.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/SSR/ssconfig.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/ssconfig.txt",
        "https://raw.githubusercontent.com/Ashkan-m/v2ray/main/Sub.txt",
        "https://raw.githubusercontent.com/Ashkan-m/v2ray/main/Sub_NoTest.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/blues.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/kkzui.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/merged.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/nodefree.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/v2rayshare.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/wenode.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/yudou66.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/zyfxs.txt",
        "https://raw.githubusercontent.com/Crusader-Strike/AKBConf/main/AKBConfigs.txt",
        "https://raw.githubusercontent.com/Ennzo0/V2ray/main/all.txt",
        "https://raw.githubusercontent.com/HDYOU/porxy/main/combine.txt",
        "https://raw.githubusercontent.com/ImMyron/V2ray/main/Telegram",
        "https://raw.githubusercontent.com/ImMyron/V2ray/main/Web",
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config",
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/newconfig",
        "https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/actives.txt",
        "https://raw.githubusercontent.com/MrPooyaX/SansorchiFucker/main/data.txt",
        "https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/Shenzo.txt",
        "https://raw.githubusercontent.com/NiREvil/vless/main/sub/G-Core",
        "https://raw.githubusercontent.com/NiREvil/vless/main/sub/SSTime",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/checked",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/temporary",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/vmess",
        "https://raw.githubusercontent.com/ResistalProxy/V2Ray/master/server.txt",
        "https://raw.githubusercontent.com/Restia-Ashbell/cf_vless_sub/main/sub",
        "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Raw",
        "https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/main/sub64",
        "https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/master/Eternity",
        "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Raw",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity",
        "https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/main/submerge/converted.txt",
        "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Realm",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity.txt",
        "https://raw.githubusercontent.com/Vauth/node/main/Main",
        "https://raw.githubusercontent.com/Vauth/node/main/Pro",
        "https://raw.githubusercontent.com/abshare/abshare.github.io/main/README.md",
        "https://raw.githubusercontent.com/adoxnet/subV2ray/main/biit.txt",
        "https://raw.githubusercontent.com/adoxnet/subV2ray/main/oxnet_ir.txt",
        "https://raw.githubusercontent.com/allenfengjr/VlessSub/main/sub",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/MCI.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/Mobinet.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/Mokhabrat.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/Rightel.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/irancell.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/shatel.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/various",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Reality-Azadi-config/Config/Azadi-Reality-Different",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Reality-Azadi-config/Config/Config",
        "https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/all",
        "https://raw.githubusercontent.com/dimzon/scaling-sniffle/main/all-sort.txt",
        "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUB/main/BASE64.txt",
        "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUB/main/v2ray.txt",
        "https://raw.githubusercontent.com/halfaaa/Free/main/1.30.2023.txt",
        "https://raw.githubusercontent.com/hfarahani/vv/main/co.txt",
        "https://mrsp137.github.io/NewSub_FREEV2RNG/@FREEV2RNG#FreeV2rng-1",
        "https://raw.githubusercontent.com/hkaa0/permalink/main/proxy/V2ray",
        "https://raw.githubusercontent.com/kaoxindalao/v2raycheshi/main/v2raycheshi",
        "https://raw.githubusercontent.com/lflflf999/0516/main/BX-JD",
        "https://raw.githubusercontent.com/liketolivefree/kobabi/main/4mom.txt",
        "https://raw.githubusercontent.com/liketolivefree/kobabi/main/4sam.txt",
        "https://raw.githubusercontent.com/liketolivefree/kobabi/main/sub.txt",
        "https://raw.githubusercontent.com/liketolivefree/kobabi/main/sub_all.txt",
        "https://raw.githubusercontent.com/m3hdio1/v2ray_sub/main/v2ray_sub.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_1.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_2.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_3.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_4.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_1.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_2.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_3.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_4.txt",
        "https://raw.githubusercontent.com/mianfeifq/share/main/README.md",
        "https://raw.githubusercontent.com/mksshare/mksshare.github.io/main/README.md",
        "https://raw.githubusercontent.com/mlabalabala/v2ray-node/main/vm_static_node.txt",
        "https://raw.githubusercontent.com/moeinkey/key/main/new",
        "https://raw.githubusercontent.com/moeinkey/key/main/ssh",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/default.txt",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/lt-sub.txt",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/my.txt",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/ru.txt",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/speed.txt",
        "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list_raw.txt",
        "https://raw.githubusercontent.com/rb360full/V2Ray-Configs/main/Reza-2",
        "https://raw.githubusercontent.com/renyige1314/CLASH/main/CLASH",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/best",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/best.txt",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/mirza-all.txt",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/sub",
        "https://raw.githubusercontent.com/rezaxanii/Config-Station/main/configs.txt",
        "https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config_64base",
        "https://raw.githubusercontent.com/shabane/kamaji/master/hub/ss.txt",
        "https://raw.githubusercontent.com/shabane/kamaji/master/hub/trojan.txt",
        "https://raw.githubusercontent.com/shabane/kamaji/master/hub/vmess.txt",
        "https://raw.githubusercontent.com/shirkerboy/scp/main/sub",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/ss.txt",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/ssr.txt",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/trojan.txt",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/vmess.txt",
        "https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt",
        "https://raw.githubusercontent.com/theGreatPeter/v2rayNodes/main/nodes.txt",
        "https://raw.githubusercontent.com/tolinkshare/freenode/main/README.md",
        "https://raw.githubusercontent.com/tristan-deng/v2rayNodesSelected/main/MyNodes.txt",
        "https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/o/node.txt",
        "https://raw.githubusercontent.com/wudongdefeng/free/main/freevm/list_raw.txt",
        "https://raw.githubusercontent.com/xc0000e9/deatnote/main/Hiddify-next.fragment",
        "https://raw.githubusercontent.com/xc0000e9/deatnote/main/Test.txt",
        "https://raw.githubusercontent.com/ysmoradi/sub/main/clean.txt",
        "https://raw.githubusercontent.com/ysmoradi/sub/main/hiddify.txt",
        "https://rentry.co/8tq7w82x/raw",
        "https://rentry.co/DailyV2ry/raw",
        "https://gfw.mahsa/Mahsa",
        "https://zebelkhan10.fallahpour25.workers.dev/sub/74f829f3-480b-4e7f-8039-9418d055375b",
        "https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged_base64",
        "https://zebelkhan10.fallahpour25.workers.dev/sub/74f829f3-480b-4e7f-8039-9418d055375b",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/donated",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/mix_base64",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/vmess",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/trojan",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/shadowsocks",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/vmess",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/trojan",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/ss",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/splitted/mixed",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/shadowsocks",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/shadowsocks",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/ss_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/trojan_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/vmess_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/vmess_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/ss_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/trojan_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/merged",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/merged_base64",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub4/main/merged",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub4/main/merged_base64",
        "https://paste.gg/p/anonymous/21b6068195f14f7fac5f4f9a4cc77ac6/files/2e54b7f9fc5242bd82f804cb32ce9065/raw",
        "https://paste.gg/p/anonymous/b6094968dd974a5ba018ba9117655326/files/05c585aa155a4c54a0fcfab32403154e/raw",
        "https://dy.smjc.top/api/v1/client/subscribe?token=b12651a704cf680e5794f61827a46262",
        "https://dy.smjc.top/api/v1/client/subscribe?token=5bd7e01f6a299be186e5cd44f9c6c150",
        "https://paste.gg/p/anonymous/3f0c979d8eca4e5bb0be491e69c89501/files/990f7294ea214770a6fb04a336670f48/raw",
        "https://ninjasub.com/link/b1UjtCoAZeyyCFqE?clash=1",
        "https://yiyolink.xyz/link/J6OpSJ9lfi1YHzQI?clash=1",
        "https://yiyolink.xyz/link/J6OpSJ9lfi1YHzQI?sub=1",
        "https://yiyolink.xyz/link/J6OpSJ9lfi1YHzQI?sub=2",
    ]
    dir_links = [
        "http://104.168.107.230/aggregate.txt",
        "http://sub.giga-downloader.com/clean.txt",
        "http://sub.giga-downloader.com/hiddify.txt",
        "https://alienvpn402.github.io/AlienVPN402-subscribe-servers-sing-box",
        "https://alienvpn402.github.io/AlienVPN402-subscribe-servers",
        "https://api.yebekhe.link/shervin",
        "https://miner.isherv.in",
        "https://raw.githubusercontent.com/1Shervin/Sub/main/v2ray",
        "https://bamarambash.monster/subscriptions/b8767a6a-1c30-11ee-ba76-9ee097a90b8b",
        "https://branch.blanku.me",
        "https://confighub.site/sub.txt",
        "https://drive.google.com/uc?export=download&id=1Gkg2Ru0fO7-4UDNEks5vBWEXih-6_DKW",
        "https://eliv2ray.cloud/Mixed-Elena-Sub.json",
        "https://eliv2ray.cloud/Mixed-Sub-ELENA.txt",
        "https://eliv2ray.cloud/TLS-MCI-By-ELiV2RAY.txt",
        "https://eliv2ray.cloud/New-Sub-ELiV2ray.txt",
        "https://eliv2ray.cloud/Join-ELiV2RaY.txt#Elena",
        "https://eliv2ray.cloud/Vmess-Shadowsocks-Sub.txt#elena",
        "https://freevpn878.hamidimorteza680.workers.dev/sub",
        "https://gist.githubusercontent.com/johhny1898/eef96d3998241a8527bbb9557704d6bb/raw/0e6ff0583ca5e226e82756d0f602ae18d6ac5a9b/gistfile1.txt",
        "https://igdux.top/~Nekobox",
        "https://links.achaemenidempireofpersia.uk/cR3Q5X#IrancpinetSub1",
        "https://sub1.achaemenidempireofpersia.uk#IrancpinetSub2",
        "https://sub2.achaemenidempireofpersia.uk/#irancpinetSub3",
        "https://sub3.achaemenidempireofpersia.uk/#irancpinetSub4",
        "https://links.achaemenidempireofpersia.uk/8HjGm3",
        "https://links.achaemenidempireofpersia.uk/afDNsf#IranCPI_shdwtls2",
        "https://links.achaemenidempireofpersia.uk/4rYbN5#IranCPI_shdwtls2_IPV6",
        "https://links.achaemenidempireofpersia.uk/PjXNif#Hiddify_CPI_temp",
        "https://msdonor.pages.dev/sub/7f035a95-4b51-4e0b-8995-59864a9cde22#BPB-Normal",
        "https://panel.quickservice.sbs/gWQfDehzDHyfmKXWUK9N4sSL6fRn/2d0c6203-f715-4b14-973a-ac25e560b03e/all.txt?name=panel.quickservice.sbs-unknown&asn=unknown&mode=new",
        "https://qiaomenzhuanfx.netlify.app",
        "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/server.txt",
        "https://raw.githubusercontent.com/Airuop/cross/master/sub/sub_merge.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/SS-Kcptun/ssconfig.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/SSR/ssconfig.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/ssconfig.txt",
        "https://raw.githubusercontent.com/Ashkan-m/v2ray/main/Sub.txt",
        "https://raw.githubusercontent.com/Ashkan-m/v2ray/main/Sub_NoTest.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/blues.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/kkzui.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/merged.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/nodefree.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/v2rayshare.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/wenode.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/yudou66.txt",
        "https://raw.githubusercontent.com/Barabama/FreeNodes/master/nodes/zyfxs.txt",
        "https://raw.githubusercontent.com/Crusader-Strike/AKBConf/main/AKBConfigs.txt",
        "https://raw.githubusercontent.com/Ennzo0/V2ray/main/all.txt",
        "https://raw.githubusercontent.com/HDYOU/porxy/main/combine.txt",
        "https://raw.githubusercontent.com/ImMyron/V2ray/main/Telegram",
        "https://raw.githubusercontent.com/ImMyron/V2ray/main/Web",
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config",
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/newconfig",
        "https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/actives.txt",
        "https://raw.githubusercontent.com/MrPooyaX/SansorchiFucker/main/data.txt",
        "https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/Shenzo.txt",
        "https://raw.githubusercontent.com/NiREvil/vless/main/sub/G-Core",
        "https://raw.githubusercontent.com/NiREvil/vless/main/sub/SSTime",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/checked",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/temporary",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/vmess",
        "https://raw.githubusercontent.com/ResistalProxy/V2Ray/master/server.txt",
        "https://raw.githubusercontent.com/Restia-Ashbell/cf_vless_sub/main/sub",
        "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Raw",
        "https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/main/sub64",
        "https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/master/Eternity",
        "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Raw",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity",
        "https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/main/submerge/converted.txt",
        "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Realm",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity.txt",
        "https://raw.githubusercontent.com/Vauth/node/main/Main",
        "https://raw.githubusercontent.com/Vauth/node/main/Pro",
        "https://raw.githubusercontent.com/abshare/abshare.github.io/main/README.md",
        "https://raw.githubusercontent.com/adoxnet/subV2ray/main/biit.txt",
        "https://raw.githubusercontent.com/adoxnet/subV2ray/main/oxnet_ir.txt",
        "https://raw.githubusercontent.com/allenfengjr/VlessSub/main/sub",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/MCI.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/Mobinet.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/Mokhabrat.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/Rightel.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/irancell.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/shatel.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/various",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Reality-Azadi-config/Config/Azadi-Reality-Different",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Reality-Azadi-config/Config/Config",
        "https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/all",
        "https://raw.githubusercontent.com/dimzon/scaling-sniffle/main/all-sort.txt",
        "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUB/main/BASE64.txt",
        "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUB/main/v2ray.txt",
        "https://raw.githubusercontent.com/halfaaa/Free/main/1.30.2023.txt",
        "https://raw.githubusercontent.com/hfarahani/vv/main/co.txt",
        "https://mrsp137.github.io/NewSub_FREEV2RNG/@FREEV2RNG#FreeV2rng-1",
        "https://raw.githubusercontent.com/hkaa0/permalink/main/proxy/V2ray",
        "https://raw.githubusercontent.com/kaoxindalao/v2raycheshi/main/v2raycheshi",
        "https://raw.githubusercontent.com/lflflf999/0516/main/BX-JD",
        "https://raw.githubusercontent.com/liketolivefree/kobabi/main/4mom.txt",
        "https://raw.githubusercontent.com/liketolivefree/kobabi/main/4sam.txt",
        "https://raw.githubusercontent.com/liketolivefree/kobabi/main/sub.txt",
        "https://raw.githubusercontent.com/liketolivefree/kobabi/main/sub_all.txt",
        "https://raw.githubusercontent.com/m3hdio1/v2ray_sub/main/v2ray_sub.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_1.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_2.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_3.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_4.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_1.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_2.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_3.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_4.txt",
        "https://raw.githubusercontent.com/mianfeifq/share/main/README.md",
        "https://raw.githubusercontent.com/mksshare/mksshare.github.io/main/README.md",
        "https://raw.githubusercontent.com/mlabalabala/v2ray-node/main/vm_static_node.txt",
        "https://raw.githubusercontent.com/moeinkey/key/main/new",
        "https://raw.githubusercontent.com/moeinkey/key/main/ssh",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/default.txt",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/lt-sub.txt",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/my.txt",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/ru.txt",
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/speed.txt",
        "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list_raw.txt",
        "https://raw.githubusercontent.com/rb360full/V2Ray-Configs/main/Reza-2",
        "https://raw.githubusercontent.com/renyige1314/CLASH/main/CLASH",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/best",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/best.txt",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/mirza-all.txt",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/sub",
        "https://raw.githubusercontent.com/rezaxanii/Config-Station/main/configs.txt",
        "https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config_64base",
        "https://raw.githubusercontent.com/shabane/kamaji/master/hub/ss.txt",
        "https://raw.githubusercontent.com/shabane/kamaji/master/hub/trojan.txt",
        "https://raw.githubusercontent.com/shabane/kamaji/master/hub/vmess.txt",
        "https://raw.githubusercontent.com/shirkerboy/scp/main/sub",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/ss.txt",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/ssr.txt",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/trojan.txt",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/vmess.txt",
        "https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt",
        "https://raw.githubusercontent.com/theGreatPeter/v2rayNodes/main/nodes.txt",
        "https://raw.githubusercontent.com/tolinkshare/freenode/main/README.md",
        "https://raw.githubusercontent.com/tristan-deng/v2rayNodesSelected/main/MyNodes.txt",
        "https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/o/node.txt",
        "https://raw.githubusercontent.com/wudongdefeng/free/main/freevm/list_raw.txt",
        "https://raw.githubusercontent.com/xc0000e9/deatnote/main/Hiddify-next.fragment",
        "https://raw.githubusercontent.com/xc0000e9/deatnote/main/Test.txt",
        "https://raw.githubusercontent.com/ysmoradi/sub/main/clean.txt",
        "https://raw.githubusercontent.com/ysmoradi/sub/main/hiddify.txt",
        "https://rentry.co/8tq7w82x/raw",
        "https://rentry.co/DailyV2ry/raw",
        "https://gfw.mahsa/Mahsa",
        "https://zebelkhan10.fallahpour25.workers.dev/sub/74f829f3-480b-4e7f-8039-9418d055375b",
        "https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged_base64",
        "https://zebelkhan10.fallahpour25.workers.dev/sub/74f829f3-480b-4e7f-8039-9418d055375b",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/donated",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/mix_base64",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/vmess",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/trojan",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/shadowsocks",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/vmess",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/trojan",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/ss",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/splitted/mixed",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/shadowsocks",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/shadowsocks",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/ss_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/trojan_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/vmess_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/vmess_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/ss_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/trojan_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/merged",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/merged_base64",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub4/main/merged",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub4/main/merged_base64",
        "https://paste.gg/p/anonymous/21b6068195f14f7fac5f4f9a4cc77ac6/files/2e54b7f9fc5242bd82f804cb32ce9065/raw",
        "https://paste.gg/p/anonymous/b6094968dd974a5ba018ba9117655326/files/05c585aa155a4c54a0fcfab32403154e/raw",
        "https://dy.smjc.top/api/v1/client/subscribe?token=b12651a704cf680e5794f61827a46262",
        "https://dy.smjc.top/api/v1/client/subscribe?token=5bd7e01f6a299be186e5cd44f9c6c150",
        "https://paste.gg/p/anonymous/3f0c979d8eca4e5bb0be491e69c89501/files/990f7294ea214770a6fb04a336670f48/raw",
        "https://ninjasub.com/link/b1UjtCoAZeyyCFqE?clash=1",
        "https://yiyolink.xyz/link/J6OpSJ9lfi1YHzQI?clash=1",
        "https://yiyolink.xyz/link/J6OpSJ9lfi1YHzQI?sub=1",
        "https://yiyolink.xyz/link/J6OpSJ9lfi1YHzQI?sub=2",
    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)

    combined_data = decoded_links + decoded_dir_links
    merged_configs = filter_for_protocols(combined_data, protocols)

    # Clean existing output files
    output_filename = os.path.join(output_folder, "All_Configs_Sub.txt")
    filename1 = os.path.join(output_folder, "All_Configs_base64_Sub.txt")
    
    if os.path.exists(output_filename):
        os.remove(output_filename)
    if os.path.exists(filename1):
        os.remove(filename1)

    for i in range(20):
        filename = os.path.join(output_folder, f"Sub{i}.txt")
        if os.path.exists(filename):
            os.remove(filename)
        filename1 = os.path.join(base64_folder, f"Sub{i}_base64.txt")
        if os.path.exists(filename1):
            os.remove(filename1)

    # Write merged configs to output file
    with open(output_filename, "w") as f:
        f.write(fixed_text)
        for config in merged_configs:
            f.write(config + "\n")

    # Split merged configs into smaller files (no more than 600 configs per file)
    with open(output_filename, "r") as f:
        lines = f.readlines()

    num_lines = len(lines)
    max_lines_per_file = 600
    num_files = (num_lines + max_lines_per_file - 1) // max_lines_per_file

    for i in range(num_files):
        profile_title = f"🆓 Git:Barry-far | Sub{i+1} 🫂"
        encoded_title = base64.b64encode(profile_title.encode()).decode()
        custom_fixed_text = f"""#profile-title: base64:{encoded_title}
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/coldwater-10/V2ray-Config
#profile-web-page-url: https://github.com/coldwater-10/V2ray-Config
"""

        input_filename = os.path.join(output_folder, f"Sub{i + 1}.txt")
        with open(input_filename, "w") as f:
            f.write(custom_fixed_text)
            start_index = i * max_lines_per_file
            end_index = min((i + 1) * max_lines_per_file, num_lines)
            for line in lines[start_index:end_index]:
                f.write(line)

        with open(input_filename, "r") as input_file:
            config_data = input_file.read()
        
        output_filename = os.path.join(base64_folder, f"Sub{i + 1}_base64.txt")
        with open(output_filename, "w") as output_file:
            encoded_config = base64.b64encode(config_data.encode()).decode()
            output_file.write(encoded_config)

if __name__ == "__main__":
    main()
