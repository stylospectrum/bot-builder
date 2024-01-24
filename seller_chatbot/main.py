import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from .config.settings import settings
from .app_module import AppModule
from .story_blocks.story_blocks_module import StoryBlocksModule
from .postgres.engine import create_db_and_tables
from .response_interceptor import ResponseInterceptor

create_db_and_tables()

app = AppModule(modules=[StoryBlocksModule])
app.add_middleware(ResponseInterceptor)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def start():
    uvicorn.run("seller_chatbot.main:app",
                host="0.0.0.0", port=int(settings.PORT), reload=True)
