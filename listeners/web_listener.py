import aiohttp, asyncio

async def stream_audio(url, output_file="streamed_audio.mp3"):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(output_file, "wb") as f:
                async for chunk in resp.content.iter_chunked(1024):
                    f.write(chunk)
    return output_file
