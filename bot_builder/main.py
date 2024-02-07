import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from .config.settings import settings
from .core.core_module import CoreModule
from .bot_responses.bot_responses_module import BotResponsesModule
from .story_blocks.story_blocks_module import StoryBlocksModule
from .postgres.engine import create_db_and_tables
from .interceptors.response_interceptor import ResponseInterceptor

create_db_and_tables()

app = CoreModule(modules=[StoryBlocksModule, BotResponsesModule])
app.add_middleware(ResponseInterceptor)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def start():
    uvicorn.run("bot_builder.main:app",
                host="0.0.0.0", port=int(settings.PORT), reload=True)
