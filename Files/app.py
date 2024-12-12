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
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/hysteria",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/tuic",
        "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/hy2",
        "http://91.231.182.239:2096/sub/oUODTZ1C",
        "https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged_base64",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/donated",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/vmess",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/vless",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/trojan",
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/shadowsocks",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/vmess",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/vless",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/trojan",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/ss",
        "https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/base64/vless",
        "https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/base64/ss",
        "https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/base64/trojan",
        "https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/base64/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/vless",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/vless",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/shadowsocks",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/shadowsocks",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/merged_base64",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub4/main/merged_base64",
        "https://raw.githubusercontent.com/coldwater-10/V2Hub5/main/merged_base64",
        "https://sub1.achaemenidempireofpersia.uk/#IrancpinetSub2",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity",
        "https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/main/submerge/converted.txt",
        "https://dy.smjc.top/api/v1/client/subscribe?token=b12651a704cf680e5794f61827a46262",
        "https://dy.smjc.top/api/v1/client/subscribe?token=5bd7e01f6a299be186e5cd44f9c6c150",
        "https://sub.giga-downloader.com/clean.txt",
        "https://msdonor.pages.dev/sub/7f035a95-4b51-4e0b-8995-59864a9cde22#BPB-Normalhttps://qiaomenzhuanfx.netlify.app/",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/SS-Kcptun/ssconfig.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/SSR/ssconfig.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/ssconfig.txt",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/sub",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/vless",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/best",
        "https://raw.githubusercontent.com/voken100g/AutoSSR/master/online",
        "https://raw.githubusercontent.com/voken100g/AutoSSR/master/recent",
        "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Raw",
        "https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/main/sub64",
        "https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/master/Eternity",
        "https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/Shenzo.txt",
        "https://raw.githubusercontent.com/MrPooyaX/SansorchiFucker/main/data.txt",
        "https://raw.githubusercontent.com/ts-sf/fly/main/v2",
        "https://raw.githubusercontent.com/Vauth/node/main/Main",
        "https://raw.githubusercontent.com/Vauth/node/main/Pro",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_1.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_2.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_3.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mci/sub_4.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_1.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_2.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_3.txt",
        "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/mtn/sub_4.txt",
        "https://raw.githubusercontent.com/AzadNetCH/Clash/main/AzadNet_iOS.txt",
        "https://raw.githubusercontent.com/Mohammadgb0078/IRV2ray/main/vmess.txt",
        "https://raw.githubusercontent.com/Mohammadgb0078/IRV2ray/main/vless.txt",
        "https://nmsubs.com/interface/Client/getSubscribe?token=30d691c705d50a064e25e05dad555b3b",
        "https://duijie.cfyun.top/api/v1/client/subscribe?token=9dbea5a02c4c40b29f6795d13d06800a",
        "https://raw.githubusercontent.com/coldwater-10/V2ray-Configs/main/Splitted-By-Protocol/ssr.txt",
        "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/ssr",
        "https://proxy.crazygeeky.com/sip002/sub",
        "https://proxy.crazygeeky.com/ssr/sub",
        "https://proxy.crazygeeky.com/vmess/sub",
        "https://proxy.crazygeeky.com/trojan/sub",
        "https://raw.githubusercontent.com/coldwater-10/HiN-VPN/main/subscription/base64/hysteria2",
        "https://fs123121.cdn.22.jiacdnd123456789.com/answer/land?token=5ad57ba4f689c71ff7f79e9202262d9a",
        "https://sub.591haoka.com/api/v1/client/subscribe/token=9e48312624d64c219f8e7u9af55b4k961d68",
        "https://falcocloud.730894.xyz/api/v1/client/subscribe?token=2be7ea32053de07b2453f7516894b215",
        "https://tg.z-cloud.dynv6.net/token=Rn87qQA0uYVXBnFDocvwJ9fxnUoj1jiEExPB2W2jpCe4Grt7iqiyG123Ea5DEpkG",
        "https://xn--wtq35pfyd55o.co/pianyi/v0/client/subscribe?token=da9ada979edff7ddddf481d3b785ff83",
        "https://base64.bigwatermelon.org/api/v1/client/subscribe?token=232e5ebac1ee2506b51c049c2b8caad3",
        "https://syynweb.shop/api/v1/client/subscribe?token=f8c376caa12b91d4d8a0c54204c169fc",
        "https://getinfo.bigbigwatermelon.com/api/v1/client/subscribe?token=a3fe37757d77f2e3b46036ef1aebf864",
        "https://lancloud.zichuanlan.top/api/v1/client/subscribe?token=48c07997475799084107077567d0e5ea",
        "https://svip.365cloud.me/api/v1/client/subscribe?token=60aae69790a7f05417038e9815019620",
        "https://d.palu123.com/apk/go/client/banzou?token=6c16121cf3f11467566dbd1eecb9c36a&flag",
        "https://dy.kunkun.v6.navy/api/v1/client/subscribe?token=7fdf493f890d8c6ee6917f1741a69355",
        "https://dy.jntm.ikun.moshen.tech/api/v1/client/subscribe?token=3e855d259445709af8f1f379f8a489ca",
        "https://api.abyssyun.top/api/v1/client/subscribe?token=b2461a92a0d67ab065a2140d5b477d6f",
    ]
    dir_links = [
        "https://raw.githubusercontent.com/ndsphonemy/proxy-sub/main/hys-tuic.txt",
        "https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/normal/hysteria2",
        "https://raw.githubusercontent.com/coldwater-10/HiN-VPN/main/subscription/normal/hysteria2",
        "https://raw.githubusercontent.com/jahangirGH/sublinks/main/tuicsub.txt#IrancpinetSub1",
        "https://drive.google.com/uc?export=download&id=1Gkg2Ru0fO7-4UDNEks5vBWEXih-6_DKW",
        "https://raw.githubusercontent.com/coldwater-10/Vpnclashfa/main/raw/hy2.txt",
        "https://raw.githubusercontent.com/coldwater-10/Vpnclashfa/main/raw/tuic%20%26%20hy2.txt",
        "https://alienvpn402.github.io/AlienVPN402-subscribe-servers-sing-box",
        "https://raw.githubusercontent.com/Everyday-VPN/Everyday-VPN/main/subscription/main.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/ss_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/trojan_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/vmess_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorLire/main/vless_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/vmess_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/vless_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/ss_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollectorVpnclashfa/main/trojan_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollector_mahsaserver/main/ss_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollector_mahsaserver/main/vmess_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollector_mahsaserver/main/vless_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollector_mahsaserver/main/trojan_iran.txt",
        "https://miner.isherv.in",
        "https://api.yebekhe.link/shervin/",
        "https://raw.githubusercontent.com/1Shervin/Sub/main/v2ray",
        "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Realm",
        "https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/main/EdgeTunnel/ed",
        "https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity.txt",
        "https://mrsp137.github.io/NewSub_FREEV2RNG/@FREEV2RNG#FreeV2rng-1",
        "https://paste.gg/p/anonymous/21b6068195f14f7fac5f4f9a4cc77ac6/files/2e54b7f9fc5242bd82f804cb32ce9065/raw",
        "https://paste.gg/p/anonymous/b6094968dd974a5ba018ba9117655326/files/05c585aa155a4c54a0fcfab32403154e/raw",
        "https://paste.gg/p/anonymous/3f0c979d8eca4e5bb0be491e69c89501/files/990f7294ea214770a6fb04a336670f48/raw",
        "http://104.168.107.230/aggregate.txt",
        "https://sub.giga-downloader.com/hiddify.txt",
        "https://branch.blanku.me/",
        "https://eliv2ray.cloud/TLS-MCI-By-ELiV2RAY.txt",
        "https://gist.githubusercontent.com/johhny1898/eef96d3998241a8527bbb9557704d6bb/raw/0e6ff0583ca5e226e82756d0f602ae18d6ac5a9b/gistfile1.txt",
        "https://igdux.top/~Nekobox",
        "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/server.txt",
        "https://raw.githubusercontent.com/Ashkan-m/v2ray/main/Sub.txt",
        "https://raw.githubusercontent.com/Ashkan-m/v2ray/main/Sub_NoTest.txt",
        "https://raw.githubusercontent.com/nameless255/shadow/main/shadow.txt",
        "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/splitted/ssr.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2RayAggregator/master/sub/splitted/ssr.txt",
        "https://raw.githubusercontent.com/Rayan-Config/Rayan-Config.github.io/refs/heads/main/ALL",
        "https://raw.githubusercontent.com/Rayan-Config/Rayan-Config.github.io/refs/heads/main/CF",
        "https://raw.githubusercontent.com/Rayan-Config/Rayan-Config.github.io/refs/heads/main/FL",
        "https://raw.githubusercontent.com/Rayan-Config/Rayan-Config.github.io/refs/heads/main/GC",
        "https://raw.githubusercontent.com/Rayan-Config/Rayan-Config.github.io/refs/heads/main/HYS",
        "https://raw.githubusercontent.com/XYZMojtaba/sub/main/adsl.txt",
        "https://raw.githubusercontent.com/XYZMojtaba/sub/main/mci.txt",
        "https://raw.githubusercontent.com/XYZMojtaba/sub/main/mtn.txt",
        "https://raw.githubusercontent.com/XYZMojtaba/sub/main/mtn2.txt",
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
