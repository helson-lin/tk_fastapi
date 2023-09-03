from fastapi import FastAPI
from douyin_tiktok_scraper.scraper import Scraper
from src.dtos.ISayHelloDto import ISayHelloDto

app = FastAPI()
api = Scraper()


def can_download(result):
    try:
        nwm_video_url_HQ = result['video_data']['nwm_video_url_HQ']
        return nwm_video_url_HQ
    except Exception as e:
        return None


async def hybrid_parsing(url: str):
    # Hybrid parsing(Douyin/TikTok URL)
    result = await api.hybrid_parsing(url)
    print(result['status'])
    if result['status'] == 'success':
        video_url = can_download(result)
        if video_url == None:
            return '视频主没有开放下载权限'
        else:
            return video_url
    else:
        return '解析失败'


@app.get("/")
async def root():
    return {"message": "server is running"}


@app.get("/tiktok")
async def tiktok(url: str):
    try:
        print(url)
        result = await hybrid_parsing(url=url)
        return result
    except Exception as e:
        return {"error": str(e)}
